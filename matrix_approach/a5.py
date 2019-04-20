import numpy as np
import matplotlib.pyplot as plt
def mid(A,C):
	D=(A+C)/2;
	return D
defv=np.array([-1,1])
A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])
F=mid(A,B)
D=mid(C,B)
E=mid(A,C)

AD=np.vstack((A,D)).T
AD=np.matmul(AD,defv)
print(A,"+ t",AD)


BE=np.vstack((B,E)).T
BE=np.matmul(BE,defv)
print(B,"+ t",BE)


CF=np.vstack((C,F)).T
CF=np.matmul(CF,defv)
print(C,"+ t",CF)
