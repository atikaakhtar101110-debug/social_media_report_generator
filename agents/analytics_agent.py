import pandas as pd


class AnalysisAgent:

    def analyze(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Analyze social media campaign data
        and calculate marketing KPIs.
        """

        df = df.copy()

        # CTR
        if "clicks" in df.columns and "impressions" in df.columns:
            df["ctr"] = (
                df["clicks"] / df["impressions"] * 100
            ).fillna(0)

        # CPC
        if "spend" in df.columns and "clicks" in df.columns:
            df["cpc"] = (
                df["spend"] / df["clicks"]
            ).fillna(0)

        # Conversion rate
        if "conversions" in df.columns and "clicks" in df.columns:
            df["conversion_rate"] = (
                df["conversions"] / df["clicks"] * 100
            ).fillna(0)

        # CPA
        if "spend" in df.columns and "conversions" in df.columns:
            df["cpa"] = (
                df["spend"] / df["conversions"]
            ).fillna(0)

        # Engagement rate
        if (
            "engagements" in df.columns
            and "impressions" in df.columns
        ):
            df["engagement_rate"] = (
                df["engagements"] /
                df["impressions"] * 100
            ).fillna(0)

        return df
