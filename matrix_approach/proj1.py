import numpy as np
import matplotlib.pyplot as plt
omat=np.array([[0,1],[-1,0]])
len=50
def circle(i):
	p=O+(np.linalg.norm(OP))*(np.array([np.cos(i),np.sin(i)]))
	return p
def line_intersect():
	n1=np.array([2,1])
	n2=np.array([1,-1])
	N=np.vstack((n1,n2))
	p=np.array([3,1])
	return np.matmul(np.linalg.inv(N),p)

O=line_intersect()
print("intersection",O)
P=np.array([1,-1])
OP=O-P
print("normal",OP)
temp=np.matmul(OP,omat)
pOP=temp.T
print("tangent",pOP)
print("Equation of tangent is")
print(P,'+ t',pOP)
l=np.linspace(0,2,50)
x_pop=np.zeros((2,50))
x_pop2=np.zeros((2,50))
for i in range(len):
	temp=P+l[i]*(pOP)
	temp2=P-l[i]*(pOP)
	x_pop[:,i]=temp.T
	x_pop2[:,i]=temp2.T

	
plt.plot(x_pop[0,:],x_pop[1,:],label="$x+4y=-3$")
plt.plot(x_pop2[0,:],x_pop2[1,:],color='b')
plt.text(O[0]*1.1,O[1]*1.1,'O(1.33,0.33)')
plt.plot(O[0],O[1],'o')
plt.text(P[0]*1.1,P[1]*1.1,'P(-1,1)')
plt.plot(P[0],P[1],'o')
print("the radius of circle is 2.42")

c1=plt.Circle((O[0],O[1]), np.linalg.norm(OP), color='r', fill=False)
plt.gcf().gca().add_artist(c1)	
plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend(loc='best')
plt.axis('equal')
plt.show()
plt.savefig('plot.png')
