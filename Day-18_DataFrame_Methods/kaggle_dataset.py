import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df["Survived"].value_counts())