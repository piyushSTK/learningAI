import numpy as np

A = np.matrix('0 0 1 3; 0 0 1 2; 1 1 0 0; 3 2 0 0')
b = np.matrix('-6 ; -5 ; 5; 12')
print (np.linalg.inv(A)*b)
