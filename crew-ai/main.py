import os
from crewai import Crew
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()


class CustomCrew:
    def __init__(self, input_prompt, context=None):
        self.input_prompt = input_prompt
        self.context = context

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        prompt_designer = agents.prompt_designer()
        keyword_specalist = agents.keyword_specialist()
        context_analyst = agents.context_analyst()
        ethics_advisor = agents.ethics_advisor()
        creative_director = agents.creative_director()
        markdown_specialist = agents.markdown_specialist()

        # Custom tasks include agent name and variables as input
        task_structure_prompt = tasks.structure_task(
            prompt_designer,
            self.input_prompt,
        )

        task_keyword_generation = tasks.keyword_generation(
            keyword_specalist,
            self.input_prompt,
        )

        task_context_analysis = tasks.context_analysis(
            context_analyst,
            self.input_prompt,
            self.context,
        )

        task_ethics_check = tasks.ethics_check(
            ethics_advisor,
            self.input_prompt,
        )

        task_markdown_check = tasks.markdown_check(
            markdown_specialist,
            self.input_prompt,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                prompt_designer,
                keyword_specalist,
                context_analyst,
                ethics_advisor,
                creative_director,
                markdown_specialist,
            ],
            tasks=[
                task_structure_prompt,
                task_keyword_generation,
                task_context_analysis,
                task_ethics_check,
                task_markdown_check,
            ],
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    input_prompt = input("Enter your prompt: ")
    context = input("Enter additional context (optional): ")
    custom_crew = CustomCrew(input_prompt, context)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
