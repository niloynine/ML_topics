🌳 Decision Trees

A decision tree works like a sequence of questions.

Example: disease diagnosis

Is fever > 38°C?
        |
     Yes / No
      |     |
   cough?   healthy
   |    |
 yes   no
flu   cold

The model keeps asking simple questions about features until it reaches a prediction.

Why Decision Trees Are Powerful

They are popular because they are:

✔ Easy to understand
✔ Work for classification and regression
✔ Handle nonlinear patterns
✔ Require little preprocessing

They are also the foundation of powerful models like Random Forest and Gradient Boosting.
Key Idea

At every step the tree asks:

Which question splits the data best?

To decide this, the algorithm measures impurity.

One common impurity measure is:

Gini Impurity

Intuition of Gini Impurity:

It measures how mixed the classes are.

Perfect node
All samples same class.

Mixed node
not all are in same class

Decision trees can grow too deep and memorize training data.
That leads to the same issue we discussed earlier:
Overfitting.

How We Prevent Overfitting

We control the tree using hyperparameters:

Parameter	        Meaning
Max depth	        limit how deep the tree can grow
Min samples split	require enough data before splitting
Min samples leaf	minimum samples per leaf

These keep the tree simpler and more generalizable.