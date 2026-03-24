Topic: Cross-Validation


What if dataset is too small?
A single train/validation split might give misleading results.

The Problem=
Suppose i split data like this:

Train: 80%
Validation: 20%
But what if that 20%:

is unusually easy? → accuracy looks high
is unusually hard? → accuracy looks low

👉 evaluation becomes unstable
The Solution — Cross-Validation

Instead of using one split, we use multiple splits.

K-Fold Cross-Validation-

Most common method:

Step-by-step (K = 5)

Split data into 5 parts:
Fold1 Fold2 Fold3 Fold4 Fold5

Then:

1️⃣ Train on 4 folds, validate on 1
2️⃣ Repeat 5 times (each fold becomes validation once)
Final performance = average of 5 folds result
Each time:
4 folds → training
1 fold → validation

Visualization

Run 1: [V] [T] [T] [T] [T]
Run 2: [T] [V] [T] [T] [T]
Run 3: [T] [T] [V] [T] [T]
Run 4: [T] [T] [T] [V] [T]
Run 5: [T] [T] [T] [T] [V]

(V = validation, T = training)


Why This Is Better?

Uses all data for validation
More stable results
Reduces randomness

Important Insight-
Cross-validation helps reduce problems related to:

small datasets
unlucky splits
unstable validation scores

Trade-offs:

Advantage	                Disadvantage
More reliable evaluation	Slower training
Better use of data	        Higher computation