import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1200, 1500, 1800, 1700, 2100],
    "Profit": [200, 250, 320, 300, 400]
}
df = pd.DataFrame(data)

# Line Plot
df.plot(x="Month", y="Sales", kind="line")
plt.show()

# Bar Plot
df.plot(x="Month", y="Profit", kind="bar")
plt.show()

# Export CSV
df.to_csv("sales_data.csv", index=False)

# Export Excel
df.to_excel("sales_data.xlsx", index=False)

print("Files exported successfully.")