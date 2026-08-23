from sklearn.linear_model import LinearRegression
import pandas as pd


class PredictionAgent:

    def predict(self, file_path):

        # Load the uploaded Excel/CSV file
        if file_path.endswith(".csv"):
            data = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path)
        else:
            raise ValueError("Prediction supports only CSV and Excel files.")

        # Check Sales column
        if "Sales" not in data.columns:
            raise ValueError("Sales column is required for prediction.")

        # Remove invalid Sales values
        data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
        data = data.dropna(subset=["Sales"]).reset_index(drop=True)

        if len(data) < 2:
            raise ValueError("At least 2 valid sales records are required.")

        # Case 1: Month column exists
        if "Month" in data.columns:

            data["Month"] = pd.to_numeric(
                data["Month"], errors="coerce"
            )

            data = data.dropna(
                subset=["Month", "Sales"]
            ).reset_index(drop=True)

            X = data[["Month"]]
            y = data["Sales"]

            model = LinearRegression()
            model.fit(X, y)

            next_month = pd.DataFrame({
                "Month": [data["Month"].max() + 1]
            })

            prediction = model.predict(next_month)

        # Case 2: Date column exists
        elif "Date" in data.columns:

            data["Date"] = pd.to_datetime(
                data["Date"], errors="coerce"
            )

            data = data.dropna(
                subset=["Date", "Sales"]
            ).sort_values("Date").reset_index(drop=True)

            if len(data) < 2:
                raise ValueError(
                    "At least 2 valid dated sales records are required."
                )

            # Create sequential time index
            data["Time_Index"] = range(1, len(data) + 1)

            X = data[["Time_Index"]]
            y = data["Sales"]

            model = LinearRegression()
            model.fit(X, y)

            next_index = pd.DataFrame({
                "Time_Index": [len(data) + 1]
            })

            prediction = model.predict(next_index)

        # Case 3: No Month/Date column
        else:

            # Use row order as time sequence
            data["Time_Index"] = range(1, len(data) + 1)

            X = data[["Time_Index"]]
            y = data["Sales"]

            model = LinearRegression()
            model.fit(X, y)

            next_index = pd.DataFrame({
                "Time_Index": [len(data) + 1]
            })

            prediction = model.predict(next_index)

        return round(float(prediction[0]), 2)