import numpy as np

from Objective import Objective
from Constraint import Constraint
from LinearProgram import LinearProgram
from Tableau import Tableau

def test_ex_geometric():
    obj = Objective(
        type="max",
        coeffs=np.array([3, 2], dtype=float)
    )
    
    constraint_0 = Constraint(
        coeffs=np.array([-1, 3], dtype=float),
        type="<=",
        rhs=12
    )
    constraint_1 = Constraint(
        coeffs=np.array([1, 1], dtype=float),
        type="<=",
        rhs=8
    )
    constraint_2 = Constraint(
        coeffs=np.array([2, -1], dtype=float),
        type="<=",
        rhs=10
    )
    
    constraints = [constraint_0, constraint_1, constraint_2]
    
    lp = LinearProgram(
        objective=obj,
        constraints=constraints
    )
    
    lp.optimize()
    
    assert Tableau.get_solution(lp.tableau)[:lp.num_decision_vars] == (6.0, 2.0), "Geometric example fail."
    
def test_ex_2_1():
    obj = Objective(
        type="max",
        coeffs=np.array([6, 8, 5, 9], dtype=float)
    )
    
    constraint_0 = Constraint(
        coeffs=np.array([2, 1, 1, 3], dtype=float),
        type="<=",
        rhs=5
    )
    constraint_1 = Constraint(
        coeffs=np.array([1, 3, 1, 2], dtype=float),
        type="<=",
        rhs=3
    )
    
    constraints = [constraint_0, constraint_1]
    
    lp = LinearProgram(
        objective=obj,
        constraints=constraints
    )
    
    lp.optimize()
    
    assert Tableau.get_solution(lp.tableau)[:lp.num_decision_vars] == (2.0, 0.0, 1.0, 0.0), "Exercise 2.1 fail."
    
def test_ex_2_2():
    obj = Objective(
        type="max",
        coeffs=np.array([2, 1], dtype=float)
    )
    
    constraint_0 = Constraint(
        coeffs=np.array([2, 1], dtype=float),
        type="<=",
        rhs=4
    )
    constraint_1 = Constraint(
        coeffs=np.array([2, 3], dtype=float),
        type="<=",
        rhs=3
    )
    constraint_2 = Constraint(
        coeffs=np.array([4, 1], dtype=float),
        type="<=",
        rhs=5
    )
    constraint_3 = Constraint(
        coeffs=np.array([1, 5], dtype=float),
        type="<=",
        rhs=1
    )
    
    constraints = [constraint_0, constraint_1, constraint_2, constraint_3]
    
    lp = LinearProgram(
        objective=obj,
        constraints=constraints
    )
    
    lp.optimize()
    
    assert Tableau.get_solution(lp.tableau)[:lp.num_decision_vars] == (1, 0), "Exercise 2.2 fail."
    
def test_ex_2_3():
    obj = Objective(
        type="max",
        coeffs=np.array([2, -6, 0], dtype=float)
    )
    
    constraint_0 = Constraint(
        coeffs=np.array([-1, -1, -1], dtype=float),
        type="<=",
        rhs=-2
    )
    constraint_1 = Constraint(
        coeffs=np.array([2, -1, 1], dtype=float),
        type="<=",
        rhs=1
    )

    constraints = [constraint_0, constraint_1]
    
    lp = LinearProgram(
        objective=obj,
        constraints=constraints
    )
    
    lp.optimize()
    
    assert Tableau.get_solution(lp.tableau)[:lp.num_decision_vars] == (0, 1/2, 3/2), "Exercise 2.3 fail."
    
def test_ex_2_6():
    obj = Objective(
        type="max",
        coeffs=np.array([1, 3], dtype=float)
    )
    
    constraint_0 = Constraint(
        coeffs=np.array([-1, -1], dtype=float),
        type="<=",
        rhs=-3
    )
    constraint_1 = Constraint(
        coeffs=np.array([-1, 1], dtype=float),
        type="<=",
        rhs=-1
    )
    constraint_2 = Constraint(
        coeffs=np.array([1, 2], dtype=float),
        type="<=",
        rhs=2
    )
    
    constraints = [constraint_0, constraint_1, constraint_2]
    
    lp = LinearProgram(
        objective=obj,
        constraints=constraints
    )
    
    try:
        lp.optimize()
        assert False, "Infeasibility excpetion not raised."
    except RuntimeError:
        pass
        
def test_ex_2_7():
    obj = Objective(
        type="max",
        coeffs=np.array([1, 3], dtype=float)
    )
    
    constraint_0 = Constraint(
        coeffs=np.array([-1, -1], dtype=float),
        type="<=",
        rhs=-3
    )
    constraint_1 = Constraint(
        coeffs=np.array([-1, 1], dtype=float),
        type="<=",
        rhs=-1
    )
    constraint_2 = Constraint(
        coeffs=np.array([-1, 2], dtype=float),
        type="<=",
        rhs=2
    )
    
    constraints = [constraint_0, constraint_1, constraint_2]
    
    lp = LinearProgram(
        objective=obj,
        constraints=constraints
    )
        
    try:
        lp.optimize()
        assert False, "Unbounded excpetion not raised."
    except RuntimeError:
        pass
    
def test_ex_notes():
    obj = Objective(
        type="min",
        coeffs=np.array([6, 3], dtype=float)
    )
    
    constraint_0 = Constraint(
        coeffs=np.array([1, 1], dtype=float),
        type=">=",
        rhs=1
    )
    constraint_1 = Constraint(
        coeffs=np.array([2, -1], dtype=float),
        type=">=",
        rhs=1
    )
    constraint_2 = Constraint(
        coeffs=np.array([0, 3], dtype=float),
        type="<=",
        rhs=2
    )

    constraints = [constraint_0, constraint_1, constraint_2]
    
    lp = LinearProgram(
        objective=obj,
        constraints=constraints
    )
    
    lp.optimize()
    
    assert Tableau.get_solution(lp.tableau)[:lp.num_decision_vars] == (2/3, 1/3), "Exercise from notes sheet fail."
    
def run_tests():
    print(f"*" * 20 + " Testing geometric example " + "*" * 20)
    test_ex_geometric()
    
    print(f"*" * 20 + " Testing exercise 2.1 " + "*" * 20)
    test_ex_2_1()
    
    print(f"*" * 20 + " Testing exercise 2.2 " + "*" * 20)
    test_ex_2_2()
    
    print(f"*" * 20 + " Testing exercise 2.3 " + "*" * 20)
    test_ex_2_3()
    
    print(f"*" * 20 + " Testing exercise 2.6 " + "*" * 20)
    test_ex_2_6()
    
    print(f"*" * 20 + " Testing exercise 2.7 " + "*" * 20)
    test_ex_2_7()
    
    print(f"*" * 20 + " Testing note sheet example " + "*" * 20)
    test_ex_notes()
    
    print("All tests passed.")

    
if __name__=="__main__":
    run_tests()