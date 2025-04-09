import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
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

grid_parameters = {
    "max_depth":[None,3,5,7,10],
    "criterion":["gini","entropy"],
    "min_samples_split":[2,5,10],
    "min_samples_leaf":[1,2,4]
}

dt_model = DecisionTreeClassifier(random_state=42)
grid_search = GridSearchCV(dt_model, grid_parameters, cv=5, scoring="accuracy", n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)
print(f"Najlepszy wynik w walidacji krzyżowej: {grid_search.best_params_}")
print(f"Najlepszy wynik (accuracy) w walidacji krzyżowej: {grid_search.best_score_}")

best_dt = grid_search.best_estimator_

#Ocena modelu
y_val_pred = best_dt.predict(X_val)
accuracy = accuracy_score(y_val, y_val_pred)
print(f"Accuracy na zbiorze walidacyjnym: {accuracy:.4f}")

print("Macierz konfuzji:")
print(confusion_matrix(y_val, y_val_pred))
print("\nRaport klasyfikacji:")
print(classification_report(y_val, y_val_pred))

# Predykcja na zbiorze testowym
passenger_ids = test_df["PassengerId"]
X_test = test_df.drop("PassengerId", axis=1)

y_test_pred = best_dt.predict(X_test)


submission = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": y_test_pred
})
submission.to_csv("data/submission_decision_tree_optimized.csv", index=False)
print("\nPlik submission_decision_tree_optimized.csv z predykcjami został zapisany w folderze 'data'.")

# Zapisanie modelu do pliku
joblib.dump(best_dt, "models/decision_tree_model_optimized.pkl")
print("Model zapisany jako 'decision_tree_model_optimized.pkl'")
