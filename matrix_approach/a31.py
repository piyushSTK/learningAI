import numpy as np

A=np.array([-2,-2])
B=np.array([1,3])
C=np.array([4,-1])
AB=np.vstack((A,B)).T
BC=np.vstack((B,C)).T
CA=np.vstack((C,A)).T
diff=np.array([-1,1])
AB=np.matmul(AB,diff)
BC=np.matmul(BC,diff)
CA=np.matmul(CA,diff)
perp=np.array([[0,1],[-1,0]])
pAB=np.matmul(AB,perp)
pBC=np.matmul(BC,perp)
pCA=np.matmul(CA,perp)
print(AB)
print(BC)
print(CA)
print(pAB)
print(pBC)
print(pCA)
