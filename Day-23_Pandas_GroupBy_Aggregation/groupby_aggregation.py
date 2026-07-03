import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Sales", "Sales"],
    "Employee": ["Ankush", "Rahul", "Priya", "Neha", "Aman", "Riya"],
    "Salary": [50000, 40000, 55000, 42000, 38000, 45000],
    "Experience": [2, 3, 4, 2, 1, 5]
}
df = pd.DataFrame(data)
print(df)

print("\nAverage Salary by Department")
print(df.groupby("Department")["Salary"].mean())

print("\nMaximum Salary by Department")
print(df.groupby("Department")["Salary"].max())

print("\nMinimum Salary by Department")
print(df.groupby("Department")["Salary"].min())

print("\nTotal Salary by Department")
print(df.groupby("Department")["Salary"].sum())

print("\nEmployee Count")
print(df.groupby("Department")["Employee"].count())

# Multiple Aggregations
print(
    df.groupby("Department").agg({
        "Salary": ["mean", "max", "min", "sum"],
        "Experience": ["mean", "max"]
    })
)

# Group by Multiple Columns
data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Gender": ["M", "F", "M", "F"],
    "Salary": [50000, 55000, 40000, 42000]
}
df = pd.DataFrame(data)
print(df.groupby(["Department", "Gender"])["Salary"].mean())