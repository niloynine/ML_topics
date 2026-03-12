Why We Split Data?

If we train and test on the same data, the model can memorize instead of learning.
This leads to Overfitting.
So we split the dataset into three parts:

Dataset	            Purpose
Training Set	    Model learns patterns
Validation Set	    Tune model settings
Test Set	        Final unbiased evaluation


#The Danger of Using the Test Set

The test set must remain untouched.

If you repeatedly check performance on the test set and adjust your model, you start training on the test data indirectly.This ruins the fairness of evaluation.This is why ML researchers introduced cross-validation.
K-Fold Cross Validation:
Instead of one split, we divide the data into K parts.Then we average the results.
This gives a much more reliable estimate of model performance.

Cross-validation helps:

✔ detect overfitting
✔ use small datasets efficiently
✔ compare models fairly

It’s standard in research papers and ML competitions.