import os
import sqlite3

import streamlit as st
import pandas as pd
import plotly.express as px

from agents.orchestrator_agent import OrchestratorAgent
from reports.pdf_generator import generate_pdf


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Multi-Agent DSS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background: linear-gradient(135deg, #eef6ff 0%, #f8fbff 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #102a56;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #60708a;
        margin-bottom: 25px;
    }

    .section-title {
        color: #123b78;
        font-weight: 750;
    }

    .agent-card {
        background: linear-gradient(
            135deg,
            #e0f7f1,
            #d5f1eb
        );
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 12px;
        border: 1px solid #b9e4db;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    }

    .agent-name {
        font-size: 17px;
        font-weight: 700;
        color: #087f5b;
    }

    .agent-status {
        font-size: 14px;
        color: #176b52;
        margin-top: 5px;
    }

    .metric-card {
        background: white;
        border-radius: 15px;
        padding: 18px;
        border: 1px solid #dce7f5;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    .recommendation {
        background: #edf6ff;
        border-left: 5px solid #1976d2;
        padding: 14px;
        border-radius: 8px;
        margin-bottom: 10px;
    }

    .system-online {
        background: #e7f8ef;
        color: #16804d;
        padding: 10px 15px;
        border-radius: 10px;
        font-weight: 700;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# ============================================================
# LOGIN SYSTEM
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

    # ---------- LOGIN PAGE CSS ----------
    st.markdown(
        """
        <style>

        .stApp {
            background:
                radial-gradient(
                    circle at 50% 15%,
                    #172d5c 0%,
                    #0b1638 35%,
                    #050b1f 75%,
                    #030712 100%
                );
        }

        .block-container {
            max-width: 850px;
            padding-top: 4rem;
            padding-bottom: 2rem;
        }

        /* Login title */
        .login-title {
            text-align: center;
            color: white;
            font-size: 42px;
            font-weight: 800;
            margin-top: 10px;
            margin-bottom: 5px;
        }

        .login-subtitle {
            text-align: center;
            color: #9fb1d0;
            font-size: 17px;
            margin-bottom: 35px;
        }

        /* Input labels */
        .stTextInput label {
            color: #dce7ff !important;
            font-weight: 600 !important;
        }

        /* Input boxes */
        .stTextInput input {
            background-color: #f7f9fc !important;
            border-radius: 12px !important;
            border: 1px solid #315da8 !important;
            height: 48px !important;
        }

        /* Login button */
        .stButton > button {
            width: 100%;
            height: 50px;
            border-radius: 12px;
            border: none;
            background: linear-gradient(
                90deg,
                #1769e0,
                #2989ff
            );
            color: white;
            font-size: 17px;
            font-weight: 700;
            box-shadow: 0 5px 20px rgba(41,137,255,0.30);
        }

        .stButton > button:hover {
            background: linear-gradient(
                90deg,
                #2989ff,
                #1769e0
            );
            color: white;
        }

        .login-footer {
            text-align: center;
            margin-top: 30px;
            color: #62a8ff;
            font-size: 13px;
            letter-spacing: 3px;
            font-weight: 600;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # ---------- LOGO ----------
    logo_path = "assets/logo.png"

    if os.path.exists(logo_path):

        col_left, col_center, col_right = st.columns(
            [1, 2, 1]
        )

        with col_center:

            st.image(
                logo_path,
                width=180
            )

    else:

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:80px;
                margin-bottom:10px;
            ">
                🤖
            </div>
            """,
            unsafe_allow_html=True
        )


    # ---------- TITLE ----------

    st.markdown(
        """
        <div class="login-title">
            AI Multi-Agent DSS
        </div>

        <div class="login-subtitle">
            Intelligent Decision Support System
        </div>
        """,
        unsafe_allow_html=True
    )


    # ---------- LOGIN FORM ----------

    username = st.text_input(
        "👤 Username",
        placeholder="Enter username",
        key="login_username"
    )


    password = st.text_input(
        "🔐 Password",
        type="password",
        placeholder="Enter password",
        key="login_password"
    )


    st.markdown("<br>", unsafe_allow_html=True)


    if st.button(
        "🚀 LOGIN TO DSS",
        use_container_width=True
    ):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error(
                "❌ Invalid username or password"
            )


    # ---------- FOOTER ----------

    st.markdown(
        """
        <div class="login-footer">
            ANALYZE • PREDICT • RECOMMEND • DECIDE
        </div>
        """,
        unsafe_allow_html=True
    )


    st.stop()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <h2 style="color:white;">
        🤖 AI Multi-Agent DSS
    </h2>
    """,
    unsafe_allow_html=True
)

if st.sidebar.button(
    "🚪 Logout",
    use_container_width=True
):

    st.session_state.logged_in = False
    st.rerun()


menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Sales History",
        "About Project"
    ]
)


# ============================================================
# ORCHESTRATOR
# ============================================================

try:

    orchestrator = OrchestratorAgent()

except Exception as e:

    st.error(
        f"❌ Unable to initialize AI agents: {e}"
    )

    st.stop()


# ============================================================
# ABOUT PROJECT
# ============================================================

if menu == "About Project":

    st.markdown(
        '<h1 class="main-title">📖 About AI Multi-Agent DSS</h1>',
        unsafe_allow_html=True
    )

    st.write(
        """
        ### 🤖 AI Multi-Agent Decision Support System

        An intelligent decision-support application designed to
        analyze sales data, generate business recommendations,
        predict future sales and answer user questions using
        multiple specialized AI agents.
        """
    )

    st.markdown("---")

    st.subheader("🎯 Project Objective")

    st.write(
        """
        The main objective of this project is to automate sales
        analysis and support business decision-making using a
        multi-agent architecture.
        """
    )

    st.subheader("🤖 Multi-Agent Architecture")

    architecture = pd.DataFrame(
        {
            "Agent": [
                "Data Agent",
                "Cleaning Agent",
                "Analysis Agent",
                "Prediction Agent",
                "Recommendation Agent",
                "Chat Agent",
                "Database Agent"
            ],
            "Function": [
                "Loads sales data",
                "Cleans and prepares data",
                "Calculates sales statistics",
                "Predicts future sales",
                "Generates business recommendations",
                "Answers sales-related questions",
                "Stores analysis and prediction results"
            ]
        }
    )

    st.dataframe(
        architecture,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("🛠️ Technologies Used")

    tech_cols = st.columns(5)

    technologies = [
        "🐍 Python",
        "🐼 Pandas",
        "🤖 Scikit-learn",
        "🌐 Streamlit",
        "📊 Plotly",
        "🗄️ SQLite",
        "📄 ReportLab",
        "📑 Excel",
        "🔐 Session Login",
        "📈 Machine Learning"
    ]

    for i, tech in enumerate(technologies):

        with tech_cols[i % 5]:

            st.info(tech)

    st.subheader("🔄 System Workflow")

    st.code(
        """
Excel Upload
      ↓
Data Agent
      ↓
Cleaning Agent
      ↓
Analysis Agent
      ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
Prediction    Recommendation    Chat Agent
 ↓               ↓                ↓
        Decision Support
              ↓
        SQLite Database
              ↓
         PDF Report
        """,
        language="text"
    )

    st.subheader("👨‍💻 Developer")

    st.success(
        """
        **Jeyasurya**

        B.Tech – Artificial Intelligence & Data Science
        """
    )

    st.stop()


# ============================================================
# SALES HISTORY
# ============================================================

if menu == "Sales History":

    st.markdown(
        '<h1 class="main-title">📊 Sales History</h1>',
        unsafe_allow_html=True
    )

    st.caption(
        "🗄️ Stored sales records from the SQLite database"
    )

    database_path = "database/database.db"

    if not os.path.exists(database_path):

        st.warning(
            "⚠️ Database file not found."
        )

        st.stop()

    try:

        conn = sqlite3.connect(database_path)

        data = pd.read_sql(
            "SELECT * FROM sales_history",
            conn
        )

        conn.close()

        st.metric(
            "📄 Total Records",
            len(data)
        )

        st.markdown("---")

        st.subheader("📋 Sales Records")

        if data.empty:

            st.info(
                "No sales records found in the database."
            )

        else:

            st.dataframe(
                data,
                use_container_width=True,
                hide_index=True
            )

    except Exception as e:

        st.error(
            f"❌ Unable to load sales history: {e}"
        )

    st.stop()


# ============================================================
# DASHBOARD HEADER
# ============================================================

st.markdown(
    """
    <div class="main-title">
        🤖 AI Multi-Agent Decision Support System
    </div>

    <div class="subtitle">
        📊 Smart Sales Analysis &nbsp;|&nbsp;
        🤖 AI Recommendations &nbsp;|&nbsp;
        📈 Prediction &nbsp;|&nbsp;
        🗄️ SQLite Database
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FILE UPLOAD
# ============================================================

st.subheader("📂 Upload your Sales Excel File")

uploaded_file = st.file_uploader(
    "Upload Excel file",
    type=["xlsx"],
    label_visibility="collapsed"
)


if uploaded_file is None:

    st.info(
        "📌 Please upload an Excel file to continue."
    )

    st.stop()


# ============================================================
# SAVE UPLOADED FILE
# ============================================================

os.makedirs(
    "datasets",
    exist_ok=True
)

uploaded_path = (
    "datasets/uploaded_sales.xlsx"
)


with open(
    uploaded_path,
    "wb"
) as f:

    f.write(
        uploaded_file.getbuffer()
    )


# ============================================================
# READ AND VALIDATE DATA
# ============================================================

try:

    uploaded_data = pd.read_excel(
        uploaded_path
    )

except Exception as e:

    st.error(
        f"❌ Unable to read Excel file: {e}"
    )

    st.stop()


# Required columns

required_columns = [
    "Product",
    "Sales"
]


missing_columns = [
    column
    for column in required_columns
    if column not in uploaded_data.columns
]


if missing_columns:

    st.error(
        "❌ Missing required column(s): "
        + ", ".join(missing_columns)
    )

    st.info(
        "Your Excel file must contain: Product and Sales columns."
    )

    st.stop()


# Empty dataset

if uploaded_data.empty:

    st.error(
        "❌ The uploaded Excel file is empty."
    )

    st.stop()


# Convert sales to numeric

uploaded_data["Sales"] = pd.to_numeric(
    uploaded_data["Sales"],
    errors="coerce"
)


uploaded_data = uploaded_data.dropna(
    subset=["Sales"]
)


if uploaded_data.empty:

    st.error(
        "❌ No valid numeric Sales values found."
    )

    st.stop()


# ============================================================
# RUN MULTI-AGENT SYSTEM
# ============================================================

try:

    with st.spinner(
        "🤖 AI Agents are analyzing your sales data..."
    ):

        result = orchestrator.execute(
            uploaded_path
        )

except Exception as e:

    st.error(
        f"❌ Unable to process sales data: {e}"
    )

    st.stop()


# ============================================================
# GET RESULTS SAFELY
# ============================================================

analysis = result.get(
    "analysis",
    {}
)

recommendations = result.get(
    "recommendations",
    []
)

prediction = result.get(
    "prediction",
    0
)


# ============================================================
# AGENT STATUS
# ============================================================

st.markdown("---")

st.markdown(
    '<h2 class="section-title">🤖 AI Agent Status</h2>',
    unsafe_allow_html=True
)


agent_col1, agent_col2, agent_col3 = st.columns(3)


agents = [
    ("📂 Data Agent", agent_col1),
    ("🧹 Cleaning Agent", agent_col1),
    ("📊 Analysis Agent", agent_col2),
    ("📈 Prediction Agent", agent_col2),
    ("💡 Recommendation Agent", agent_col3),
    ("🤖 Chat Agent", agent_col3)
]


for agent_name, column in agents:

    with column:

        st.markdown(
            f"""<div class="agent-card">
<div class="agent-name">🟢 {agent_name}</div>
<div class="agent-status">Working</div>
</div>""",
            unsafe_allow_html=True
        )

st.success(
    "🟢 Database Agent — Connected"
)


# ============================================================
# WELCOME
# ============================================================

welcome_col1, welcome_col2 = st.columns(
    [3, 1]
)


with welcome_col1:

    st.markdown(
        "### 👋 Welcome, Admin"
    )

    st.caption(
        "AI-powered sales intelligence and decision support"
    )


with welcome_col2:

    st.markdown(
        """
        <div class="system-online">
            🟢 System Online
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DASHBOARD SUMMARY
# ============================================================

st.markdown("---")

st.markdown(
    '<h2 class="section-title">📊 Dashboard Summary</h2>',
    unsafe_allow_html=True
)


st.success(
    "🟢 System Status: All AI Agents are Working"
)


st.write(
    """
    This dashboard analyzes uploaded sales data,
    predicts future sales, provides AI recommendations,
    and visualizes business insights.
    """
)

# ============================================================
# KEY METRICS
# ============================================================

st.markdown("---")

st.subheader("📊 Key Business Metrics")

# Get analysis values safely
analysis = result.get("analysis", {})

total_sales = analysis.get(
    "Total Sales",
    uploaded_data["Sales"].sum()
)

average_sales = analysis.get(
    "Average Sales",
    uploaded_data["Sales"].mean()
)

highest_sale = analysis.get(
    "Highest Sale",
    uploaded_data["Sales"].max()
)

lowest_sale = analysis.get(
    "Lowest Sale",
    uploaded_data["Sales"].min()
)

# Create metric columns
metric1, metric2, metric3, metric4 = st.columns(4)

# Display metrics
with metric1:
    st.metric(
        "💰 Total Sales",
        f"₹{total_sales:,.0f}"
    )

with metric2:
    st.metric(
        "📊 Average Sales",
        f"₹{average_sales:,.2f}"
    )

with metric3:
    st.metric(
        "🏆 Highest Sale",
        f"₹{highest_sale:,.0f}"
    )

with metric4:
    st.metric(
        "📉 Lowest Sale",
        f"₹{lowest_sale:,.0f}"
    )
# ============================================================
# AI RECOMMENDATIONS
# ============================================================

st.markdown("---")

st.subheader("💡 AI Recommendations")

if recommendations:

    for i, rec in enumerate(recommendations, start=1):

        st.info(
            f"💡 Recommendation {i}\n\n{rec}"
        )

else:

    st.info(
        "ℹ️ No AI recommendations available."
    )
# ============================================================
# SALES PREDICTION
# ============================================================

st.markdown("---")

st.subheader("📈 Sales Prediction")

next_month = len(uploaded_data) + 1

# Create two columns
prediction_col1, prediction_col2 = st.columns(2)

# Next month
with prediction_col1:
    st.metric(
        "🔮 Next Month",
        f"Month {next_month}"
    )

# Prediction value
try:
    prediction_value = float(prediction)
except (TypeError, ValueError):
    prediction_value = 0.0

with prediction_col2:
    st.metric(
        "💰 Predicted Sales",
        f"₹{prediction_value:,.2f}"
    )


# ============================================================
# PRODUCT FILTER
# ============================================================

st.markdown("---")

st.subheader("📊 Sales Trend")


products = sorted(
    uploaded_data["Product"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)


selected_product = st.selectbox(
    "🔍 Select Product",
    ["All"] + products
)


chart_data = uploaded_data.copy()


if selected_product != "All":

    chart_data = chart_data[
        chart_data["Product"].astype(str)
        == selected_product
    ]


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

st.markdown("---")

st.subheader("📌 Business Insights")

if not chart_data.empty:

    product_summary = (
        chart_data
        .groupby("Product", as_index=False)["Sales"]
        .sum()
    )

    best_product = product_summary.loc[
        product_summary["Sales"].idxmax(),
        "Product"
    ]

    worst_product = product_summary.loc[
        product_summary["Sales"].idxmin(),
        "Product"
    ]

else:

    best_product = "N/A"
    worst_product = "N/A"


insight_col1, insight_col2, insight_col3, insight_col4 = st.columns(4)


with insight_col1:
    st.metric(
        "🏆 Best Selling Product",
        str(best_product)
    )


with insight_col2:
    st.metric(
        "📉 Lowest Selling Product",
        str(worst_product)
    )


with insight_col3:
    st.metric(
        "💰 Total Revenue",
        f"₹{total_sales:,.0f}"
    )


with insight_col4:
    st.metric(
        "🔮 Next Month Prediction",
        f"₹{prediction_value:,.2f}"
    )

# ============================================================
# PRODUCT BAR CHART
# ============================================================

st.subheader("📊 Product-wise Sales")


if not chart_data.empty:

    product_sales = (
        chart_data
        .groupby("Product", as_index=False)["Sales"]
        .sum()
    )

    fig = px.bar(
        product_sales,
        x="Product",
        y="Sales",
        title="Product-wise Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="Product",
        yaxis_title="Sales",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info(
        "No sales data available for the selected product."
    )


# ============================================================
# PIE CHART
# ============================================================

st.subheader("🥧 Sales Distribution")


if not chart_data.empty:

    product_sales = (
        chart_data
        .groupby("Product", as_index=False)["Sales"]
        .sum()
    )

    fig2 = px.pie(
        product_sales,
        names="Product",
        values="Sales",
        title="Product-wise Sales Distribution",
        hole=0.35
    )

    fig2.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:

    st.info(
        "No sales distribution available."
    )


# ============================================================
# MONTHLY SALES TREND
# ============================================================

st.subheader("📈 Monthly Sales Trend")


trend_data = uploaded_data.copy()


if "Date" in trend_data.columns:

    trend_data["Date"] = pd.to_datetime(
        trend_data["Date"],
        errors="coerce"
    )

    trend_data = trend_data.dropna(
        subset=["Date", "Sales"]
    )


    if not trend_data.empty:

        monthly_data = (
            trend_data
            .assign(
                Month=trend_data["Date"]
                .dt.to_period("M")
                .astype(str)
            )
            .groupby(
                "Month",
                as_index=False
            )["Sales"]
            .sum()
        )


        fig3 = px.line(
            monthly_data,
            x="Month",
            y="Sales",
            markers=True,
            title="Monthly Sales Trend"
        )


        fig3.update_layout(
            template="plotly_white",
            xaxis_title="Month",
            yaxis_title="Sales"
        )


        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    else:

        st.info(
            "📅 Date column exists, but no valid dates were found."
        )

else:

    st.info(
        "📅 Monthly Sales Trend requires a Date column in the uploaded dataset."
    )


# ============================================================
# AI CHAT ASSISTANT
# ============================================================

st.markdown("---")

st.subheader("🤖 AI Chat Assistant")


st.write(
    "Ask a question about your sales data:"
)


user_question = st.text_input(
    "💬 Your Question",
    placeholder="Example: What is the total sales?"
)


if st.button(
    "🤖 Ask AI",
    use_container_width=True
):

    if user_question.strip():

        try:

            chat_response = (
                orchestrator
                .chat_agent
                .answer(
                    user_question,
                    analysis,
                    recommendations
                )
            )

            st.success(
                chat_response
            )

        except Exception as e:

            st.error(
                f"❌ Chat Agent error: {e}"
            )

    else:

        st.warning(
            "⚠️ Please enter a question."
        )


# ============================================================
# PDF REPORT
# ============================================================

st.markdown("---")

st.subheader("📄 Download Report")


try:

    os.makedirs(
        "reports",
        exist_ok=True
    )

    generate_pdf(
        analysis,
        recommendations,
        prediction_value,
        next_month
    )


    report_path = (
        "reports/Sales_Report.pdf"
    )


    if os.path.exists(report_path):

        with open(
            report_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="📥 Download Sales Report",
                data=pdf_file.read(),
                file_name="Sales_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    else:

        st.warning(
            "⚠️ PDF report was not generated."
        )


except Exception as e:

    st.error(
        f"❌ Unable to generate PDF report: {e}"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#60708a;
        padding:20px;
    ">
        🤖 <b>AI Multi-Agent DSS</b><br>
        Intelligent Analytics • Prediction • Recommendation • Decision Support
        <br><br>
        Developed by <b>Jeyasurya</b> | B.Tech AI & Data Science
    </div>
    """,
    unsafe_allow_html=True
)