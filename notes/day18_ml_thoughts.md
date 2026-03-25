Hyperparameter Tuning

In Machine Learning, there are two types of parameters:

1️⃣ Model Parameters

learned automatically
example: weights in linear regression

2️⃣ Hyperparameters

set before training
control how the model learns

Examples:

learning rate
number of epochs
regularization strength
tree depth

How do we choose the best hyperparameters?
Method 1 — Grid Search

This is the brute-force method.

You define values like:

learning_rate = [0.01, 0.1, 1]
depth = [3, 5, 7]

Try all combinations:

(0.01,3), (0.01,5), (0.01,7)
(0.1,3),  (0.1,5),  (0.1,7)
(1,3),    (1,5),    (1,7)

👉 Train model on each
Method 2 — Random Search

Instead of trying everything:

👉 randomly pick combinations

Example:

(0.01,5)
(1,3)
(0.1,7)

Why Random Search Is Preferred in Practice?

In real-world Machine Learning projects:

datasets are large
models are complex
training is expensive
Grid search becomes too slow because it tries every combination.

Real-World Insight-

In industry and research:

Start with random search
Then optionally refine with smaller grid search around good regions
This is a common strategy in Hyperparameter Optimization.