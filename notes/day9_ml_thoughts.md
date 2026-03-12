d the core pipeline of logistic regression:

1️⃣ Linear model

z=(w^T)*x

2️⃣ Sigmoid converts it to probability

P=σ(z)

3️⃣ Cross-entropy measures how wrong the prediction is.

4️⃣ Gradient descent updates the weights to reduce that loss.

So logistic regression is basically:

Linear regression + sigmoid + cross-entropy.



2️⃣ Sigmoid function: 

Sigmoid converts any real number → probability between 0 and 1.

📈 What Sigmoid Does

If:
z→+∞ → output ≈ 1
z→−∞ → output ≈ 0
z=0 → output = 0.5

Formula:

σ(z)=1/(1+e^−z)

Where

z=(w^T)*x
So logistic regression does:

Compute a linear score 
(w^T)*x

Pass it through sigmoid

Get a probability

Example:

z	sigmoid(z)
-5	~0
0	0.5
5	~1

So sigmoid turns a line into an S-shaped probability curve.It converts any number → into (0,1).

🔥 Big Insight

Linear regression → straight line output
Logistic regression → straight line boundary + curved probability

🔥 Why We DON’T Use MSE for Logistic Regression

There are two big reasons.

1️⃣ Optimization Problem (Very Important)

If we use:

MSE=(y−(σ((w^T)*x)))^2

The loss function becomes:

❌ Non-convex

That means:

Multiple local minima
Gradient descent can get stuck
Training becomes unstable

We want a convex loss function so:

Only one global minimum
Optimization is reliable

2️⃣ Probability Theory Reason (Even More Important)

Logistic regression models:

P(y=1∣x)

For probability models, the correct loss is:
Log Loss (Cross-Entropy)
Why?

Because it comes from maximum likelihood estimation.
It directly answers:
What parameters make observed data most probable?
MSE does NOT align with probability theory.

🧠 Intuition Version

MSE treats problem like regression.
But logistic regression is about:

👉 Estimating probabilities
👉 Making likelihood of correct labels high

So we use:
Log Loss

🔥 What Log Loss Does

For true label y:

If y = 1:

−log(p)

If y = 0:

−log(1−p)

This heavily punishes:
Confident wrong predictions
Exactly what we want.


4️⃣ Gradient descent

It is a core optimization algorithm in machine learning used to find the optimal parameters (weights and biases) of a model by iteratively minimizing a loss function. This process is analogous to a person walking down a hill to find the lowest point in a valley.

How Gradient Descent Works

The algorithm follows an iterative process to reach the minimum point of the loss function, where the model's error is lowest: 

Initialization:
The process begins by assigning random initial values to the model's parameters (weights and biases).

Calculate the Gradient:
The algorithm computes the gradient (the slope or vector of partial derivatives) of the loss function with respect to the current parameters. The gradient indicates the direction of the steepest ascent.

Update Parameters: 
To minimize the loss, the parameters are updated by moving in the opposite direction of the gradient. The size of this step is controlled by a hyperparameter called the learning rate (alpha):

theta(new)=theta(old)-alpha*deltaJ(theta)

where 
theta= represents the parameters, 
alptha= the learning rate, and 
deltaJ(theta)= the gradient of the loss function.

Repeat: 
Steps are repeated until the algorithm converges, meaning the loss function stops decreasing significantly, and the parameters are close to their optimal values. 