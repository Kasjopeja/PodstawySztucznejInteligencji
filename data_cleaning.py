import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych
train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

# Uzupełnienie braków w kolumnie Fare w test_df
test_df['Fare'] = test_df['Fare'].fillna(test_df['Fare'].median())

# Uzupełnienie braków w 'Age' medianą
train_df['Age'].fillna(train_df['Age'].median(), inplace=True)
test_df['Age'].fillna(test_df['Age'].median(), inplace=True)

# Uzupełnienie braków w 'Embarked' najczęściej występującą wartością (trybem)
most_common_embarked = train_df['Embarked'].mode()[0]
train_df['Embarked'] = train_df['Embarked'].fillna(most_common_embarked)


if test_df['Embarked'].isnull().sum() > 0:
    test_df['Embarked'].fillna(most_common_embarked, inplace=True)

# Usunięcie kolumny 'Cabin'
if 'Cabin' in train_df.columns:
    train_df.drop('Cabin', axis=1, inplace=True)
if 'Cabin' in test_df.columns:
    test_df.drop('Cabin', axis=1, inplace=True)

# Krótka weryfikacja braków
print("\n=== Braki danych w Train (po uzupełnieniu) ===")
print(train_df.isnull().sum())
print("\n=== Braki danych w Test (po uzupełnieniu) ===")
print(test_df.isnull().sum())


# Zapisanie przetworzonych danych do nowych plików
train_df.to_csv("data/train_clean.csv", index=False)
test_df.to_csv("data/test_clean.csv", index=False)
print("\nPliki train_clean.csv i test_clean.csv zostały zapisane w folderze 'data'.")
