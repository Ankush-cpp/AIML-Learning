import pandas as pd

employees = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104],
    "Name": ["Ankush", "Rahul", "Priya", "Neha"],
    "Department": ["IT", "HR", "IT", "Sales"]
})

salary = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104],
    "Salary": [50000, 40000, 55000, 45000]
})

# Merge
merged = pd.merge(employees, salary, on="Emp_ID")
print("Merged Data")
print(merged)

# Join
employees_index = employees.set_index("Emp_ID")
salary_index = salary.set_index("Emp_ID")

joined = employees_index.join(salary_index)
print("\nJoined Data")
print(joined)

# Pivot
sales = pd.DataFrame({
    "Month": ["Jan", "Jan", "Feb", "Feb"],
    "Product": ["Laptop", "Phone", "Laptop", "Phone"],
    "Sales": [20, 35, 25, 40]
})

pivot = sales.pivot(index="Month", columns="Product", values="Sales")

print("\nPivot Table")
print(pivot)

# Melt
melt = pd.melt(
    pivot.reset_index(),
    id_vars="Month",
    value_vars=["Laptop", "Phone"],
    var_name="Product",
    value_name="Sales"
)

print("\nMelted Data")
print(melt)