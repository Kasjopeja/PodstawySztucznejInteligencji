# Zbiór danych

Wykorzystujemy zbiór danych znajdujący się na Kaggla.

https://www.kaggle.com/c/titanic/

Zbiór ten zawiera informacje o pasażerach statku Titanic i służy do budowy modelu klasyfikacyjnego, którego celem jest przewidywanie, kto przeżył katastrofę.


| Zmienna  | Definicja                                      | Opis                                           |
|----------|------------------------------------------------|------------------------------------------------|
| survival | czy przetrwali                                 | 0 = zgineli, 1 = przeżyli                      |
| pclass   | klasa biletu                                   | 1 = pierwsza, 2 = druga, 3 = trzecia           |
| sex      | płeć                                           |                                                |
| age      | wiek w latach                                  |                                                |
| sibsp    | liczba rodzeństwa i/lub małżonków na pokładzie |                                                |
| parch    | liczba rodziców i/lub dzieci na pokładzie      |                                                |
| ticket   | numer biletu                                   |                                                |
| fare     | opłata za bilet pasażera                       |                                                |
| cabin    | numer kabiny                                   |                                                |
| embarked | port startowy                                  | C = Cherbourg, Q = Queenstown, S = Southampton |


## Wstępna analiza danych

---

Najpierw przygotowaliśmy dane do czyszczenia robiąc ich wstępną analizę.


Na potrzeby czyszczenia danych najpierw wykonano ich eksplorację. Zbiór zawiera informacje o **891 pasażerach** i **12 zmiennych**.

![Zrzut ekranu 2025-04-08 224441.png](../images/Zrzut%20ekranu%202025-04-08%20224441.png)
![Zrzut ekranu 2025-04-08 224514.png](../images/Zrzut%20ekranu%202025-04-08%20224514.png)

Analiza braków danych wykazała:
- **177 brakujących wartości** w kolumnie `Age` (wiek),
- **687 braków w `Cabin`**, co stanowi ponad 77% danych – kolumnę zdecydowano się usunąć,
- **2 braki w `Embarked`** – możliwe do uzupełnienia.

![Zrzut ekranu 2025-04-08 224524.png](../images/Zrzut%20ekranu%202025-04-08%20224524.png)

Wiek pasażerów ma **asymetryczny rozkład prawostronny** – najwięcej osób znajduje się w przedziale 20–30 lat. Widoczna jest również grupa małych dzieci.
![Zrzut ekranu 2025-04-08 224544.png](../images/Zrzut%20ekranu%202025-04-08%20224544.png)


W macierzy korelacji zauważono kilka interesujących zależności:

- `Pclass` jest **negatywnie skorelowany z przeżyciem** (`Survived` ≈ -0.34), co sugeruje, że pasażerowie z wyższych klas mieli większe szanse na przeżycie.
- `Fare` wykazuje **dodatnią korelację z przeżyciem** (~0.26), co może być związane z klasą podróży.
- `SibSp` i `Parch` są umiarkowanie skorelowane (0.41), co może świadczyć o podróżujących rodzinach.

![Zrzut ekranu 2025-04-08 224551.png](../images/Zrzut%20ekranu%202025-04-08%20224551.png)

## Czyszczenie danych

---

Proces czyszczenia danych obejmował następujące kroki:

**Uzupełnianie braków:**
   - `Fare`: brakujące wartości zastąpiono **medianą** (ma ona znacznie mniejsze odchylenie niż średnia).
   - `Age`: uzupełniono medianą, ponieważ rozkład wieku był skośny.
   - `Embarked`: wypełniono najczęściej występującą wartością (`S` – Southampton).


**Kodowanie zmiennych kategorycznych:**
   - `Sex`: zakodowano jako `0` dla `female` i `1` dla `male`.
   - `Embarked`: zakodowano jako:
     - `S` → 0
     - `C` → 1
     - `Q` → 2

**Usunięcie nieprzydatnych kolumn:**
   - `Cabin`: ze względu na dużą liczbę braków,
   - `Name` i `Ticket`: nie zawierały informacji istotnych dla modelowania i nie były w formacie numerycznym.    

Sprawdzono, czy wszystkie brakujące wartości zostały poprawnie uzupełnione.Dane zostały zapisane do nowych plików: `train_clean.csv` oraz `test_clean.csv`.

![Zrzut ekranu 2025-04-08 224252.png](../images/Zrzut%20ekranu%202025-04-08%20224252.png)