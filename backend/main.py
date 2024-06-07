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
        custom_agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        prompt_designer = custom_agents.prompt_designer()
        prompt_builder = custom_agents.prompt_builder()
        markdown_specialist = custom_agents.markdown_specialist()

        # Custom tasks include agent name and variables as input
        task_structure_prompt = tasks.structure_task(
            prompt_designer,
            self.input_prompt,
        )

        task_prompt_generation = tasks.prompt_generation(
            prompt_builder,
            self.input_prompt,
            self.context,
        )

        task_markdown_check = tasks.markdown_check(
            markdown_specialist,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                prompt_designer,
                prompt_builder,
                # markdown_specialist,
            ],
            tasks=[
                task_structure_prompt,
                task_prompt_generation,
                # task_markdown_check,
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


def promptify_prompt(input_prompt, context=None):
    custom_crew = CustomCrew(input_prompt, context)
    result = custom_crew.run()
    return result
