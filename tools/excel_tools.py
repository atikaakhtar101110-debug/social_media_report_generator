from pathlib import Path
import pandas as pd


def save_excel_report(
    df: pd.DataFrame,
    filename: str = "social_media_report.xlsx"
) -> str:
    """
    Save the final social media report as an Excel file.
    """

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / filename

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            sheet_name="Social Media Report",
            index=False
        )

    return str(file_path)
