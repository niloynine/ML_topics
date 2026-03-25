Real-World Thinking-

Different problems need different priorities:

Problem	            Important Metric
Cancer detection	Recall
Spam detection	    Precision
Balanced tasks	    F1 score
Why?
Missing a cancer patient = dangerous → high recall needed
Marking real email as spam = annoying → high precision needed

Model evaluation depends on the problem context, not just accuracy.

Precision measures how many predicted positives are correct, while recall measures how many actual positives are detected.

In critical applications like cancer or fraud detection, recall is more important because missing positive cases is dangerous.

In applications like spam filtering, precision is more important to avoid incorrect positive predictions.

Choosing the right metric is essential for building reliable machine learning systems.