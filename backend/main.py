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
        custom_agents = CustomAgents(self.input_prompt)
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        prompt_engineer = custom_agents.prompt_engineer()
        prompt_researcher = custom_agents.prompt_researcher()
        prompt_builder = custom_agents.prompt_builder()

        task_input_question_list = tasks.prompt_input_question_list(
            prompt_engineer,
            self.input_prompt,
        )

        task_output_question_list = tasks.prompt_output_question_list(
            prompt_engineer,
            self.input_prompt,
        )

        task_prompt_research = tasks.prompt_research(
            prompt_researcher,
            self.input_prompt,
            self.context,
        )

        task_builder_prompt = tasks.prompt_build(
            prompt_builder,
            task_input_question_list,
            task_output_question_list,
            task_prompt_research,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                prompt_engineer,
                prompt_researcher,
                prompt_builder,
            ],
            tasks=[
                task_input_question_list,
                task_output_question_list,
                task_prompt_research,
                task_builder_prompt,
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


def promptify_prompt(input_prompt, context=None):
    custom_crew = CustomCrew(input_prompt, context)
    result = custom_crew.run()
    return result
