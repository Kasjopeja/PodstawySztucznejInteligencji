import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Wczytanie danych
train_df = pd.read_csv("data/train_clean.csv")
test_df = pd.read_csv("data/test_clean.csv")

# Przygotowanie cech (X) i etykiet (y)
y = train_df["Survived"]
X = train_df.drop(["Survived", "PassengerId"], axis=1)

# Podział danych na zbiór treningowy i walidacyjny
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Definicja przestrzeni parametrów do optymalizacji
param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [None, 5, 10, 15],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

# Inicjalizacja klasyfikatora Random Forest
rf = RandomForestClassifier(random_state=42)

# Użycie GridSearchCV z 5-krotną walidacją krzyżową
grid_search = GridSearchCV(
    rf,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train, y_train)

# Wyświetlenie najlepszych parametrów i wyniku
print("Najlepsze parametry:")
print(grid_search.best_params_)
print("Najlepszy wynik (accuracy) w walidacji krzyżowej: {:.4f}".format(grid_search.best_score_))

# Przypisanie optymalnego modelu
best_rf = grid_search.best_estimator_

# Ocena modelu na zbiorze walidacyjnym
y_val_pred = best_rf.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f"Accuracy na zbiorze walidacyjnym: {val_accuracy:.4f}")
print("Macierz konfuzji:")
print(confusion_matrix(y_val, y_val_pred))
print("\nRaport klasyfikacji:")
print(classification_report(y_val, y_val_pred))

# Predykcja na zbiorze testowym
passenger_ids = test_df["PassengerId"]
X_test = test_df.drop("PassengerId", axis=1)
y_test_pred = best_rf.predict(X_test)

# Zapis wyników do pliku CSV (format Kaggle)
submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": y_test_pred
})
submission.to_csv("data/submission_random_forest_optimized.csv", index=False)
print("\nPlik submission_random_forest_optimized.csv został zapisany w folderze 'data'.")

# Zapisanie optymalizowanego modelu do pliku
joblib.dump(best_rf, "models/optimized_random_forest_model.pkl")
print("Optymalizowany model został zapisany jako 'optimized_random_forest_model.pkl'.")