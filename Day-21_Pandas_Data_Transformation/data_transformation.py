import pandas as pd

data = {
    "Name": ["ankush", "rahul", "priya"],
    "Age": [21, 22, 20],
    "Salary": [30000, 45000, 50000]
}

df = pd.DataFrame(data)
df["Name"] = df["Name"].str.title()
df["Salary"] = df["Salary"] * 1.1
df["Age_Group"] = df["Age"].apply(
    lambda x: "Adult" if x >= 21 else "Young"
)
print(df)

# Common Transformations

# 1. Rename Columns
df.rename(columns={"Salary": "Income"}, inplace=True)

# 2. Create New Column
df["Bonus"] = df["Salary"] * 0.1

# 3. Map Values
df["Gender"] = ["M", "F", "F"]
df["Gender"] = df["Gender"].map({
    "M": "Male",
    "F": "Female"
})

# 4. Apply Function
df["Salary"] = df["Salary"].apply(
    lambda x: x + 5000
)

# 5. Binning
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 18, 25, 60],
    labels=["Teen", "Young", "Adult"]
)