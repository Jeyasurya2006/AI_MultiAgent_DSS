class ChatAgent:

    def answer(self, question, analysis, recommendations):

        if "highest" in question.lower():
            return f"The highest sale is ₹{analysis['Highest Sale']}. {recommendations[0]}"

        elif "lowest" in question.lower():
            return f"The lowest sale is ₹{analysis['Lowest Sale']}. {recommendations[1]}"

        else:
            return "Sales analysis completed successfully."