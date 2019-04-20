import numpy as np
import matplotlib.pyplot as plt
import subprocess
#																																										import shelx


A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])

D=B-A
print("A",A)
print("B",B)
print("D",D)
P=np.array([5,-3])
print("P",P)
N=P*D					#need to write algo for matrix multiplication
print(N)
