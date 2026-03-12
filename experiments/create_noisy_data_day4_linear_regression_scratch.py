import numpy as np
import matplotlib.pyplot as plt

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