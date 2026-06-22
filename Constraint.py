import numpy as np

class Constraint():
    def __init__(self, coeffs: np.ndarray, type: str, rhs: float):
        self.coeffs = coeffs
        self.type   = type
        self.rhs    = rhs
    
    def get_coeffs(self):
        return self.coeffs
    
    def get_type(self):
        return self.type
    
    def get_rhs(self):
        return self.rhs
    
    def get_vector_rep(self):
        return np.concatenate((self.coeffs, self.rhs), axis=None)

    def deep_copy(self):
        deepcopy = Constraint(
            coeffs=self.coeffs.copy(),
            type=self.type,
            rhs=self.rhs
        )
        return deepcopy