import pandas as pd

data = {
    "Age": ["21", "22", "20"]
}

df = pd.DataFrame(data)
print(df.dtypes)

df["Age"] = df["Age"].astype(int)
print(df.dtypes)