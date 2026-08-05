from agents.data_agent import DataAgent
from agents.cleaning_agent import CleaningAgent
from agents.analysis_agent import AnalysisAgent
from agents.prediction_agent import PredictionAgent
from agents.recommendation_agent import RecommendationAgent
from agents.chat_agent import ChatAgent


class OrchestratorAgent:

    def __init__(self):
        self.data_agent = DataAgent()
        self.cleaning_agent = CleaningAgent()
        self.analysis_agent = AnalysisAgent()
        self.prediction_agent = PredictionAgent()
        self.recommendation_agent = RecommendationAgent()
        self.chat_agent = ChatAgent()

    def execute(self, file_path):
        data = self.data_agent.load_data(file_path)

        clean_data = self.cleaning_agent.clean_data(data)

        analysis = self.analysis_agent.analyze(clean_data)

        recommendations = self.recommendation_agent.recommend(clean_data)

        prediction = self.prediction_agent.predict("datasets/monthly_sales.xlsx")

        chat_response = self.chat_agent.answer(
            "highest sales",
            analysis,
            recommendations
        )

        return {
            "analysis": analysis,
            "recommendations": recommendations,
            "prediction": prediction,
            "chat": chat_response
        }