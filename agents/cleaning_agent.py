class CleaningAgent:

    def clean_data(self, data):

        data = data.drop_duplicates()

        data = data.dropna()

        return data