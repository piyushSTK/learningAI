import numpy as np
import matplotlib.pyplot as plt
len=10

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
l=np.linspace(0,1,10)
ad=np.zeros((2,10))
be=np.zeros((2,10))
cf=np.zeros((2,10))
ab=np.zeros((2,10))
bc=np.zeros((2,10))
ca=np.zeros((2,10))
A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])
D=mid(B,C)
E=mid(A,C)
F=mid(A,B)


AD=np.vstack((A,D)).T
CF=np.vstack((C,F)).T
BE=np.vstack((B,E)).T

for i in range(len):
	temp=A+(D-A)*l[i]
	ad[:,i]=temp.T
	temp=B+(E-B)*l[i]
	cf[:,i]=temp.T
	temp=C+(F-C)*l[i]
	be[:,i]=temp.T
	temp=A+(B-A)*l[i]
	ab[:,i]=temp.T
	temp=B+(C-B)*l[i]
	bc[:,i]=temp.T
	temp=C+(A-C)*l[i]
	ca[:,i]=temp.T
	
dvec=np.array([-1,1])
omat=np.array([[0,1],[-1,0]])
P=line_intersect(AD,CF)
Q=line_intersect(AD,BE)
R=line_intersect(BE,CF)
print(AD)
print(BE)
print(CF)
print(P)
print(Q)
print(R)
plt.plot(A[0],A[1],'o')
plt.text(A[0]*1.1,A[1]*1.1,'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*1.1,B[1]*1.1,'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*1.1,C[1]*1.1,'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*1.1,D[1]*1.1,'D')
plt.plot(E[0],E[1],'o')
plt.text(E[0]*1.1,E[1]*1.1,'E')
plt.plot(F[0],F[1],'o')
plt.text(F[0]*1.1,F[1]*1.1,'F')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*1.1,P[1]*1.1,'G')
plt.plot(ad[0,:],ad[1,:],label='$AD$')
plt.plot(be[0,:],be[1,:],label='$BE$')
plt.plot(cf[0,:],cf[1,:],label='$CF$')
plt.plot(ab[0,:],ab[1,:],label='$AB$')
plt.plot(bc[0,:],bc[1,:],label='$BC$')
plt.plot(ca[0,:],ca[1,:],label='$CA$')

plt.xlabel('$x$')
plt.xlabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
plt.show()
