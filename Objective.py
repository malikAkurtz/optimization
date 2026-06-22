import numpy as np

class Objective():
    def __init__(self, type: str, coeffs: np.ndarray):
        self.type = type
        self.coeffs = coeffs
        
    def deep_copy(self):
        deepcopy = Objective(
            type=self.type,
            coeffs=self.coeffs.copy()
        )
        return deepcopy