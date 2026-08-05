import pandas as pd


class AnalysisAgent:

    def analyze(self, data):

        total_sales = data["Sales"].sum()

        average_sales = data["Sales"].mean()

        highest_sale = data["Sales"].max()

        lowest_sale = data["Sales"].min()

        return {
            "Total Sales": total_sales,
            "Average Sales": average_sales,
            "Highest Sale": highest_sale,
            "Lowest Sale": lowest_sale
        }