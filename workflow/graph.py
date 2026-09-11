from agents.analysis_agent import AnalysisAgent
from agents.report_agent import ReportAgent


class SocialMediaWorkflow:

    def __init__(self):
        self.analysis_agent = AnalysisAgent()
        self.report_agent = ReportAgent()

    def run(self, df):

        # Step 1: Analyze data
        analyzed_data = self.analysis_agent.analyze(df)

        # Step 2: Generate Excel report
        report_path = self.report_agent.generate_report(
            analyzed_data
        )

        return {
            "data": analyzed_data,
            "report": report_path
        }
