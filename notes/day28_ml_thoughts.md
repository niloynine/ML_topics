## 🚀 Day 28 — Hyperparameter Tuning (Improving Model Performance)

---

### 🧠 Key Idea

Hyperparameters are settings of a model that are **set before training** and control how the model learns. Proper tuning of these parameters can significantly improve performance.

---

### ⚙️ What Are Hyperparameters?

* Not learned from data ❌
* Set manually before training ✅

Examples:

* K in KNN
* max_depth in Decision Tree
* n_estimators in Random Forest
* λ (lambda) in regularization

---

### ⚠️ Problem with Defaults

```text
Default parameters → not optimal ❌
```

👉 Models may:

* Underperform
* Overfit or underfit

---

### ✅ Solution: Hyperparameter Tuning

```text
Try different values → choose the best combination
```

👉 Goal: improve model performance and generalization

---

### 🔍 Method 1 — Grid Search

* Tries **all possible combinations**
* Uses cross-validation

Example:

```text
(n_estimators, max_depth)
→ (10,5), (10,10), (50,5), (50,10)
```

✔ Accurate
❌ Can be slow

---

### ⚡ Method 2 — Random Search

* Tries **random combinations**
* Faster than grid search

✔ Efficient for large parameter spaces
❌ May miss best combination

---

### 🧠 Why Tuning Matters

```text
Better hyperparameters → better model performance
```

👉 Helps:

* Reduce overfitting
* Improve accuracy
* Find optimal model behavior

---

### ⚖️ Connection to Bias-Variance

* Too complex → overfitting
* Too simple → underfitting

👉 Tuning helps find the **balance**

---

### 🚨 Common Mistakes

* Using default parameters blindly
* Not using cross-validation during tuning
* Tuning without understanding the model

---

### 💡 Personal Insight

* Small parameter changes can make a big difference
* Tuning is essential for real-world ML systems
* Always combine tuning with cross-validation

---

### 🎯 Final Takeaway

> "Hyperparameter tuning is the key to unlocking a model’s full potential."

---
 