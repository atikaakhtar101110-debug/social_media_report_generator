import streamlit as st
import pandas as pd

from workflow.graph import SocialMediaWorkflow


st.set_page_config(
    page_title="Social Media Report Generator",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Social Media Report Generator")

st.write(
    "Automatically analyze social media campaign "
    "performance and generate an Excel report."
)


uploaded_file = st.file_uploader(
    "Upload campaign data for testing",
    type=["csv", "xlsx"]
)


if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    if st.button("Generate Report"):

        workflow = SocialMediaWorkflow()

        result = workflow.run(df)

        st.success("Report generated successfully!")

        st.subheader("Analyzed Data")
        st.dataframe(result["data"])

        with open(result["report"], "rb") as file:

            st.download_button(
                label="Download Excel Report",
                data=file,
                file_name="social_media_report.xlsx",
                mime=(
                    "application/vnd.openxmlformats-officedocument"
                    ".spreadsheetml.sheet"
                )
            )
            
