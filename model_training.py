import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#Wczytanie wyczyszczonych danych
train_df = pd.read_csv("data/train_clean.csv")
test_df = pd.read_csv("data/test_clean.csv")


#Przygotowanie cech (x) i etykiet (y)
y = train_df["Survived"]
X = train_df.drop(["Survived", "PassengerId"], axis=1)

#train/test split
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#Regresja Logistyczna
model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train, y_train)

#Ocena modelu
y_val_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_val_pred)
print(f"Accuracy na zbiorze walidacyjnym: {accuracy:.4f}")

print("Macierz konfuzji:")
print(confusion_matrix(y_val, y_val_pred))
print("\nRaport klasyfikacji:")
print(classification_report(y_val, y_val_pred))

#Predykcja na zbiorze testowym
passenger_ids = test_df["PassengerId"]
X_test = test_df.drop("PassengerId", axis=1)

y_test_pred = model.predict(X_test)

#Zapis wyników
submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": y_test_pred
})

submission.to_csv("data/submission.csv", index=False)

