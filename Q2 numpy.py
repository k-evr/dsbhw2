import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[3,5],[4,6]])
common = np.array([i for i in A if i in B])
print(common)
