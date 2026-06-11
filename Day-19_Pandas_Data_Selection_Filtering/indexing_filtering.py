import pandas as pd

data = {
    "Name": ["Ankush", "Rahul", "Priya", "Aman", "Neha"],
    "Age": [21, 22, 20, 23, 19],
    "Rating": [4.5, 3.8, 4.9, 2.9, 4.2]
}

df = pd.DataFrame(data)

print(df)

print(df["Name"])

print(df[["Name", "Rating"]])

print(df.loc[0])

print(df.loc[1:3])

print(df.iloc[0])

print(df.iloc[0:3])

print(df.iloc[:, 0])

print(df.iloc[:, 1:3])