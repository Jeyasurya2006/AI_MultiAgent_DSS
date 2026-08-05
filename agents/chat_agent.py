class ChatAgent:

    def answer(self, question, analysis, recommendations):
        question = question.lower()

        if "highest" in question:
            return f"The highest sale is ₹{analysis['Highest Sale']}. {recommendations[0]}"

        elif "lowest" in question:
            return f"The lowest sale is ₹{analysis['Lowest Sale']}. {recommendations[-1]}"

        elif "total" in question:
            return f"Total sales are ₹{analysis['Total Sales']}."

        elif "average" in question:
            return f"Average sales are ₹{analysis['Average Sales']}."

        else:
            return "Sorry, I can answer questions about total, average, highest and lowest sales."