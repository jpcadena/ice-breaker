"""
A module for LinkedIn in the application.services package.
"""

from typing import Any

import requests
from requests import Response

from application.config import settings


def scrape_linkedin_profile(linkedin_profile_url: str) -> dict[str, Any]:
    """
    Scrape information from LinkedIn profiles,
    :param linkedin_profile_url: The URL of the LinkedIn profile
    :type linkedin_profile_url: str
    :return: The profile information
    :rtype: dict[str, Any]
    """
    header_dic: dict[str, str] = {
        "Authorization": f"Bearer {settings.PROXYCURL_API_KEY}"
    }
    response: Response = requests.get(
        str(settings.API_ENDPOINT),
        params={"url": linkedin_profile_url},
        headers=header_dic,
        timeout=settings.REQUEST_TIMEOUT,
    )
    data: dict[str, Any] = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups", []):
        for group_dict in data["groups"]:
            group_dict.pop("profile_pic_url", None)
    return data
