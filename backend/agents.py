from crewai import Agent
from textwrap import dedent
from crewai import Agent
import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.search_tool import SearchTools
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm_model = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.5,
)


class CustomAgents:

    def __init__(self, input_prompt):
        self.input_prompt = input_prompt

    def prompt_engineer(self):
        return Agent(
            role="Prompt Engineer",
            backstory=dedent(
                f"""
                    You are a professional prompt engineer with expertise in understanding and
                    working with prompts.

                    You have a lot of experience in prompt building, designing, and structuring. 
                """
            ),
            goal=dedent(
                f"""
                    Use your expertise to complete the task as per the instructions.
                """
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )

    def prompt_researcher(self):
        return Agent(
            role="Prompt Researcher",
            backstory=dedent(
                f"""
                    You are a professional prompt researcher with expertise in finding relevant 
                    information on a wide range of prompts.

                    You have experience in conducting in-depth research and analysis to 
                    gather valuable insights and data on prompts.
                """
            ),
            goal=dedent(
                f"""
                    To find relevant topics, information, data, keywords, key points, and 
                    context on the given input prompt.
                """
            ),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )

    def prompt_builder(self):
        return Agent(
            role="Prompt Builder",
            backstory=dedent(
                f"""
                    You are a professional prompt builder with expertise in creating high-quality 
                    prompts for AI models.

                    You have experience in generating well-structured, clear, concise, and 
                    descriptive prompts.
                """
            ),
            goal=dedent(
                f"""
                    Generate a high-quality,descriptive and professional prompt that is 
                    well-structured, clear and concise based on the information gathered
                    by the team.
                """
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )

    # def prompt_builder(self):
    #     return Agent(
    #         role="Prompt Builder",
    #         backstory=dedent(
    #             f"""
    #             You are an expert in creating high-quality prompts. You have a deep 
    #             understanding of prompt engineering.

    #             You have expertise in creating high-quality prompts for AI models.

    #     """
    #         ),
    #         goal=dedent(
    #             f"""
    #             With the provided plan, generate a more descriptive prompt that is
    #             well-structured, clear, concise and descriptive.

    #             The prompt should be more about describing the input prompt in a
    #             well-structured way not to answer it.

    #             Use this words(not compulsory):
    #             [provide, cover, explain, describe, give, answer, write, response,
    #              generate, create, build, develop, construct, compose, make, define,
    #              design, etc...]
    #     """
    #         ),
    #         allow_delegation=False,
    #         verbose=True,
    #         llm=llm_model,
    #     )


