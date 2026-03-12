import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])
# plt.scatter(x,y)// plot training data
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("training data")
# plt.show()
# print("x shape:", x.shape)
# print("y shape:", y.shape)
x=np.c_[np.ones(len(x)), x]# add bias term
# print(x)
# print("x shape:", x.shape)

def mse_loss(x,y,w):# mean squared error loss function
    n=len(y)# number of samples
    y_pred=x @ w# predicted values
    loss=(1/n) * np.sum((y - y_pred) ** 2)# compute MSE
    return loss

# w_test=np.array([0.0,2.0])
# print("MSE Loss:", mse_loss(x,y,w_test))

# w_test=np.array([0.0,3.0])
# print("MSE Loss:", mse_loss(x,y,w_test))

# w_test=np.array([0.0,0.0])
# print("MSE Loss:", mse_loss(x,y,w_test))

def gradient(x,y,w): # gradient of MSE loss function
    n=len(y) # number of samples
    y_pred=x @ w # predicted values
    grad=(-2/n) * (x.T @ (y - y_pred)) # compute gradient
    return grad

w=np.array([0.0,0.0])#start with a bad guess
alpha=0.01 # learning rate
epoches=1000 # number of iterations
for i in range(epoches):
    grad=gradient(x,y,w)
    w=w-alpha*grad # update weights
    if i % 100 == 0:
        loss=mse_loss(x,y,w)
        print(f"Epoch {i}, Loss: {loss:.4f}, Weights: {w}")

y_pred=x @ w
# plt.scatter(x[:,1],y)
plt.scatter(x[:,1],y)# plot training data
plt.plot(x[:,1],y_pred)# plot the fitted line
plt.xlabel('x')
plt.ylabel('y') 
plt.title("Linear Regression fit")
plt.show()