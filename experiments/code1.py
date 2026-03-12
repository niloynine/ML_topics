import numpy as np

# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# a=a.reshape(3,4)
# print(a)

# b=np.mean(a,axis=0,dtype=np.int32)
# print(b)
# c=np.sum(a,axis=1)
# print(c)

# A=np.random.randint(5,8,size=(2,3))
# print(A)
# B=np.random.randint(1,4,size=(3,2))
# print(B)
# print(np.dot(A,B))

# a=np.array([[1,2,3],[7,8,9]], dtype=np.int32)
# print(np.mean(a))
# print (np.mean(a,axis=1))    
# # print(np.sum(a,axis=0))
# # print(np.sum(a,axis=1))
# # print(np.sum(a,axis=0,keepdims=True))
# print(np.sum(a,axis=1,keepdims=True))
# t=np.array([[1,2,3,4,5,6],[10,11,12,13,14,15]])
# print(t)
# # print(t.shape)  
# # print(t.dtype)
# # print(t.ndim)
# # print(t.size)
# # print(t.itemsize)
# # print(t.nbytes)
# # print(t[:,5])
# # print(t[1,:])
# print(t[0,2:6:2])

# a=np.ones((5,5))
# z=np.zeros((3,3))

# z[1,1]=9
# print(z)
# print(a)
# a[1:4,1:4]=z
# print(a)

#linear regression
import matplotlib.pyplot as plt
# x=np.array([1,2,3,4,5])
# y=np.array([2,4,6,8,10])   
# plt.scatter(x,y)
# plt.xlabel('x') 
# plt.ylabel('y')
# plt.title('Linear Regression')  
# plt.show()
X=np.array([[1,1],[1,2],[1,3]])
W=np.array([2,3])
Y=X @ W
# print(Y)
# plt.scatter(X[:,1],Y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Linear Regression Prediction')
# plt.show()

plt.scatter(X[:,1],Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Prediction')
plt.show()