# Function to generate insights from cleaned data

def get_insights(data):

    # Handle empty dataset
    if len(data) == 0:
        print("No data available")
        return

    # Average rating
    total_ratings = 0

    for user in data:
        total_ratings += float(user['rating'])

    avg_rating = round(total_ratings / len(data), 2)

    print(f" Average Product Rating: {avg_rating}")

    # Poor rating percentage
    poor_ratings = 0

    for user in data:
        if float(user['rating']) < 3:
            poor_ratings += 1

    poor_percentage = round((poor_ratings / len(data)) * 100, 2)

    print(f" Percentage of Users with Poor Rating: {poor_percentage}%")

    # Count users with good ratings
    good_ratings = 0

    for user in data:
        if float(user['rating']) >= 4:
            good_ratings += 1

    print(f" Users with Good Ratings: {good_ratings}")

    # Total users
    print(f" Total Users: {len(data)}")