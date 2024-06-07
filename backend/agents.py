from crewai import Agent
from textwrap import dedent
from crewai import Agent
import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.search_tool import SearchTools

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm_model = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.5,
)


class CustomAgents:

    def prompt_designer(self):
        return Agent(
            role="Professional Prompt Designer",
            backstory=dedent(
                f"""
                    One of the best prompt designer in the world with a deep understanding 
                    of prompt engineering.

                    You have expertise in creating high-quality prompts for AI models.
                """
            ),
            goal=dedent(
                f"""
                    Generate a small plan that is based on the given input prompt and
                    context.

                    The plan will guilde the LLM/AI model to generate a professional 
                    prompt.

                    The plan cover points to generate a prompt that is well-structured,
                    clear, concise and descriptive.

                    The plan is not for answering the input prompt but to generate a
                    professional prompt.

                """
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )

    def prompt_builder(self):
        return Agent(
            role="Prompt Builder",
            backstory=dedent(
                f"""
                You are an expert in creating high-quality prompts. You have a deep 
                understanding of prompt engineering.

                You have expertise in creating high-quality prompts for AI models.

        """
            ),
            goal=dedent(
                f"""
                With the provided plan, generate a more descriptive prompt that is
                well-structured, clear, concise and descriptive.

                The prompt should be more about describing the input prompt in a
                well-structured way not to answer it.

                Use this words(not compulsory):
                [provide, cover, explain, describe, give, answer, write, response,
                 generate, create, build, develop, construct, compose, make, define,
                 design, etc...]
        """
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )

    def markdown_specialist(self):
        return Agent(
            role="Markdown Specialist",
            backstory=dedent(
                f"""
                    You have expertise in markdown formatting and syntax. You're familiar 
                    with different markdown elements and their usage in creating structured
                    and visually appealing content.
        """
            ),
            goal=dedent(
                f"""
                Convert the generated content into markdown format, ensuring proper formatting and structure.
                Use markdown syntax to create headings, lists, links,colors and other elements to make the content
                visually appealing and easy to read.

                Also use advanced markdown features like tables, images, and code blocks where necessary.
        """
            ),
            allow_delegation=False,
            verbose=True,
            llm=llm_model,
        )
