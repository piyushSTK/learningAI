import numpy as np
import matplotlib.pyplot as plt
def sq(x):
	return x**2

#Plotting log(x)
x = np.linspace(0.5,8,50)#points on the x axis
f=(x*x)#Objective function
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$\ln x$')


#Plot commands
#Plotting line segments with x>0 and y=logx 
#color used to color each line with a different color
plt.plot([1,4],[sq(1),sq(4)],color=(1,0,0),marker='o',label="($1$,$\ln(1)$)-($4$,$\ln(4)$)")
plt.plot([2,6],[sq(2),sq(6)],color=(0,1,0),marker='o',label="($2$,$\ln(2)$)-($6$,$\ln(6)$)")
plt.plot([3,5],[sq(3),sq(5)],color=(0,0,1),marker='o',label="($3$,$\ln(3)$)-($5$,$\ln(5)$)")
plt.legend(loc=2)
plt.show()
