import pandas as pd

print("PANDAS SERIES PRACTICE\n")

data = [10, 20, 30, 40, 50]

series = pd.Series(data)

print("Pandas Series:")
print(series)

print("\nSERIES PROPERTIES\n")

print("Values:")
print(series.values)

print("\nIndex:")
print(series.index)

print("\nDatatype:")
print(series.dtype)

print("\nShape:")
print(series.shape)

print("\nSize:")
print(series.size)

print("\nCUSTOM INDEX\n")

students = pd.Series(
    [85, 90, 78],
    index=["Ankush", "Rahul", "Priya"]
)

print(students)

print("\nAccess Single Value:")
print(students["Ankush"])

print("\nSERIES OPERATIONS\n")

print("Addition:")
print(series + 10)

print("\nMultiplication:")
print(series * 2)

print("\nMean:")
print(series.mean())

print("\nMaximum:")
print(series.max())

print("\nMinimum:")
print(series.min())

print("\nBOOLEAN FILTERING\n")

print("Values greater than 25:")
print(series[series > 25])

print("\nSERIES FROM DICTIONARY\n")

mobile_sales = {
    "Apple": 120,
    "Samsung": 95,
    "OnePlus": 70
}

sales_series = pd.Series(mobile_sales)

print(sales_series)

print("\nEDA BASIC INSIGHTS\n")

print("Total Sales:", sales_series.sum())
print("Average Sales:", sales_series.mean())
print("Highest Sales:", sales_series.max())

print("\nSORTING\n")

print(sales_series.sort_values())

print("\nCHECKING NULL VALUES\n")

series_with_null = pd.Series([10, 20, None, 40])

print(series_with_null)

print("\nNull Check:")
print(series_with_null.isnull())