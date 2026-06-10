import pandas as pd

csv_data = pd.read_csv("data.csv")

print(csv_data.head())

print(csv_data.tail())

print(csv_data.info())

json_data = pd.read_json("data.json")

print(json_data)

print(json_data.describe())