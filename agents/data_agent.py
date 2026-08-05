import pandas as pd


class DataAgent:

    def load_data(self, file_path):

        if file_path.endswith(".csv"):
            data = pd.read_csv(file_path)

        elif file_path.endswith(".xlsx"):
            data = pd.read_excel(file_path)

        else:
            raise ValueError("Unsupported file format")

        return data