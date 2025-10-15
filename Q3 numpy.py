import numpy as np
A = np.array([1,3,5,7,9,11,13])
result = (A >= 5) & (A <= 10)
num = A[result]
print(num)