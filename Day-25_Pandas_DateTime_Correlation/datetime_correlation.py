import pandas as pd

data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03"],
    "Sales": [1200, 1500, 1800],
    "Profit": [200, 250, 320]
}
df = pd.DataFrame(data)

# Convert string to datetime
df["Date"] = pd.to_datetime(df["Date"])
print(df)

# Date properties
print(df["Date"].dt.day)
print(df["Date"].dt.month)
print(df["Date"].dt.year)
print(df["Date"].dt.day_name())

# Correlation
print(df[["Sales", "Profit"]].corr())