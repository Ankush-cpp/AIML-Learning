import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1200, 1500, 1800, 1600, 2100]
}

df = pd.DataFrame(data)

# Display data
print(df)

# Plot data
plt.plot(df["Month"], df["Sales"])

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()