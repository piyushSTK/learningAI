#Author:P N V S S K Havish

import cvxpy as cp
import numpy as np
import csv

#Funtion yo read files
def read_data(filename):
    X=[]
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            X.append(np.array(row).astype('float64'))
    X=np.array(X)
    return X

#Reading Xsvm.csv and ysvm.csv files
X=read_data('Xsvm.csv')
y=read_data('ysvm.csv')
#print(X.shape)
#print(y.shape)

#Training the SVM

# initialisations for convex optimization, the problem is solved on the dual of the original problem statement
alpha = cp.Variable(len(y))
term2 = cp.matmul(X.T,cp.matmul(cp.diag(alpha),y))
term2 = cp.norm(term2)**2

#Figure out how it works based on manual

term1 = cp.sum(alpha)
full = term1 - 0.5*term2 #Objective Function

constraint = cp.matmul(alpha.T,y)
Constraint = [0<=alpha,constraint == 0]  #Constraint in standard form
obj = cp.Maximize(full)
prob = cp.Problem(obj, Constraint)
prob.solve(verbose=True)

Alpha=np.array(alpha.value).reshape(500,)


w=np.dot(X.T,np.matmul(np.diag(Alpha),y))
w=w.reshape(2,1)
#print(w)

Alpha[Alpha<1e-3]=0
#print(np.nonzero(Alpha))


w0=(1/y[469])-np.dot(w.T,X[469].reshape(2,1))
#print(w0)


# Testing the trained SVM
test=np.array([[2,-0.5],[0.8,0.7],[1.58,-1.33],[0.008, 0.001]])
for elem in test:
    if np.dot(w.T,elem)+w0>0:
        print("The class is 1")
    else:
        print("The class is -1")

