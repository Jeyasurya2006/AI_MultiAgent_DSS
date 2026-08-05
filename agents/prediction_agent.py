from sklearn.linear_model import LinearRegression
import pandas as pd


class PredictionAgent:

    def predict(self, file_path):

        data = pd.read_excel(file_path)

        X = data[["Month"]]

        y = data["Sales"]

        model = LinearRegression()

        model.fit(X, y)

        next_month = pd.DataFrame({"Month": [len(data) + 1]})
        prediction = model.predict(next_month)
        return round(prediction[0], 2)