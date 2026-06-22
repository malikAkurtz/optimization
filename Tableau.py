from __future__ import annotations
import numpy as np

import copy

from Debug import DEBUG, PRINT_DEBUG

class Tableau():
    def __init__(self, matrix: np.ndarray, basic_vars: list[int]):
        self.matrix = matrix
        self.basic_vars = basic_vars   
    
    @staticmethod
    def clear_columns(tableau: Tableau) -> np.ndarray:
        new_matrix = tableau.matrix.copy()
        
        # Loop through columns belonging to basic variables
        for i, variable in enumerate(tableau.basic_vars):
            PRINT_DEBUG(f"Row {i} corresponds to variable {variable}")
            # Ensure the variables column is a unit vector
            variable_column = tableau.matrix[:, variable]
            unit_vector = np.eye(len(tableau.matrix))[i]
            
            PRINT_DEBUG("Variable column:")
            PRINT_DEBUG(variable_column)
            PRINT_DEBUG("Should be: ")
            PRINT_DEBUG(unit_vector)
            
            if np.allclose(variable_column, unit_vector):
                PRINT_DEBUG("Variable column is unit vector, moving on.")
                continue
            else:
                PRINT_DEBUG("Variable column isn't unit vector, adding to obj row.")
                new_matrix[-1] += tableau.matrix[i]
                
        return new_matrix
    
    @staticmethod
    def ratio_test(coeff_vector: np.ndarray, rhs_vector: np.ndarray, basic_vars: np.ndarray) -> int:
        PRINT_DEBUG("Performing ratio test.")
        
        PRINT_DEBUG("Coefficients: ")
        PRINT_DEBUG(coeff_vector)
        
        PRINT_DEBUG("RHS: ")
        PRINT_DEBUG(rhs_vector)
        
        if coeff_vector.shape != rhs_vector.shape:
            PRINT_DEBUG("ERROR: Coefficient vector and RHS vector have inconsistent shapes.")
            return -1
        
        num_basic_vars = coeff_vector.size
        
        ratios = [rhs_vector[i] / coeff_vector[i] if (coeff_vector[i] > 0.0) else np.inf for i in range(num_basic_vars)]
        ratios = np.array(ratios)
        
        PRINT_DEBUG("Ratios: ")
        PRINT_DEBUG(ratios)
        
        if np.allclose(ratios, np.array([np.inf] * num_basic_vars)):
            PRINT_DEBUG("Problem is unbounded.")
            raise RuntimeError("Problem is unbounded.")
        else:
            # This is the index of the leaving variable in the basic_vars array
            leaving_variable_idx = np.argmin(ratios)
            
            leaving_variable = basic_vars[leaving_variable_idx]
            
            return leaving_variable
        
    @staticmethod
    def pivot(tableau: Tableau, entering_variable: int, entering_variable_idx: int) -> np.ndarray:
        new_matrix = tableau.matrix.copy()
        
        PRINT_DEBUG("Tableau coming into pivot function:")
        PRINT_DEBUG(new_matrix)
        
        PRINT_DEBUG(f"Entering variable is now at row: {entering_variable_idx}")
            
        PRINT_DEBUG(f"Dividing row {entering_variable_idx} by {new_matrix[entering_variable_idx][entering_variable]}")
        new_matrix[entering_variable_idx] = new_matrix[entering_variable_idx] / new_matrix[entering_variable_idx][entering_variable]
        
        PRINT_DEBUG("Tableau after normalization.")
        PRINT_DEBUG(new_matrix)
        
        PRINT_DEBUG("Performing pivot.")
        for i in range(tableau.matrix.shape[0]):
            if i == entering_variable_idx:
                continue
            
            PRINT_DEBUG(f"Correcting row: {i}")
            
            scalar = new_matrix[i][entering_variable].item()
            
            PRINT_DEBUG(f"Row scalar: {scalar}")
                                
            new_matrix[i] += (-1 * scalar * new_matrix[entering_variable_idx])
            
        PRINT_DEBUG("New tableau: ")
        PRINT_DEBUG(new_matrix)
        
        return new_matrix
    
    @staticmethod
    def simplex(tableau: Tableau) -> Tableau:
        # This method assumes the last row is the objective row to maximize
        new_tableau = copy.copy(tableau)
        
        num_vars = new_tableau.matrix.shape[1] - 1        
        optimal_solution_found = False
        
        # for _ in range(5):
        while not optimal_solution_found:
            # Determine the entering variable
            obj_coeffs = new_tableau.matrix[-1][:-1]
            
            entering_variable = 0
            c = obj_coeffs[0]
            
            for i in range(num_vars):
                if obj_coeffs[i] > c:
                    entering_variable = i
                    c = obj_coeffs[i]
            
            # If largest coefficient in obj row is <= 0, end simplex, BFS is optimal
            if c < 0 or np.isclose(c, 0):
                PRINT_DEBUG("Optimal solution found, terminating simplex.")
                return new_tableau
            
            PRINT_DEBUG(f"Entering variable: {entering_variable}, c={c}")

            # Determine the leaving variable
            leaving_variable = Tableau.ratio_test(
                coeff_vector=new_tableau.matrix[:len(tableau.basic_vars), entering_variable],
                rhs_vector=new_tableau.matrix[:len(tableau.basic_vars), -1],
                basic_vars=new_tableau.basic_vars
            )
            
            PRINT_DEBUG(f"Leaving variable: {leaving_variable}")
            
            # Add entering variable to basic_vars in proper index
            leaving_variable_idx = new_tableau.basic_vars.index(leaving_variable)
            new_tableau.basic_vars[leaving_variable_idx] = entering_variable
            
            PRINT_DEBUG("New basic variables: ")
            PRINT_DEBUG(new_tableau.basic_vars)
            
            # Need to get the index of the entering variable in the tableau
            entering_variable_idx = new_tableau.basic_vars.index(entering_variable)
            
            # Perform the pivot
            new_tableau.matrix = Tableau.pivot(
                tableau=new_tableau,
                entering_variable=entering_variable,
                entering_variable_idx=entering_variable_idx
            )
            
        return new_tableau
    
    @staticmethod
    def objective_is_zero(tableau: Tableau) -> bool:
        if not np.isclose(tableau.matrix[-1][-1], 0.0):
            return False
        else:
            return True
        
    @staticmethod
    def phase_2_prep(tableau: Tableau, num_artificial_vars: int) -> np.ndarray:
        new_matrix = tableau.matrix.copy()
        
        # Delete columns of artifical variables
        for i in range(num_artificial_vars):
            new_matrix = np.delete(new_matrix, -2, axis=1)
        
        # Delete the bottom most objective row (the phase 1 objective row)
        new_matrix = np.delete(new_matrix, -1, axis=0)
        
        return new_matrix
    
    @staticmethod
    def get_solution(tableau: Tableau) -> tuple[float]:
        # Assuming the last row is the objective
        solution = []
        
        for variable in range(tableau.matrix.shape[1]-1):
            if variable in tableau.basic_vars:
                variable_idx = tableau.basic_vars.index(variable)
                value = tableau.matrix[variable_idx][-1]
                solution.append(value)
            else:
                solution.append(0.0)
                
        solution = tuple(solution)
        
        return solution
    
    def __copy__(self):
        copy = Tableau(
            matrix=self.matrix.copy(),
            basic_vars=self.basic_vars.copy()
        )
        return copy

    
        
