## 🚀 Day 23 — Feature Scaling (Normalization & Standardization)

---

### 🧠 Key Idea

Different features can have different ranges, which can **bias machine learning models**. Feature scaling ensures that all features contribute fairly during training.

---

### ⚠️ Problem: Different Feature Scales

Example:

* age = 50
* fever = 1

👉 Model may assume **age is more important** just because it has a larger value ❌

---

### ✅ Solution: Feature Scaling

Bring all features to a **similar range**

---

### 🔧 Types of Scaling

#### 1️⃣ Standardization (Most Common)

```text
z = (x - mean) / std
```

* Mean = 0
* Standard deviation = 1
* ✔ Best for Logistic Regression, SVM

---

#### 2️⃣ Normalization (Min-Max Scaling)

```text
x = (x - min) / (max - min)
```

* Range: 0 to 1
* ✔ Useful for KNN, Neural Networks

---

### 🔗 Pipeline Integration

Correct pipeline:

```text
Data → Imputer → Scaler → Model
```

Example:

* Fill missing values
* Scale features
* Train model

---

### 🔒 Important Rules

* ❌ Never scale before splitting data → causes **data leakage**
* ✅ Always scale inside a **pipeline after splitting**
* 🔁 Same scaler must be applied to both train and test data

---

### 🤖 Models That Need Scaling

✔ Logistic Regression
✔ KNN
✔ SVM

---

### ❌ Models That Do NOT Need Scaling

* Decision Trees
* Random Forest

👉 Because they rely on **splits, not distances**

---

### 🚨 Common Mistake (I Learned)

* Not scaling features → model gives **wrong importance**
* Leads to:

  * Poor performance
  * Biased learning
  * Slow convergence

---

### 💡 Personal Insight

* Scaling is not optional for many models
* It directly affects **model quality and learning behavior**
* Pipelines ensure scaling is done correctly and safely

---

### 🎯 Final Takeaway

> "Always scale features for distance/weight-based models, and do it inside a pipeline after splitting."

---
