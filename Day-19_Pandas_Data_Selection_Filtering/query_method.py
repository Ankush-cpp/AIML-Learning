import pandas as pd

data = {
    "Name": ["Ankush", "Rahul", "Priya", "Aman", "Neha"],
    "Age": [21, 22, 20, 23, 19],
    "Rating": [4.5, 3.8, 4.9, 2.9, 4.2]
}

df = pd.DataFrame(data)

print(df.query("Age > 20"))

print(df.query("Rating > 4"))

print(df.query("Age > 20 and Rating > 4"))

print(df.query("Name == 'Ankush'"))