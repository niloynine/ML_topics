# import numpy as np
# x=np.array([[1,2],[2,1],[3,0],[0,3]])
# y=np.array([8,7,6,7])
# print("X shape:", x.shape)

# x=np.c_[np.ones(len(x)),x]# add bias column
# # print("x modified shape:",x.shape)
# print("Modified x:\n",x.astype(np.float32))

# w=np.zeros(x.shape[1])# initialize weights
# print("Initial weights:", w)

# y_pred=x@w# predicted values
# print("Initial predictions:", y_pred)

# def mse_loss(x,y,w):
#     n=len(y)# number of samples
#     y_pred=x@w# predicted values
#     loss=(1/n)*np.sum(y-y_pred)**2# compute MSE loss
#     return loss


# loss=mse_loss(x,y,w)
# print("Initial MSE Loss:", loss)




from sklearn.model_selection import train_test_split
import numpy as np
x=np.array([[i] for i in range (1,21)])
y=np.array([2*i for i in range (1,21)])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(x_train,y_train)

train_loss=np.mean((model.predict(x_train)-y_train)**2)
test_loss= np.mean((model.predict(x_test)-y_test)**2)
print("Train MSE Loss:", train_loss)
print("Test MSE Loss:", test_loss)