from agents.data_agent import DataAgent
from agents.cleaning_agent import CleaningAgent
from agents.analysis_agent import AnalysisAgent
from agents.prediction_agent import PredictionAgent
from agents.recommendation_agent import RecommendationAgent
from agents.chat_agent import ChatAgent
from database.database_agent import DatabaseAgent


class OrchestratorAgent:

    def __init__(self):
        self.data_agent = DataAgent()
        self.cleaning_agent = CleaningAgent()
        self.analysis_agent = AnalysisAgent()
        self.prediction_agent = PredictionAgent()
        self.recommendation_agent = RecommendationAgent()
        self.chat_agent = ChatAgent()
        self.database_agent = DatabaseAgent()

    def execute(self, file_path):

        # 1. Load uploaded data
        data = self.data_agent.load_data(file_path)

        # 2. Clean data
        clean_data = self.cleaning_agent.clean_data(data)

        # 3. Analyze data
        analysis = self.analysis_agent.analyze(clean_data)

        # 4. Generate recommendations
        recommendations = self.recommendation_agent.recommend(clean_data)

        # 5. Predict using the SAME uploaded file
        prediction = self.prediction_agent.predict(file_path)

        # 6. Save analysis and prediction
        self.database_agent.save_analysis(
            analysis,
            prediction
        )

        # 7. Default chat response
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

    def chat(self, question, analysis, recommendations):

        return self.chat_agent.answer(
            question,
            analysis,
            recommendations
        )