import pandas as pd

data = {
    "Name": ["Ankush", "Rahul", "Priya", "Aman", "Neha"],
    "Age": [21, 22, 20, 23, 19],
    "Rating": [4.5, 3.8, 4.9, 2.9, 4.2]
}

df = pd.DataFrame(data)

print(df[df["Rating"] > 4])

print(df[df["Age"] > 20])

print(df[(df["Age"] > 20) & (df["Rating"] > 4)])

print(df[(df["Age"] < 22) | (df["Rating"] > 4.5)])

print(df[df["Name"] == "Ankush"])