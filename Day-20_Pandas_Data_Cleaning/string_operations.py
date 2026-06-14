import pandas as pd

data = {
    "Name": [" ankush ", "RAHUL", "Priya"]
}

df = pd.DataFrame(data)

print(df["Name"].str.strip())

print(df["Name"].str.lower())

print(df["Name"].str.upper())

print(df["Name"].str.title())