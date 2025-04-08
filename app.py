from fastapi import FastAPI, Request
import joblib
import pandas as pd
import uvicorn

# Wczytanie modeli
modelDT = joblib.load("models/decision_tree_model.pkl")
modelR = joblib.load("models/model_training_regression.pkl")
modelRF = joblib.load("models/model_training_random_forest.pkl")

# Domyślne dane (zakodowane dane testowe – przyjmujemy odpowiedni format)
default_input = pd.read_csv("data/test_clean.csv")
default_input = default_input.drop("PassengerId", axis=1)

app = FastAPI()


# Endpoint do predykcji
@app.post("/predict")
async def predict(request: Request):
    body = await request.json()

    # Pobranie modelu (lub wszystkich jeśli nie podano)
    model_choice = body.get("model")  # "decision_tree", "regression", "random_forest"

    # Pobranie danych (jeśli podano)
    input_data = body.get("data")  # lista słowników [{...}, {...}] lub None
    if input_data:
        input_df = pd.DataFrame(input_data)
    else:
        input_df = default_input.copy()

    predictions = {}

    # Wybór modelu lub użycie wszystkich
    if model_choice == "decision_tree":
        predictions["decision_tree"] = modelDT.predict(input_df).tolist()
    elif model_choice == "regression":
        predictions["regression"] = modelR.predict(input_df).tolist()
    elif model_choice == "random_forest":
        predictions["random_forest"] = modelRF.predict(input_df).tolist()
    else:
        # Jeśli nie podano modelu – użyj wszystkich
        predictions["decision_tree"] = modelDT.predict(input_df).tolist()
        predictions["regression"] = modelR.predict(input_df).tolist()
        predictions["random_forest"] = modelRF.predict(input_df).tolist()

    return {
        "predictions": predictions,
        "used_models": list(predictions.keys()),
        "rows_predicted": len(input_df)
    }


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
