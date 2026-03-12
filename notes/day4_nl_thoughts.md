1️⃣ Why do large weights increase overfitting risk?

Large weights increase overfitting risk because they make the model extremely sensitive to small changes or noise in the input, causing the model to fit noise rather than the true underlying pattern.  

2️⃣ Why might we want to penalize large weights?

We penalize large weights to encourage simpler, more stable models that generalize better to unseen data by reducing sensitivity to noise.

L2 regularization discourages large weights by adding a penalty term to the loss, resulting in smoother and more stable models that generalize better.

L1 regularization not only reduces overfitting but also reveals which features truly matter by eliminating irrelevant ones.

NB- Regularization increases bias slightly while significantly reducing variance, helping the model generalize better to unseen data.

Regularization:

Increases bias

Decreases variance