import pandas as pd

data = {
    "name": ["ankush", "rahul", "priya"],
    "age": [21, 22, 20],
    "salary": [30000, 45000, 50000]
}

df = pd.DataFrame(data)

# Rename column
df = df.rename(columns={"salary": "income"})

# Create new column
df["bonus"] = df["income"] * 0.1

# Apply function
df["income"] = df["income"].apply(lambda x: x + 5000)

# Map values
df["status"] = df["age"].map({
    20: "Student",
    21: "Graduate",
    22: "Professional"
})

# Change datatype
df["age"] = df["age"].astype(float)

# Insert new column
df.insert(1, "city", ["Bhopal", "Indore", "Delhi"])

# Sort values
df = df.sort_values(by="income", ascending=False)

# Set index
df = df.set_index("name")
print(df)

# Reset index
df = df.reset_index()
print(df)