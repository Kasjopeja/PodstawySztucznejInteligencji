# Wykorzystanie modele uczenia maszynowego


W ramach analizy danych o pasażerach Titanica zbudowano i przetestowano trzy różne modele klasyfikacyjne: **Regresję Logistyczną**, **Drzewo Decyzyjne** oraz **Las Losowy (Random Forest)**. Każdy z modeli został oceniony na podstawie dokładności (accuracy) na zbiorze walidacyjnym oraz wygenerował osobne predykcje dla zbioru testowego.

Dane zostały podzielone na zbiór treningowy i walidacyjny w proporcji 80/20.

## Regresja Logistyczna

---

Regresja logistyczna to klasyczny model liniowy, który sprawdza się dobrze przy problemach binarnych – takich jak przewidywanie przeżycia (`Survived`). Działa szybko i dobrze interpretuje wpływ poszczególnych cech.

- **Zalety**:
  - prostota i szybkość trenowania,
  - dobra interpretowalność,
  - dobrze działa przy niezbyt złożonych danych.
- **Dlaczego wybrano**:  
  Stanowi silną linię bazową – pozwala ocenić, czy bardziej złożone modele rzeczywiście wnoszą poprawę jakości predykcji.

## Drzewo Decyzyjne 

---

Drzewa decyzyjne to modele strukturalne, które uczą się reguł decyzyjnych poprzez podziały danych. Są łatwe do wizualizacji i interpretacji.

- **Zalety**:
  - przejrzysta struktura,
  - możliwość pracy z danymi nieliniowymi,
  - nie wymagają standaryzacji cech.
- **Dlaczego wybrano**:  
  Model pozwala sprawdzić, czy dane zawierają struktury decyzyjne, które można łatwo wydzielić prostymi regułami. Może być też punktem wyjścia do budowy bardziej zaawansowanego modelu ensemble.

## Las Losowy

---

Random Forest to metoda zespołowa (ensemble), która buduje wiele drzew decyzyjnych i agreguje ich wyniki, co zwykle poprawia stabilność i dokładność.

- **Zalety**:
  - wysoka skuteczność,
  - odporność na przeuczenie (overfitting),
  - dobrze radzi sobie z danymi o mieszanym typie.
- **Dlaczego wybrano**:  
  Model często osiąga jedne z najlepszych wyników w zadaniach klasyfikacyjnych na średnich i dużych zbiorach danych. Jest bardziej odporny na błędy pojedynczych drzew.

