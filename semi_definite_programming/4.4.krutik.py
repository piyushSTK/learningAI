
from cvxopt import matrix
from cvxopt import solvers

c = matrix([-1.,-2.,-5.])
Aval = matrix([2.,3.,1.],(1,3))
bval = matrix([7.])
G = [ matrix([[-1., -1., 0., 0.],[ -1., 0., -1., 0.],[0.,  0.,  0., -1.]]) ]
h = [ matrix([[-1., 0.], [0., 0.]]) ]
sol = solvers.sdp(c, Gs=G, hs=h, A=Aval, b=bval)
print(sol['x'])

