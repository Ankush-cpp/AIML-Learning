import pandas as pd

data = {
    "Name": ["Ankush", "Rahul", "Priya"],
    "Age": [21, 22, 20],
    "Rating": [4.5, 3.8, 4.9]
}

df = pd.DataFrame(data)

print(df)

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.index)

print(df["Name"])

print(df.loc[0])

print(df[["Name", "Rating"]])

print(df.describe())

print(df[df["Rating"] > 4])

print(df.sort_values(by="Rating", ascending=False))