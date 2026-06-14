import pandas as pd
import numpy as np

data = {
    "Name": ["Ankush", "Rahul", None, "Priya"],
    "Age": [21, np.nan, 22, 20]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())

print(df.isnull().sum())

print(df.dropna())

print(df.fillna("Unknown"))