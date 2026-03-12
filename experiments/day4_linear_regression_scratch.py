

import numpy as np
import matplotlib.pyplot as plt


#create synthetic linear data with noise to train a linear regression model without regularization and observe the effect of noise on the learned weights and predictions
np.random.seed(0)# for reproducibility

#linspace generates 50 evenly spaced values between 0 and 10, reshape to make it a 2D array with one column (feature)
x=np.linspace(0,10,50).reshape(-1,1)# 50 samples, 1 feature #linear space from 0 to 10, reshape to (50,1) for model training  #reshape x to 2D for model training
#for linear regression, x should be 2D (n_samples, n_features) and y should be 1D (n_samples,)
print("x shape:", x.shape)
y=2*x.flatten()+np.random.normal(0,3,size=50)# linear relation with noise  # flatten x to 1D for y calculation #reshape x to 2D for model training 
print("y shape:", y.shape)

plt.scatter(x,y)
plt.xlabel("x")     
plt.ylabel("y")
plt.title("Synthetic Linear Data")
plt.show()


#train a plain linear regression model without regularization to see the effect of noise on the learned weights and predictions
from sklearn.linear_model import LinearRegression #import LinearRegression from sklearn to perform linear regression

model_plain=LinearRegression()# create an instance of LinearRegression without regularization (plain linear regression)
model_plain.fit(x,y)# fit the model to the data (x,y) to learn the coefficients and intercept for the linear relationship between x and y
print("Plain Linear Regression Coefficients:", model_plain.coef_, "Intercept:", model_plain.intercept_)# print the coefficients and intercept learned by the plain linear regression model
print("No regularization weight:", model_plain.coef_)# print the weight (coefficient) learned by the plain linear regression model, which represents the slope of the line fitting the data.

#train a ridge regression model with L2 regularization to see the effect of regularization on the learned weights and predictions
from sklearn.linear_model import Ridge #import Ridge from sklearn to perform ridge regression
model_ridge=Ridge(alpha=10)#alpha=lamda #create an instance of Ridge regression with a regularization strength of alpha=10 to see the effect of regularization on the learned weights and predictions
model_ridge.fit(x,y) #fit the ridge regression model to the data (x,y) to learn the coefficients and intercept while applying L2 regularization to prevent overfitting
print("Ridge Regression Coefficients:", model_ridge.coef_, "Intercept:", model_ridge.intercept_)# print the coefficients and intercept learned by the ridge regression model, which should be smaller than those of the plain linear regression model due to the effect of regularization

plt.scatter(x, y)
plt.plot(x, model_plain.predict(x), label="No regularization")
plt.plot(x, model_ridge.predict(x), label="Ridge")
plt.title("Linear Regression with and without Regularization")
plt.legend()# add a legend to differentiate between the predictions of the plain linear regression and ridge regression models
plt.show()
