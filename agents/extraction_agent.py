import pandas as pd


class ExtractionAgent:
    """
    Extract useful social media campaign metrics
    from the raw response returned by the Meta API.
    """

    def extract(self, meta_response: dict) -> pd.DataFrame:
        """
        Convert Meta API response into a pandas DataFrame.
        """

        if not meta_response:
            raise ValueError("Meta API response is empty.")

        data = meta_response.get("data", [])

        if not data:
            raise ValueError("No campaign data found.")

        rows = []

        for campaign in data:

            row = {
                "campaign_name": campaign.get(
                    "campaign_name", ""
                ),
                "impressions": self._to_number(
                    campaign.get("impressions", 0)
                ),
                "reach": self._to_number(
                    campaign.get("reach", 0)
                ),
                "clicks": self._to_number(
                    campaign.get("clicks", 0)
                ),
                "spend": self._to_number(
                    campaign.get("spend", 0)
                ),
            }

            # Extract conversions from Meta actions
            row["conversions"] = self._extract_conversions(
                campaign.get("actions", [])
            )

            rows.append(row)

        return pd.DataFrame(rows)

    @staticmethod
    def _to_number(value):
        """Convert API values to numbers."""

        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    @staticmethod
    def _extract_conversions(actions):
        """
        Extract conversion-related actions from
        the Meta actions array.
        """

        conversion_types = {
            "purchase",
            "lead",
            "complete_registration",
            "offsite_conversion",
        }

        total = 0.0

        for action in actions:

            action_type = action.get("action_type")
            value = action.get("value", 0)

            if action_type in conversion_types:

                try:
                    total += float(value)
                except (TypeError, ValueError):
                    pass

        return total
