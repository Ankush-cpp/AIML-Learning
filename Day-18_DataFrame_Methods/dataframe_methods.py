import pandas as pd

data = {
    "Name": ["Ankush", "Rahul", "Priya", "Aman"],
    "Age": [21, 22, 20, 23],
    "Rating": [4.5, 3.8, 4.9, 2.9]
}

df = pd.DataFrame(data)

print(df.head())

print(df.tail())

print(df.info())

print(df.describe())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.isnull().sum())

print(df["Rating"].mean())

print(df["Rating"].max())

print(df["Rating"].min())

print(df.sort_values(by="Rating", ascending=False))

print(df["Age"].value_counts())