import numpy as np
#AX = B
#X = Ainverse * B
myvec_A = np.array([[1,-2],[0,1]])
myvec_B = np.array([4,0])
myvec_A_inv = np.linalg.inv(myvec_A) 

myvec_X = np.matmul(myvec_A_inv, myvec_B)
print (myvec_X)