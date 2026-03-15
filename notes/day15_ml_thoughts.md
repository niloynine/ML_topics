Core Idea of Boosting

Instead of training many independent models (like Random Forest), boosting trains models sequentially.

Each new model tries to fix the mistakes of the previous model.

Think of it like a student learning:

1️⃣ First attempt → many mistakes
2️⃣ Teacher shows mistakes
3️⃣ Second attempt focuses on those mistakes
4️⃣ Repeat until performance improves

Key Difference from Random Forest-

Method	                Idea

Random Forest	        many trees trained independently
Gradient Boosting	    trees trained sequentially to fix errors

Why Boosting Is Powerful?
Algorithms like:

XGBoost
LightGBM

dominate many real-world ML competitions because they:

1. handle complex patterns
2. reduce bias
3. reduce variance

In Gradient Boosting the model repeatedly focuses on mistakes.

But sometimes those mistakes are not real patterns — they may be:

noise
measurement errors
outliers

If the model keeps trying to fix them, it may start memorizing noise. This leads to Overfitting.

How Real Systems Prevent This?

Modern boosting systems like: XGBoost, LightGBM control overfitting using:

1. learning rate
2. tree depth limits
3. regularization
4. early stopping