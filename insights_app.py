
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import google.generativeai as genai
import io


genai.configure(api_key="AIzaSyCVAXEEtxknZrDHJN0FglkP5I1AIcKMibo")  # Replace with your key

st.set_page_config(page_title="Retail Data Insight Generator", layout="wide")
st.title("📊 Automated Retail Insight Generator with Gemini")


uploaded_file = st.file_uploader("C:\\Users\\prakirti\\OneDrive\\Desktop\\DynPro\\sales_insights\\Superstore.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding="latin-1")
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    
    summary = df.describe().to_string()
    st.subheader("📈 Summary Statistics")
    st.text(summary)

    
    if st.button("🧠 Generate Business Insight"):
        prompt = f"""
        Here is a summary of retail sales data:

        {summary}

        Please generate a simple business insight report that:
        - Highlights trends
        - Explains any outliers or extreme values
        - Gives plain-language insights for decision-making
        """

        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)

        st.subheader("📄 AI-Generated Business Insight")
        st.markdown(response.text)

        
        st.subheader("📊 Total Profit by Category")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(data=df, x='Category', y='Profit', estimator=sum, ci=None, ax=ax)
        ax.set_title("Profit by Category")
        ax.set_ylabel("Profit (₹)")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

        
        with pd.ExcelWriter("retail_ai_report.xlsx", engine="xlsxwriter") as writer:
            df.describe().to_excel(writer, sheet_name="Summary Stats")
            pd.DataFrame({"Insight": [response.text]}).to_excel(writer, sheet_name="AI Insights")

        with open("retail_ai_report.xlsx", "rb") as f:
            st.download_button("⬇️ Download Report as Excel", f, "retail_ai_report.xlsx")

