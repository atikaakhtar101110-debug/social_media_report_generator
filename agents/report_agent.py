from tools.excel_tools import save_excel_report


class ReportAgent:

    def generate_report(self, df):
        """
        Generate the final Excel report.
        """

        file_path = save_excel_report(
            df,
            "social_media_report.xlsx"
        )

        return file_path
