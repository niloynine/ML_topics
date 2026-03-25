
When building a model, we cannot evaluate it on the same data used for training.

Why?

Because the model might simply memorize the training data.

This leads to
Overfitting.

So we split the dataset into three parts.

1️⃣ Training Set

Purpose:

used to train the model

model learns patterns here

Example:

Model learns weights using this data

Usually about 70–80% of the data.

2️⃣ Validation Set

Purpose:

used to tune the model
choose hyperparameters
compare models

Example decisions:

learning rate
tree depth
regularization strength
Usually about 10–15% of the data.

3️⃣ Test Set

Purpose:

used only once at the end
gives the final unbiased performance

Important rule:

The model must never see the test data during training.
Usually about 10–15% of the data.

Visual Example:
Dataset
│
├── Training Set (70%)
│
├── Validation Set (15%)
│
└── Test Set (15%)


Dataset
│
├── Train → learn model parameters
│
├── Validation → choose best model
│
└── Test → final performance report