# Function to clean raw user data

def clean_data(data):

    # Convert text ratings to numbers
    text_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    unique_users = set()
    cleaned_data = []

    for user in data:

        # -------------------------------
        # Clean rating
        # -------------------------------

        raw_rating = str(user['rating']).strip().lower()

        if raw_rating in text_to_num:
            user['rating'] = text_to_num[raw_rating]

        else:
            try:
                user['rating'] = float(raw_rating)

            except:
                user['rating'] = 0

        # -------------------------------
        # Handle missing age
        # -------------------------------

        raw_age = user.get("age")

        if raw_age is None:
            user["age"] = "Not Available"

        # -------------------------------
        # Remove duplicate users
        # -------------------------------

        name = user['name'].strip().lower()

        if name in unique_users:
            continue

        unique_users.add(name)

        # -------------------------------
        # Store cleaned user
        # -------------------------------

        cleaned_data.append(user)

    return cleaned_data