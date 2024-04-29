"""
A module for custom chains in the application-chains package.
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from application.schemas.output_parsers import (
    ice_breaker_parser,
    summary_parser,
    toi_parser,
)

llm: ChatOpenAI = ChatOpenAI(temperature=0)
llm_creative: ChatOpenAI = ChatOpenAI(temperature=1)


def get_summary_chain() -> LLMChain:
    """
    Get the summary chain
    :return: The LLM chain for summary generation
    :rtype: LLMChain
    """
    summary_template: str = """
         given the information about a person from linkedin {information},
          and twitter posts {twitter_posts} I want you to create:
         1. a short summary
         2. two interesting facts about them
         \n{format_instructions}
     """
    summary_prompt_template: PromptTemplate = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    return LLMChain(llm=llm, prompt=summary_prompt_template)


def get_interests_chain() -> LLMChain:
    """
    Get interests chain
    :return: The LLM chain for interests generation
    :rtype: LLMChain
    """
    interesting_facts_template: str = """
         given the information about a person from linkedin {information},
          and twitter posts {twitter_posts} I want you to create:
         3 topics that might interest them
        \n{format_instructions}
     """
    interesting_facts_prompt_template: PromptTemplate = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=interesting_facts_template,
        partial_variables={
            "format_instructions": toi_parser.get_format_instructions()
        },
    )
    return LLMChain(llm=llm, prompt=interesting_facts_prompt_template)


def get_ice_breaker_chain() -> LLMChain:
    """
    Get the chain for interest
    :return: The LLM chain for interest
    :rtype: LLMChain
    """
    ice_breaker_template: str = """
         given the information about a person from linkedin {information}, and
          twitter posts {twitter_posts} I want you to create:
         2 creative Ice breakers with them that are derived from their activity
          on Linkedin and twitter, preferably on latest tweets
        \n{format_instructions}
     """
    ice_breaker_prompt_template: PromptTemplate = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=ice_breaker_template,
        partial_variables={
            "format_instructions": ice_breaker_parser.get_format_instructions()
        },
    )
    return LLMChain(llm=llm_creative, prompt=ice_breaker_prompt_template)
