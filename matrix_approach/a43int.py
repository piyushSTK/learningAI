import numpy as np
import matplotlib.pyplot as plt

A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])
a=(np.linalg.norm(C-B))
c=(np.linalg.norm(A-B))
b=(np.linalg.norm(C-A))
AU=(c*(B-A)+b*(C-A))/(b+c)
BV=(a*(C-B)+c*(A-B))/(a+c)
CW=(a*(B-C)+b*(A-C))/(a+b)
print(AU,BV,CW)

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
au=np.zeros((2,10))
bv=np.zeros((2,10))
cw=np.zeros((2,10))
ab=np.zeros((2,10))
bc=np.zeros((2,10))
ca=np.zeros((2,10))

len=10

for i in range(len):
	temp=A+(AU)*l[i]
	au[:,i]=temp.T
	temp=B+(BV)*l[i]
	cw[:,i]=temp.T
	temp=C+(CW)*l[i]
	bv[:,i]=temp.T
	temp=A+(B-A)*l[i]
	ab[:,i]=temp.T
	temp=B+(C-B)*l[i]
	bc[:,i]=temp.T
	temp=C+(A-C)*l[i]
	ca[:,i]=temp.T
	
plt.plot(au[0,:],au[1,:],label='$AU$')
plt.plot(bv[0,:],bv[1,:],label='$BV$')
plt.plot(cw[0,:],cw[1,:],label='$CW$')
plt.plot(ab[0,:],ab[1,:],label='$AB$')
plt.plot(bc[0,:],bc[1,:],label='$BC$')
plt.plot(ca[0,:],ca[1,:],label='$CA$')


plt.xlabel('$x$')
plt.xlabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
plt.show()
