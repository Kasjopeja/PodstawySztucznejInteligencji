# Modele

## Model Regresji Logistycznej

![Zrzut ekranu 2025-04-03 214 441.png](image s/Zrzut%20ekranu%202025-04-03%20214441.png)

Accuracy mówi nam, jak często model trafia z przewidywaniami w stosunku do wszystkich przykładów. U nas to 80%, więc spoko.

![Zrzut ekranu 2025-04-03 214913.png](images/Zrzut%20ekranu%202025-04-03%20214913.png)

Wiersz 1 (0, nie przeżył):

98 → True Negatives (poprawnie przewidziani jako nie przeżył)

12 → False Positives (model błędnie przewidział, że przeżyli)

Wiersz 2 (1, przeżył):

22 → False Negatives (model błędnie przewidział, że nie przeżyli)

47 → True Positives (poprawnie przewidziani jako przeżył)

![Zrzut ekranu 2025-04-03 215339.png](images/Zrzut%20ekranu%202025-04-03%20215339.png)

**Precision -** ile osób, które przeżyły (1) jest faktycznie pozytywna

**Recall  -** ile osób, które przeżyły (1) zostało wykryte przez model jako 1

**F1-score -** średnia harmoniczna precyzji i czułości

**Support -** pokazuje ile było przypadków śmierci (0) i przeżycia (1) w zbiorze walidyacyjnym

My mamy 81% pewności, gdy mówimy, że pasażer umarł (0) i 89% osób, które zgineły są poprawnie wykryte. A gdy ktoś przezył to mamy 79% pewności, ale tylko 67% osób, które faktycznie przezyły sa poprawnie wykryte.
A f1-score mamy 0.85/0.72, więc jest całkiem spoko kompromis między precyzją a czułością.

![Zrzut ekranu 2025-04-03 215343.png](images/Zrzut%20ekranu%202025-04-03%20215343.png)

**Accuracy -** jak często model trafia z przewidywaniem w stosunku do wszystkich przypadków

**Macro avg -** mówi, jak model radzi sobie średnio w obu klasach, nawet jak jedna jest liczniejsza

**Weighted avg  -** daje ogólną ocenę, biorąc pod uwagę, że klasy mogą być niezbalansowane.

U nas mamy dokładnośc 80%, więc spoko. Macro avg (0.80, 0.78, 0.79) oraz weighted avg (0.80, 0.80, 0.80) pokazują, że skuteczność jest dość zrównoważona między obiema klasami.

## Model drzewa decyzyjnego

![Zrzut ekranu 2025-04-04 111018.png](images/Zrzut%20ekranu%202025-04-04%20111018.png)

W drzewie decyzyjnym wyszło nam 82% przypadków, co nie jest dużą różnicą w porównaniu do regresii, ale jednak wychodzi lepiej

![Zrzut ekranu 2025-04-04 111022.png](images/Zrzut%20ekranu%202025-04-04%20111022.png)

Wiersz 1 (0, nie przeżył):

97 → True Negatives (poprawnie przewidziani jako nie przeżył)

13 → False Positives (model błędnie przewidział, że przeżyli)

Wiersz 2 (1, przeżył):

19 → False Negatives (model błędnie przewidział, że nie przeżyli)

50 → True Positives (poprawnie przewidziani jako przeżył)

![Zrzut ekranu 2025-04-04 111028.png](images/Zrzut%20ekranu%202025-04-04%20111028.png)

Tu zaś mamy 84% pewności, żę pasażer nie żyje jak mówimy, że umarł (xD). Z czego 88% zostało poprawnie zaklasyfikowane.
Z przeżył mamy 79% proces pewności i 72% jest zaklasyfikowana poprawnie. Więc ogólnie pewność mamy tą samą co przy regresji, ale poprawnych rozpoznań jest więcej.

Po f1-score widzimy, że model jesy dokładniejszy dla 0.

I jak porównamy z regresją to _support_ jest identyczny.

![Zrzut ekranu 2025-04-04 111033.png](images/Zrzut%20ekranu%202025-04-04%20111033.png)

Średnia „macro” traktuje obie klasy z równą wagą, co podkreśla lekko niższe wyniki dla przeżycia. Średnia ważona uwzględnia liczebność klas i finalnie daje podobny wynik do accuracy, czyli ok. 82%.

## Model lasu losowego

![Zrzut ekranu 2025-04-08 131835.png](images/Zrzut%20ekranu%202025-04-08%20131835.png)

W przypadku lasu losowego dokładność to 82%, więc podobnie jak drzewo decyzyjne, trochę lepiej niż regresja.

![Zrzut ekranu 2025-04-08 131839.png](images/Zrzut%20ekranu%202025-04-08%20131839.png)

Wiersz 1 (0, nie przeżył):

97 → True Negatives (model poprawnie przewidział brak przeżycia)

13 → False Positives (model błędnie przewidział przeżycie)

Wiersz 2 (1, przeżył):

18 → False Negatives (model błędnie przewidział brak przeżycia)

51 → True Positives (model poprawnie przewidział przeżycie)

![Zrzut ekranu 2025-04-08 131844.png](images/Zrzut%20ekranu%202025-04-08%20131844.png)

Gdy model mówi, że ktoś nie przeżył to ma 84% racji i wykrywa 88% tych, którzy faktycznie nie przeżyli. 
Zaś jak przezył to mamy 80% pewności i wykrywa 74% przypadków.

Po F1-score widać, ze śmierci są dokładniejsze.

Support jest identyczny: 110 przypadków śmierci i 69 przeżyć.

![Zrzut ekranu 2025-04-08 131848.png](images/Zrzut%20ekranu%202025-04-08%20131848.png)

Wszystkie trzy metryki wynoszą 0.82, podobnie jak accuracy, więc model jest dość zbalansowany.

| Porównanie    | Regresja | Drzewo decyzjne | Las Losowy      |
|---------------| ---- | ----------- |-----------------|
| Accuracy      | 80%  | 82%         | 82%             |
| Precision (0) | 82%  | 84%         | 84%             |
| Recall (0)    | 89%  | 88%         | 88%             |
| F1 (0)        | 0,85 | 0,86        | 0,86            |
| Precision (1) | 80%  | 79%         | 79%             |
| Recall (1)    | 68%  | 72%         | 72%             |
| F1 (1)        | 73%  | 76%         | 76%             |
|               |    Model zakłada liniowe zależności, dobry przy mniejszych zbiorach  | Łatwiejsze do interpretacji (możliwość wizualizacji drzewa), ale może być podatne na overfitting |Stabilny i dokładny model, dobrze radzi sobie z generalizacją dzięki łączeniu wielu drzew; mniej podatny na overfitting niż pojedyncze drzewo, ale trudniejszy do interpretacji.|

