# 📊 Automated Retail Insight Generator with Gemini

This project is a **Streamlit web application** that helps automate **retail data analysis and insight generation**.  
It combines **data visualization, statistical summaries, and AI-powered insights** using **Google Gemini API**.

---

## 🚀 Features

- **Upload CSV Data**: Easily upload retail sales data (CSV format).  
- **Data Preview**: Instantly view the first few rows of your dataset.  
- **Summary Statistics**: Auto-generated descriptive statistics for numerical columns.  
- **AI-Powered Business Insights**:  
  - Highlights key trends  
  - Explains outliers and anomalies  
  - Provides plain-language insights for decision-making  
- **Data Visualization**: Bar chart of **total profit by category**.  
- **Export to Excel**: Download a report containing summary stats and AI-generated insights.  

---

## 🛠️ Tech Stack

- **Python**
- [Streamlit](https://streamlit.io/) – Web app framework  
- [Pandas](https://pandas.pydata.org/) – Data handling  
- [Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/) – Visualizations  
- [Google Gemini API](https://ai.google.dev/) – AI-powered insights  
- [XlsxWriter](https://xlsxwriter.readthedocs.io/) – Excel export  

---

## 📂 Project Structure

Retail-Insight-Generator
│── insights.py # Main Streamlit app
│── requirements.txt # Dependencies
│── README.md # Project documentation
│── retail_ai_report.xlsx # Generated Excel report (after running)


---

## ⚡ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/retail-insight-generator.git
   cd retail-insight-generator

2. **Install Dependencies
   ```bash
   pip install -r requirements.txt

3. Add you Google Gemini API Key
    ```bash
   genai.configure(api_key="YOUR_API_KEY_HERE")

4. Run the Streamlit app
   ```bash
   streamlit run app.py

---
## 📊 Usage

1. Launch the app in your browser (default: http://localhost:8501).

2. Upload your retail sales CSV file.

3. View data preview & summary statistics.

4.Click "🧠 Generate Business Insight" to:

  (i) Get AI-generated insights

  (ii) View profit trends by category

  (iii) Download the Excel report

---
🙌 Acknowledgements

Streamlit - for making data apps easy to build.

Google Gemini - for AI-driven insights.

Open-source community for tools and libraries.


