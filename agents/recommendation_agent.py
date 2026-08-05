class RecommendationAgent:

    def recommend(self, data):

        recommendations = []

        highest = data.loc[data["Sales"].idxmax(), "Product"]
        lowest = data.loc[data["Sales"].idxmin(), "Product"]

        recommendations.append(
            f"Increase stock for '{highest}' because it has the highest sales."
        )

        recommendations.append(
            f"Consider discounts or promotions for '{lowest}' because it has the lowest sales."
        )

        return recommendations