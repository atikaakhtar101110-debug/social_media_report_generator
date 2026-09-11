import os
import requests
from dotenv import load_dotenv

load_dotenv()


class MetaAPI:

    def __init__(self):
        self.access_token = os.getenv("META_ACCESS_TOKEN")
        self.api_version = os.getenv(
            "META_API_VERSION",
            "v23.0"
        )

        self.base_url = (
            f"https://graph.facebook.com/{self.api_version}"
        )

    def get_campaign_insights(
        self,
        ad_account_id: str,
        date_preset: str = "last_30d"
    ):
        """
        Get advertising insights from a Meta Ad Account.
        """

        url = f"{self.base_url}/{ad_account_id}/insights"

        params = {
            "access_token": self.access_token,
            "date_preset": date_preset,
            "fields": (
                "campaign_name,"
                "impressions,"
                "reach,"
                "clicks,"
                "spend,"
                "actions"
            )
        }

        response = requests.get(
            url,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()
