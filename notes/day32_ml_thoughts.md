
---

# 📄 `day32_random_forest.md`

```markdown
# 📅 Day 32 — Random Forest (Bagging)

## 🌳 What is Random Forest?

Random Forest is an ensemble learning algorithm that combines multiple Decision Trees.

Final prediction = Majority vote of all trees

---

## 🧠 How it works

1. Takes random samples of data (bagging)
2. Builds multiple decision trees
3. Each tree uses random features
4. Combines predictions

---

## 🎯 Why Random Forest?

- Reduces overfitting
- More accurate than a single decision tree
- Works well on most datasets
- Handles non-linear data

---

## 💻 Implementation

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/dataset.csv")

X = df.drop("disease", axis=1)
y = df["disease"]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf = RandomForestClassifier(n_estimators=200, random_state=42)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print("Random Forest Accuracy:", accuracy_score(y_test, y_pred))