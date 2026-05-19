from cleaning import clean_data
from insights import get_insights
from recommendation import (
    get_recommendations,
    show_recommendations
)

# Raw user data
data = [
    {"name": "Ankush", "rating": " Five ", "age": 21},
    {"name": "Rahul", "rating": "two", "age": None},
    {"name": "ankush", "rating": "4", "age": 21},
    {"name": "Priya", "rating": "three", "age": 19}
]

# Step 1: Clean data
cleaned_data = clean_data(data)

print(" Cleaned Data:\n")
print(cleaned_data)

print("\n-------------------------\n")

# Step 2: Generate insights
get_insights(cleaned_data)

print("\n-------------------------\n")

# Step 3: Generate recommendations
recommendations = get_recommendations(cleaned_data)

show_recommendations(recommendations)