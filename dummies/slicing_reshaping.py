import numpy as np
data=[[ 11,22,33],
		[44,55,66],
		[77,88,99]]
data1=[11,22,33]
data1=np.array(data1)
data=np.array(data)
print(data)
print(data.shape)
print(data1.shape)
data1=data1.reshape(3,1)
print("data1",data1.shape)
print(data1)
data2=data1.reshape(1,3)
print(data2)
print("data2",data2.shape)
data3=np.matmul(data2,data1)
print("matrix multiplied",data3)