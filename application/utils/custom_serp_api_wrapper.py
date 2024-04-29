"""
A module for custom serp api wrapper in the application.utils package.
"""

from typing import Any

from langchain.utilities import SerpAPIWrapper


class CustomSerpAPIWrapper(SerpAPIWrapper):  # type: ignore
    """
    Custom Serp API wrapper class
    """

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def _process_response(res: dict[str, Any]) -> str:
        """Process response from SerpAPI."""
        if "error" in res:
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box" in res and "answer" in res["answer_box"].keys():
            answer = res["answer_box"]["answer"]
        elif "answer_box" in res and "snippet" in res["answer_box"].keys():
            answer = res["answer_box"]["snippet"]
        elif (
            "answer_box" in res
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            answer = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res
            and "game_spotlight" in res["sports_results"].keys()
        ):
            answer = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res
            and "description" in res["knowledge_graph"].keys()
        ):
            answer = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            answer = res["organic_results"][0]["link"]
        else:
            answer = "No good search result found"
        return str(answer)


def get_profile_url(name: str) -> str:
    """
    Searches for LinkedIn or Twitter Profile Page
    :param name: The name of the profile to search for
    :type name: str
    :return: The URL of the profile
    :rtype: str
    """
    search: CustomSerpAPIWrapper = CustomSerpAPIWrapper()
    res: str = search.run(f"{name}")
    return res
