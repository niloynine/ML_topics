## 🚀 Day 22 — Handling Missing Data & Pipelines

### 🧠 Key Idea

Real-world data is messy. Missing values must be handled **before training**, otherwise models will fail.

---

### ⚠️ Problem: Missing Data

* Many datasets contain **NaN / None values**
* Models like Logistic Regression ❌ **cannot handle missing values**
* Leads to errors or incorrect learning

---

### 🛠️ Solution: Imputation

* Replace missing values with meaningful estimates

**Common strategies:**

* 📊 Mean → for numerical data
* 🔢 Median → for outliers
* 🔁 Most frequent → for categorical/binary data

---

### 🔗 Pipeline (Very Important)

A pipeline connects preprocessing and model training:

```text
Data → Imputer → Model
```

---

### ✅ Why Pipelines Matter

* 🔒 **Prevents Data Leakage**

  * Imputer learns only from **training data**
  * Test data remains unseen and fair

* 🔁 **Ensures Consistency**

  * Same preprocessing applied to:

    * Training data
    * Test data

* 🧹 **Cleaner Code**

  * Everything is organized in one workflow

* 📦 **Scalable**

  * Easy to extend (add scaling, encoding, etc.)

---

### 🚨 Common Mistake (I Learned)

❌ Filling missing values **before splitting data**

👉 This causes:

* Data leakage
* Unrealistic performance
* Biased evaluation

---

### ✅ Correct Workflow

```text
Split Data → Pipeline (Impute + Model) → Train → Evaluate
```

---

### 💡 Personal Insight

* Pipelines are not just for convenience
* They are **essential for correct ML practice**
* Without them, it’s easy to make hidden mistakes

---

### 🎯 Final Takeaway

> "Never preprocess using the full dataset — always use a pipeline after splitting."

---
