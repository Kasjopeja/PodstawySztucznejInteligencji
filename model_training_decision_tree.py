import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

train_df = pd.read_csv("data/train_clean.csv")
test_df = pd.read_csv("data/test_clean.csv")

# Przygotowanie cech (x) i etykiet (y)
y = train_df["Survived"]
X = train_df.drop(["Survived", "PassengerId"], axis=1)

# train/test split
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

#Ocena modelu
y_val_pred = dt_model.predict(X_val)
accuracy = accuracy_score(y_val, y_val_pred)
print(f"Accuracy na zbiorze walidacyjnym: {accuracy:.4f}")

print("Macierz konfuzji:")
print(confusion_matrix(y_val, y_val_pred))
print("\nRaport klasyfikacji:")
print(classification_report(y_val, y_val_pred))

# Predykcja na zbiorze testowym
passenger_ids = test_df["PassengerId"]
X_test = test_df.drop("PassengerId", axis=1)

y_test_pred = dt_model.predict(X_test)


submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": y_test_pred
})
submission.to_csv("data/submission_decision_tree.csv", index=False)
print("\nPlik submission_decision_tree.csv z predykcjami został zapisany w folderze 'data'.")

# Zapisanie modelu do pliku
joblib.dump(dt_model, "models/decision_tree_model.pkl")
print("Model zapisany jako 'decision_tree_model.pkl'")
