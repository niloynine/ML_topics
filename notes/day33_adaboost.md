# 📅 Day 33 — AdaBoost (Adaptive Boosting)

## 🧠 Overview

Today I learned **Boosting**, another important Ensemble Learning technique.

Unlike Random Forest (Bagging), where multiple models train independently in parallel, Boosting trains models sequentially.

Each new model tries to correct the mistakes made by previous models.

---

# Bagging vs Boosting

| Bagging                    | Boosting                      |
| -------------------------- | ----------------------------- |
| Models train independently | Models train sequentially     |
| Reduces variance           | Reduces bias                  |
| Uses parallel learning     | Learns from previous mistakes |
| Example: Random Forest     | Example: AdaBoost             |

---

# What is AdaBoost?

AdaBoost stands for **Adaptive Boosting**.

It combines multiple weak learners (usually small decision trees called stumps) to create a stronger model.

### Process:

1. Train first weak learner
2. Identify incorrect predictions
3. Give more importance to incorrect samples
4. Train next learner
5. Repeat until performance improves

---

# Dataset Loading

```python
import pandas as pd

df = pd.read_csv("data/dataset.csv")

print(df.head())
```

---

# Label Encoding

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['disease'] = le.fit_transform(df['disease'])
```

### Why?

Machine learning models cannot work with text labels directly.

Example:

* Flu → 0
* Cold → 1
* Diabetes → 2

---

# Feature and Target Split

```python
X = df.drop("disease", axis=1)
y = df["disease"]
```

* `X` → symptoms/features
* `y` → disease output

---

# Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

# Training AdaBoost

```python
from sklearn.ensemble import AdaBoostClassifier

ada = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)

ada.fit(X_train, y_train)
```

---

# Prediction

```python
y_pred = ada.predict(X_test)
```

---

# Accuracy Evaluation

```python
from sklearn.metrics import accuracy_score

print("AdaBoost Accuracy:", accuracy_score(y_test, y_pred))
```

---

# Comparison with Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))
```

---

# Observations

* AdaBoost learns sequentially
* Focuses on correcting mistakes
* Works well on structured datasets
* Performance depends on dataset quality

---

# Challenges Faced

* Understanding difference between bagging and boosting
* Learning how weak learners improve over time

---

# Key Takeaways

✅ Learned Boosting concept
✅ Implemented AdaBoost
✅ Compared AdaBoost with Random Forest
✅ Applied model on medical dataset


