# Wdrożenie modeli

Modele zostały wyeksportowane do plików <code> .pkl </code> i wykorzystane do utworzenia api.

Aby skorzystać z funkcjonalności należy uruchomić aplikacje (plik app) i wysłać http request z pomocą wybranego narzędzia na ardes http://127.0.0.1:8000/predict

## Dane domyślne 

Konfiguracja domyślna wykorzystuje dane testowe do przetestowania wszystkich trzech modelów i aby ją uruchomić należy wysłać metodą <code> POST</code> pustą zawartość <code> JSON </code>

## Dane urzytkownika

Podając jako zawartość <code> JSON</code> dane pasażera oraz medote którą chcemy wykorzystać możemy wykorzystać model do wykonania predykcji z wykorzystaniem własnych danych

przykladowe zapytanie:

    POST http://127.0.0.1:8000/predict
    Content-Type: application/json
    
    {
      "model": "random_forest",
      "data": [
        {
          "Pclass": 1,
          "Sex": 0,
          "Age": 38.0,
          "SibSp": 1,
          "Parch": 0,
          "Fare": 71.2833,
          "Embarked": 0
        }
      ]
    }