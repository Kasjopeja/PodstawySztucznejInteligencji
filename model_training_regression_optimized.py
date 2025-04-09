import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Wczytanie danych
train_df = pd.read_csv("data/train_clean.csv")
test_df = pd.read_csv("data/test_clean.csv")

# Przygotowanie cech (X) i etykiet (y)
y = train_df["Survived"]
X = train_df.drop(["Survived", "PassengerId"], axis=1)

# Podział danych
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Definicja przestrzeni hiperparametrów
param_grid = {
    "C": [0.01, 0.1, 1, 10, 100],
    "penalty": ["l2"],
    "solver": ["liblinear", "lbfgs"],
}

# Inicjalizacja regresji logistycznej
lr = LogisticRegression(max_iter=500, random_state=42)

# GridSearchCV (z 5-krotną walidacją)
grid_search = GridSearchCV(
    lr,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)

# Wyniki
print("Najlepsze parametry dla regresji logistycznej:")
print(grid_search.best_params_)
print("Najlepszy wynik (accuracy) w walidacji krzyżowej: {:.4f}".format(grid_search.best_score_))

best_lr = grid_search.best_estimator_

# Ocena na zbiorze walidacyjnym
y_val_pred = best_lr.predict(X_val)
print(f"\nAccuracy na zbiorze walidacyjnym: {accuracy_score(y_val, y_val_pred):.4f}")
print("Macierz konfuzji:")
print(confusion_matrix(y_val, y_val_pred))
print("\nRaport klasyfikacji:")
print(classification_report(y_val, y_val_pred))

# Predykcja na zbiorze testowym
passenger_ids = test_df["PassengerId"]
X_test = test_df.drop("PassengerId", axis=1)
y_test_pred = best_lr.predict(X_test)

# Zapis wyników
submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": y_test_pred
})
submission.to_csv("data/submission_regression_optimized.csv", index=False)
print("\nPlik submission_regression_optimized.csv został zapisany w folderze 'data'.")

# Zapisanie optymalizowanego modelu
joblib.dump(best_lr, "models/optimized_regression_model.pkl")
print("Optymalizowany model regresji logistycznej został zapisany jako 'optimized_regression_model.pkl'.")