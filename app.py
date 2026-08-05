import streamlit as st
import pandas as pd
import plotly.express as px
from agents.orchestrator_agent import OrchestratorAgent
from reports.pdf_generator import generate_pdf

st.set_page_config(
    page_title="AI Multi-Agent DSS",
    page_icon="📊",
    layout="wide"
)

st.title("🤖 AI Multi-Agent Decision Support System")

orchestrator = OrchestratorAgent()

# Upload Excel file
uploaded_file = st.file_uploader(
    "📂 Upload your Sales Excel File",
    type=["xlsx"]
)

# Stop if no file is uploaded
if uploaded_file is None:
    st.info("Please upload an Excel file to continue.")
    st.stop()

# Save uploaded file
with open("datasets/uploaded_sales.xlsx", "wb") as f:
    f.write(uploaded_file.getbuffer())

# Analyze uploaded file
result = orchestrator.execute("datasets/uploaded_sales.xlsx")
st.write(result)

analysis = result["analysis"]
recommendations = result["recommendations"]
prediction = result["prediction"]
chat = "AI Chat will be enabled soon."
# st.subheader("🤖 AI Chat Assistant")
# st.success(chat)
# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", analysis["Total Sales"])
col2.metric("Average Sales", analysis["Average Sales"])
col3.metric("Highest Sale", analysis["Highest Sale"])
col4.metric("Lowest Sale", analysis["Lowest Sale"])

# Recommendations
st.subheader("💡 AI Recommendations")

for rec in recommendations:
    st.success(rec)

# Prediction
st.subheader("📈 Sales Prediction")
st.info(f"Predicted Month 13 Sales: {prediction}")

# Chart
st.subheader("📊 Sales Trend")

data = pd.read_excel("datasets/uploaded_sales.xlsx")

fig = px.bar(
    data,
    x="Product",
    y="Sales",
    color="Product",
    title="Product-wise Sales"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("🤖 AI Chat Assistant")

st.success(chat)
# Generate PDF
generate_pdf(analysis, recommendations, prediction)

st.subheader("📄 Download Report")

with open("reports/Sales_Report.pdf", "rb") as pdf_file:
    st.download_button(
        label="📥 Download Sales Report",
        data=pdf_file,
        file_name="Sales_Report.pdf",
        mime="application/pdf"
    )