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
st.caption("📊 Smart Sales Analysis | 🤖 AI Recommendations | 📈 Prediction | 🗄️ SQLite Database")
st.sidebar.title("🤖 AI Multi-Agent DSS")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Sales History",
        "About Project"
    ]
)

orchestrator = OrchestratorAgent()
if menu == "About Project":
    st.header("📖 About Project")

    st.write("""
    ### AI Multi-Agent Decision Support System

    **Technologies Used**
    - Python
    - Streamlit
    - Pandas
    - Plotly
    - SQLite
    - Scikit-learn

    **Agents**
    - Data Agent
    - Cleaning Agent
    - Analysis Agent
    - Prediction Agent
    - Recommendation Agent
    - Chat Agent

    **Developer**
    Jeyasurya
    """)

    st.stop()
if menu == "Sales History":
    st.header("📊 Sales History")

    import sqlite3

    conn = sqlite3.connect("database/database.db")

    data = pd.read_sql("SELECT * FROM sales_history", conn)

    st.dataframe(data, use_container_width=True)

    conn.close()

    st.stop()
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

analysis = result["analysis"]
recommendations = result["recommendations"]
prediction = result["prediction"]
chat = result["chat"]
# st.subheader("🤖 AI Chat Assistant")
# st.success(chat)
# Metrics
st.markdown("---")

st.header("📊 Dashboard Summary")

st.write(
    "This dashboard analyzes uploaded sales data, predicts future sales, "
    "provides AI recommendations, and visualizes business insights."
)

st.markdown("---")
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

# Product Filter
selected_product = st.selectbox(
    "🔍 Select Product",
    ["All"] + list(data["Product"].unique())
)

if selected_product != "All":
    data = data[data["Product"] == selected_product]

# 👇 Business Insights inga varanum
st.subheader("📌 Business Insights")

best_product = data.loc[data["Sales"].idxmax(), "Product"]
worst_product = data.loc[data["Sales"].idxmin(), "Product"]

st.success(f"🏆 Best Selling Product : {best_product}")
st.error(f"📉 Lowest Selling Product : {worst_product}")
st.info(f"💰 Total Revenue : ₹{analysis['Total Sales']}")
st.warning(f"📈 Predicted Next Month Sales : ₹{prediction:.2f}")

fig = px.bar(
    data,
    x="Product",
    y="Sales",
    color="Product",
    title="Product-wise Sales"
)
st.plotly_chart(fig, use_container_width=True)

# Pie Chart
st.subheader("🥧 Sales Distribution")

fig2 = px.pie(
    data,
    names="Product",
    values="Sales",
    title="Product-wise Sales Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# Monthly Line Chart
st.subheader("📈 Monthly Sales Trend")

monthly_data = pd.read_excel("datasets/monthly_sales.xlsx")

fig3 = px.line(
    monthly_data,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)
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