import numpy as np

from Objective import Objective
from Constraint import Constraint
from Tableau import Tableau

from Debug import DEBUG, PRINT_DEBUG

class LinearProgram():
    def __init__(self, objective: Objective, constraints: list[Constraint]) -> None:
        self.constraints        = constraints
        
        self.num_constraints    = len(self.constraints)
        self.num_decision_vars  = len(self.constraints[0].coeffs)
        
        for i in range(self.num_constraints):
            if self.constraints[i].coeffs.size != self.num_decision_vars:
                raise RuntimeError("Coefficient vectors are inconsistent.")
        
        self.phase_2_objective   = objective
        
        self.num_slack_vars      = None
        self.num_artificial_vars = None
        self.phase_1_objective   = None
        
        self.num_vars            = None
        
        self.tableau = None
        
        self.solution = None
        
    @staticmethod
    def flip_type(type: str):
        if type == "<=":
            return ">="
        elif type == ">=":
            return "<="
        elif type == "=":
            return "="
        
    def standardize(self):
        # If objective is minimization, convert to maximization
        if self.phase_2_objective.type == "min":
            self.phase_2_objective.coeffs *= -1
            self.type = "max"
            
        # Convert each = constraint into two <= and >= constraints
        for i in range(self.num_constraints):
            if self.constraints[i].type == "=":
                new_le_constraint = Constraint(
                    coeffs=self.constraints[i].coeffs.copy(),
                    type="<=",
                    rhs=self.constraints[i].rhs
                )
                new_ge_constraint = Constraint(
                    coeffs=self.constraints[i].coeffs.copy(),
                    type=">=",
                    rhs=self.constraints[i].rhs
                )
                
                del self.constraints[i]
                
                self.constraints.append(new_le_constraint)
                self.constraints.append(new_ge_constraint)
        
        # Ensure rhs >= 0
        for i in range(self.num_constraints):
            if self.constraints[i].rhs < 0.0:
                self.constraints[i].coeffs *= -1
                self.constraints[i].rhs    *= -1
                self.constraints[i].type = LinearProgram.flip_type(type=self.constraints[i].type)
    
    def add_slack_variables(self):
        # For each constraint of type <=, add a slack and change type to =
        # For each constraint of type >=, subtract a slack and change type to =
        self.num_slack_vars = self.num_constraints
        
        zeros = np.zeros(self.num_slack_vars)
        
        for i in range(self.num_constraints):
            old_coeffs = self.constraints[i].coeffs.copy()
            
            to_concat = zeros.copy()
            if self.constraints[i].type == "<=":
                to_concat[i] = 1
            else:
                to_concat[i] = -1
            
            new_coeffs = np.concatenate((old_coeffs, to_concat), axis=None)
            
            self.constraints[i].coeffs = new_coeffs
            
        self.num_vars = self.num_decision_vars + self.num_slack_vars
            
    def add_artificial_variables(self):
        # Now, rhs >=0 and we will add an artificial variable to every constraint where the slack is negative
        
        self.num_artificial_vars = 0
        
        for i in range(self.num_constraints):
            if self.constraints[i].coeffs[self.num_decision_vars + i] == -1:
                self.num_artificial_vars += 1

        artificial_vars_left_to_assign = self.num_artificial_vars
        
        zeros = np.zeros(self.num_artificial_vars)
        
        for i in range(self.num_constraints):
            old_coeffs = self.constraints[i].coeffs.copy()
            
            to_concat = zeros.copy()
            
            # If this constraint has an artifical variable (if its slack is negative)
            if self.constraints[i].coeffs[self.num_decision_vars + i] == -1:
                to_concat[self.num_artificial_vars - artificial_vars_left_to_assign] = 1
                artificial_vars_left_to_assign -= 1
            
            new_coeffs = np.concatenate((old_coeffs, to_concat), axis=None)
            
            self.constraints[i].coeffs = new_coeffs
            
        self.phase_1_objective = Objective(
            type="max",
            coeffs=[-1] * self.num_artificial_vars
        )
                
        self.num_vars += self.num_artificial_vars
        
    @staticmethod
    def add_objective_row(matrix: np.ndarray, obj: Objective, type: int, pad_length: int) -> np.ndarray:
        new_matrix = matrix.copy()
    
        zero_padding = np.zeros(pad_length)
        
        if type == 2:
            padded_coeffs = np.concatenate((obj.coeffs.copy(), zero_padding.copy()))
        elif type == 1:
            padded_coeffs = np.concatenate((zero_padding.copy(), obj.coeffs.copy()))
                    
        new_matrix = np.vstack([new_matrix, np.append(padded_coeffs, 0.0)])
        
        return new_matrix
        
    def create_initial_tableau(self) -> Tableau:
        matrix = np.zeros((self.num_constraints, self.num_vars + 1))
        
        for i in range(self.num_constraints):
            constraint = self.constraints[i]
            coeffs     = constraint.get_coeffs()
            rhs        = constraint.get_rhs()
            
            for j in range(self.num_vars):
                matrix[i][j] = coeffs[j]
                
            matrix[i][-1] = rhs
        
        # Add phase 2 objective to matrix
        matrix = LinearProgram.add_objective_row(
            matrix=matrix,
            obj=self.phase_2_objective,
            type=2,
            pad_length=self.num_slack_vars + self.num_artificial_vars
        )
        
        # Add phase 1 objective to matrix
        matrix = LinearProgram.add_objective_row(
            matrix=matrix,
            obj=self.phase_1_objective,
            type=1,
            pad_length=self.num_decision_vars + self.num_slack_vars
        )
        
        # Determine initial basic variables        
        artificals = []
        
        # Add the artifical variables
        for i in range(self.num_artificial_vars):
            artificals.append(self.num_decision_vars + self.num_slack_vars + i)
            
        slacks_needed = self.num_constraints - self.num_artificial_vars
        slacks = []
        
        for i in range(slacks_needed):
            slacks.append(self.num_decision_vars + self.num_slack_vars - 1 - i)
            
        slacks.reverse()
        
        basic_vars = artificals + slacks
        
        tableau = Tableau(
            matrix=matrix,
            basic_vars=basic_vars
        )
        
        return tableau
                
    def optimize(self):
        PRINT_DEBUG("Putting LP in standard form.")
        self.standardize()
        
        PRINT_DEBUG("Constraints: ")
        for i in range(self.num_constraints):
            c = self.constraints[i]
            
            PRINT_DEBUG("*" * 10 + f"Constraint {i}" + "*" * 10)
            PRINT_DEBUG(c.coeffs)
            PRINT_DEBUG(c.type)
            PRINT_DEBUG(c.rhs)
        
        PRINT_DEBUG("Adding slack variables.")
        self.add_slack_variables()
        PRINT_DEBUG(f"# Slack variables: {self.num_slack_vars}")
        
        PRINT_DEBUG("Adding artificial_variables.")
        self.add_artificial_variables()
        PRINT_DEBUG(f"# Artificial variables: {self.num_artificial_vars}")
        
        PRINT_DEBUG(f"# Total variables: {self.num_vars}")
        
        PRINT_DEBUG("Constructing initial tableau.")
        self.tableau = self.create_initial_tableau()
        PRINT_DEBUG("Initial Tableau: ")
        PRINT_DEBUG(self.tableau.matrix)
        PRINT_DEBUG("Basic variables: ")
        PRINT_DEBUG(self.tableau.basic_vars)
        
        PRINT_DEBUG("Ensuring unit columns for basic variables.")
        self.tableau.matrix = Tableau.clear_columns(tableau=self.tableau)
        
        PRINT_DEBUG("Tableau pre-Phase 1:")
        PRINT_DEBUG(self.tableau.matrix)
        
        PRINT_DEBUG("Beginning Phase 1.")
        self.tableau = Tableau.simplex(tableau=self.tableau)
        PRINT_DEBUG("Phase 1 concluded.")
        
        PRINT_DEBUG("Tableau post-Phase 1: ")
        PRINT_DEBUG(self.tableau.matrix)
        
        problem_is_feasible = Tableau.objective_is_zero(tableau=self.tableau)
        if not problem_is_feasible:
            PRINT_DEBUG("Problem is not feasible.")
            raise RuntimeError("Problem is infeasible.")
        else:
            PRINT_DEBUG("Problem is feasible.")
            self.tableau.matrix = Tableau.phase_2_prep(
                tableau=self.tableau,
                num_artificial_vars=self.num_artificial_vars
            )
            self.num_vars -= self.num_artificial_vars
            self.num_artificial_vars = 0
            
        PRINT_DEBUG("Trimmed tableau post Phase 1: ")
        PRINT_DEBUG(self.tableau.matrix)
        
        PRINT_DEBUG("Beginning Phase 2.")
        self.tableau = Tableau.simplex(tableau=self.tableau)
        PRINT_DEBUG("Phase 2 concluded.")
        PRINT_DEBUG("Final tableau:")
        PRINT_DEBUG(self.tableau.matrix)
        
        PRINT_DEBUG("Solution:")
        self.solution = Tableau.get_solution(self.tableau)
        PRINT_DEBUG(self.solution)