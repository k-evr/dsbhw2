import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[3,5],[4,6]])
vert = np.vstack((A,B))
hor = np.hstack((A,B))
print(vert)
print(hor)
