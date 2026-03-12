Scenario:

You build a disease detection model.

Dataset:

1000 people

990 healthy

10 sick

Model predicts:

“Everyone is healthy.”

❓ Question:

What is the accuracy?
Accuracy=1000*100/990​=99%
Why is that model useless despite high accuracy?
In disease detection, missing infected people is dangerous.

✅ True Positive (TP)

Predicted sick AND actually sick.

The model predicted no one as sick.

So:
TP = 0

❌ False Positive (FP)

Predicted sick BUT actually healthy.

Model never predicted sick.

So:
FP = 0

❌ False Negative (FN)

Predicted healthy BUT actually sick.

There are 10 sick people.
All were predicted healthy.

So:
FN = 10

✅ True Negative (TN)

Predicted healthy AND actually healthy.

990 healthy people were predicted healthy.

So:
TN = 990

📊 Final Correct Values

TP = 0

FP = 0

FN = 10

TN = 990

Now the dangerous part:

🔥 Recall (Sensitivity)
𝑅𝑒𝑐𝑎𝑙𝑙=𝑇𝑃/(𝑇𝑃+𝐹𝑁)=0/(0+10)=0

The model detects 0% of sick people.

That’s why accuracy alone is misleading.

🧠 Core Lesson

Accuracy can lie when:

Data is imbalanced

One class dominates

The cost of mistakes is unequal

In medical problems, fraud detection, security:

Missing positives is worse than being slightly wrong on negatives.

1️⃣ Precision

Formula:

Precision=
TP/(FP+TP)

Substitute values:

Precision=0

That is undefined mathematically.
In practice (in libraries like sklearn), it is treated as 0.
So:
Precision means:
Of all predicted positives, how many were correct?

Here, we predicted zero positives, so precision collapses.

2️⃣ Recall

Recall=
0/10=0
So:
👉 Recall = 0
The model finds 0% of sick people.

3️⃣ F1 Score

F1=(2×Precision×Recall)/(Precision+Recall)

We have:
Precision = 0
Recall = 0
So:

F1=0
🔥 Final Summary

Accuracy = 99%
Precision = 0
Recall = 0
F1 = 0

That’s why accuracy can completely lie.

🎯 Final Question for Today

If we care MOST about detecting sick people,
which metric should we prioritize:

A) Accuracy
B) Precision
C) Recall
D) F1

ans- recall
Recall is the priority.
Why Recall?
Recall answers:

“Out of all actually sick people, how many did we detect?”

In medical diagnosis:

Missing a sick patient (False Negative) is dangerous.

It can lead to:

Delayed treatment

Disease spread

Severe consequences

So we want:

Recall to be as high as possible.

🔥 In Your Disease Example

Model had:

Recall = 0
Meaning:

It detected 0% of sick people.

Even with 99% accuracy, it completely failed.

That’s why in:

Disease detection

Fraud detection

Cancer screening

Security threats

👉 Recall is critical

🧠 But Here’s the Advanced Insight

If we ONLY maximize recall:

The model might label everyone as sick.

Then:

Recall = 100%

But precision becomes terrible

That’s why sometimes we use:

👉 F1 Score (balance of precision & recall)
