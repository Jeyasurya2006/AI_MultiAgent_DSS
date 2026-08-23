class ChatAgent:

    def answer(self, question, analysis, recommendations):

        question = question.lower().strip()

        # Highest sales
        if "highest" in question or "maximum" in question or "top" in question:
            return (
                f"The highest sale is ₹{analysis['Highest Sale']}. "
                f"{recommendations[0]}"
            )

        # Lowest sales
        elif "lowest" in question or "minimum" in question:
            return (
                f"The lowest sale is ₹{analysis['Lowest Sale']}. "
                f"{recommendations[1]}"
            )

        # Total sales
        elif "total" in question:
            return f"The total sales are ₹{analysis['Total Sales']}."

        # Average sales
        elif "average" in question or "mean" in question:
            return f"The average sales are ₹{analysis['Average Sales']}."

        # Recommendation
        elif (
            "recommend" in question
            or "recommendation" in question
            or "suggest" in question
        ):
            return " ".join(recommendations)

        # General summary
        elif (
            "summary" in question
            or "overview" in question
            or "sales" in question
        ):
            return (
                f"Sales summary: Total sales are ₹{analysis['Total Sales']}, "
                f"average sales are ₹{analysis['Average Sales']}, "
                f"highest sale is ₹{analysis['Highest Sale']}, "
                f"and lowest sale is ₹{analysis['Lowest Sale']}."
            )

        # Unknown question
        else:
            return (
                "I can help with total sales, average sales, "
                "highest sales, lowest sales, and recommendations."
            )