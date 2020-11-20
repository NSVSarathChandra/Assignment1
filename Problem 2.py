import numpy as np
#AX = B
#X = Ainverse * B
A = np.array([[1,-2],[0,1]])
B = np.array([4,0])
A_inv = np.linalg.inv(A) 

X = np.matmul(A_inv, B)
print (X)