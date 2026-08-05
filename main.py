from agents.orchestrator_agent import OrchestratorAgent

orchestrator = OrchestratorAgent()

result = orchestrator.execute("datasets/sales_data.xlsx")

print("\n========== SALES ANALYSIS ==========")

for key, value in result["analysis"].items():
    print(f"{key}: {value}")

print("\n========== AI RECOMMENDATIONS ==========")

for recommendation in result["recommendations"]:
    print(f"• {recommendation}")

print("\n========== SALES PREDICTION ==========")
print(f"Predicted Month 13 Sales: {result['prediction']}")