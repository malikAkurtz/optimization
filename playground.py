import numpy as np

def main():
    test_matrix = np.array([
        [1,2,3],
        [4,5,6]
    ], dtype=float)
    
    shallow_copy = test_matrix.copy()
    
    shallow_copy[0][0] = 2
    
    print("Original matrix: ")
    print(test_matrix)
    
    print("Shallow copy: ")
    print(shallow_copy)
    
def main1():
    arr = [1.0, 2.0]
    
    new_arr = arr * 5
    
    print(new_arr)
    
if __name__=="__main__":
    main1()