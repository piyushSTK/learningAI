import numpy as np

A = np.matrix('8 0 3 ; 0 4 1; 3 1 0')
b = np.matrix('0 ;0 ; 8')
print (np.linalg.inv(A)*b)

#A = np.matrix('8 0 3 ; 0 4 1; 3 1 0')
#b = np.matrix('0 ;0 ; 8')
#print (np.linalg.inv(A)*b)

