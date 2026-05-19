# Function to generate product recommendations

def get_recommendations(data):

    recommendations = []

    for user in data:

        current_recommendation = {}

        current_recommendation['name'] = user['name']

        rating = float(user['rating'])

        # Recommendation logic
        if rating >= 4:
            current_recommendation['recommended_brand'] = "Apple"

        elif rating >= 3:
            current_recommendation['recommended_brand'] = "Samsung"

        else:
            current_recommendation['recommended_brand'] = "Nokia"

        recommendations.append(current_recommendation)

    return recommendations


# Display recommendations
def show_recommendations(recommendations):

    print("\n📱 Product Recommendations:\n")

    for item in recommendations:
        print(
            f"{item['name']} → Recommended Brand: {item['recommended_brand']}"
        )