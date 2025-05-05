import streamlit as st
import pandas as pd
from cleaner import clean_data

st.title("🧹 Data Cleaning Automation Tool")

uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df)

    if st.button("🧼 Clean Data"):
        cleaned_df = clean_data(df)
        st.subheader("✅ Cleaned Data")
        st.dataframe(cleaned_df)

        # Download button
        st.download_button("⬇ Download Cleaned CSV", cleaned_df.to_csv(index=False), "cleaned_data.csv", "text/csv")
