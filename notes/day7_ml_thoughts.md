How do we evaluate model performance across ALL thresholds?

Answer → ROC Curve

ROC = Receiver Operating Characteristic Curve

It plots:

Axis	Meaning
X-axis	False Positive Rate (FPR)
Y-axis	True Positive Rate (Recall / TPR)

TPR (Recall):

TP / (TP + FN)


FPR:

FP / (FP + TN)

What ROC Curve Shows?

It shows how model behaves when threshold moves from:
Very Strict → Very Loose
Meaning:
High threshold → Low threshold

Ideal Model ROC:

Perfect model:
Goes straight up
Then across top

Bad model:
Diagonal line (random guessing)

What is AUC?
AUC = Area Under Curve

It summarizes ROC into single number.

AUC	Meaning
1.0	Perfect model
0.9	Excellent
0.8	Good
0.7	Okay
0.5	Random guess

🏥 In Medical Models

We want:

High AUC

High Recall zone available

Because we can choose low threshold safely.

Important- 📌 Why ROC > Accuracy

Accuracy = single threshold result
ROC = performance across all thresholds

🧠 Quick Visual Memory Trick
Shape	                     Meaning
Diagonal	                 Random guessing
Slight curve	             Weak model
Strong curve to top-left	 Good model
Sharp corner	             Near perfect

Why might ROC curve sometimes be misleading in very imbalanced datasets (like disease detection)?

(Hint: Think about TN being huge)
ans- ROC can be misleading in imbalanced datasets because:

👉 ROC uses False Positive Rate (FPR)
👉 FPR depends on True Negatives (TN)

If TN is huge → FPR becomes very small
→ ROC curve may look good
→ Even if model is bad at detecting positives.

🧠 Simple Example

Imagine disease detection:

Type	Count
Healthy	99,000
Sick	1,000

If model:

Misses many sick people ❌

But predicts healthy people correctly ✔

ROC may still look good because TN is very large.

❗ Real Problem

ROC says:
👉 "Model is good"

But reality:
👉 Model is missing sick patients → dangerous.

⭐ One-Line Perfect Exam Answer

👉 ROC can be misleading in imbalanced datasets because large numbers of true negatives can make the false positive rate look small, even if the model performs poorly on the minority class.

💡 Extra (Very Smart Insight)
 
That’s why in imbalanced problems we prefer:

✔ Precision-Recall Curve
Instead of
❌ ROC Curve