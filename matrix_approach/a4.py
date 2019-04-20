import numpy as np
def dir_vec(AB):
	return np.matmul(AB,devc)
def norm_vec(AB):
	return np.matmul(omat,P)

A=np.array([-2,-2])
B=np.array([1,3])
devc=np.array([-1,1])
omat=np.array([[0,1],
			   [-1,0]])
AB=np.vstack((A,B)).T
P=dir_vec(AB)
print(P)
print("normal is",norm_vec(AB))
C=B-A
print("line is ",A.T,"+t",(B-A).T)
print("vec*normal",)
