#create multi feature synthetic data with noise to train a linear regression model with L1 regularization (Lasso) and observe the effect of regularization on the learned weights and predictions, especially in terms of sparsity of the learned coefficients
import numpy as np

np.random.seed(0)  # for reproducibility

x=np.random.rand(100,5)  # 100 samples, 5 features
true_w=np.array([2,0,0,1.5,0])  # true weights with sparsity (only 2 features are relevant)
#only the first and fourth features are relevant, the rest are irrelevant with zero weights
y = x @ true_w + np.random.normal(0,0.5,100)  # linear relation with noise

#train without regularization to see the effect of noise on the learned weights and predictions
from sklearn.linear_model import LinearRegression

model_plain=LinearRegression()  # plain linear regression without regularization
model_plain.fit(x,y)
print("No regularization weights:", model_plain.coef_)  # print the learned weights from plain linear regression    

#train with L1 regularization (Lasso) to see the effect of regularization on the learned weights and predictions, especially in terms of sparsity
from sklearn.linear_model import Lasso
model_lasso = Lasso(alpha=0.1)

model_lasso = Lasso(alpha=0.1)
model_lasso.fit(x,y)
print("Lasso Regression weights:", model_lasso.coef_)  # print the learned weights from Lasso regression, which should be sparse with some coefficients driven to zero due to L1 regularization 
