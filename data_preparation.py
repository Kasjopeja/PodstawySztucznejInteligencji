import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
train_data = pd.read_csv('data/train.csv')
test_data = pd.read_csv('data/test.csv')

print(train_data.head())  # Podgląd pierwszych 5 wierszy
print(train_data.info())  # Informacja o kolumnach i typach danych

print(train_data.describe())

print(train_data.isnull().sum())

sns.histplot(train_data['Age'].dropna(), kde=True, color='#6a62e3')
plt.title('Rozkład wieku pasażerów')
plt.show()

corr_matrix = train_data.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='Purples')
plt.title('Macierz korelacji')
plt.show()

