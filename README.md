# Social Media Report Generator

A Streamlit application that accepts campaign data in CSV or Excel format, runs an analysis workflow, and produces a downloadable Excel report.

## Features

- Upload `.csv` and `.xlsx` campaign datasets.
- Preview the uploaded raw data.
- Run the analysis and report-generation workflow.
- Review the analyzed data in the app.
- Download the generated Excel workbook.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Render

A `render.yaml` blueprint is included for a Streamlit web service. If the analysis/report agents call an external LLM, add the required API key (for example, `OPENAI_API_KEY`) in the hosting dashboard.

## Input

Upload a CSV or Excel file containing the campaign metrics expected by the analysis workflow. Check the agent implementation for the exact required column names and data types.

## Development notes

- Validate uploaded schemas and handle empty or malformed files before processing.
- Treat generated metrics as analytical outputs; verify formulas and assumptions against the source data.
- Avoid uploading personal or confidential campaign data unless the deployment has appropriate access controls.
