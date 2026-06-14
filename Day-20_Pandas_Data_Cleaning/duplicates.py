import pandas as pd

data = {
    "Name": ["Ankush", "Rahul", "Rahul", "Priya"],
    "Age": [21, 22, 22, 20]
}

df = pd.DataFrame(data)

print(df)

print(df.duplicated())

print(df.drop_duplicates())