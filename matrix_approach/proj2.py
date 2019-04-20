import numpy as np
import matplotlib.pyplot as plt
omat=np.array([[0,1],[-1,0]])
len=10
pi=1.55
def line_intersect(n2,n1,p1):
	
	N=np.vstack((n1,n2))
	p=np.array([p1,0])
	return np.matmul(np.linalg.inv(N),p)


l=np.linspace(0,1,10)
pil=(0,pi,10)
x_pop=np.zeros((2,10))
for j in range(8):
	yax=np.array([1,0])
	xax=np.array([0,1])
	line=np.array([np.cos((j+1)/6),np.sin((j+1)/6)])
	A=line_intersect(yax,line,1)
	B=line_intersect(xax,line,1)
	print(A)
	print(B)
	AB=A-B
	PQ=(A+B)/2
	print(AB)
	print("----------------------------")
	
	for i in range(len):
		temp=B+l[i]*(AB)
		x_pop[:,i]=temp.T
	plt.plot(x_pop[0,:],x_pop[1,:])	
	plt.plot(PQ[0],PQ[1],'o')
l=np.linspace(0.1,1.55,100)
locus=np.zeros((2,100))
for i in range(100):
	yax=np.array([1,0])
	xax=np.array([0,1])
	line=np.array([np.cos(l[i]),np.sin(l[i])])
	A=line_intersect(yax,line,1)
	B=line_intersect(xax,line,1)
	PQ=(A+B)/2
	print(PQ,i)
	locus[:,i]=PQ
	#plt.plot(PQ[0],PQ[1],'o',color='r')
plt.plot(locus[0,:],locus[1,:],label='locus',color='r')
plt.grid()
plt.xlim(-1,5)
plt.ylim(-1,5)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend(loc='best')
plt.axis('equal')
plt.show()
