import numpy as np


def mid(B,C):
	D=(B+C)/2
	return D
def normal(AB):
	return np.matmul(omat,np.matmul(AB,dvec))
def line_intersect(AD,CF):
	n1=normal(AD)
	n2=normal(CF)
	N=np.vstack((n1,n2))
	p=np.zeros(2)
	p[0]=np.matmul(n1,AD[:,0])	
	p[1]=np.matmul(n2,CF[:,0])
	return np.matmul(np.linalg.inv(N),p)

A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])
D=mid(B,C)
E=mid(A,C)
F=mid(A,B)


AD=np.vstack((A,D)).T
CF=np.vstack((C,F)).T
BE=np.vstack((B,E)).T

dvec=np.array([-1,1])
omat=np.array([[0,1],[-1,0]])

print(line_intersect(AD,CF))
print(line_intersect(AD,BE))
print(line_intersect(BE,CF))
