# 📅 Day 31 — Ensemble Learning

## 🧠 What is Ensemble Learning?

Ensemble Learning is a technique where multiple machine learning models are combined to improve overall performance.

Instead of relying on a single model:
Weak Models → Combined → Strong Model

---

## 🎯 Why use Ensemble Learning?

- Improves accuracy
- Reduces overfitting
- More stable predictions
- Widely used in real-world applications

---

## 🔥 Types of Ensemble Methods

### 1. Voting
- Multiple models predict
- Final output = majority vote (classification)

### 2. Averaging
- Used in regression
- Final output = average of predictions

### 3. Bagging (Bootstrap Aggregation)
- Models trained independently on random subsets of data
- Example: Random Forest

### 4. Boosting
- Models trained sequentially
- Each model learns from previous errors
- Example: AdaBoost, Gradient Boosting

---

## 💻 Implementation — Voting Classifier

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model1 = LogisticRegression(max_iter=200)
model2 = DecisionTreeClassifier()
model3 = KNeighborsClassifier()

voting_model = VotingClassifier(
    estimators=[
        ('lr', model1),
        ('dt', model2),
        ('knn', model3)
    ],
    voting='hard'
)

voting_model.fit(X_train, y_train)

y_pred = voting_model.predict(X_test)

print("Ensemble Accuracy:", accuracy_score(y_test, y_pred))