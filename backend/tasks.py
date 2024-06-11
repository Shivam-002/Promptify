from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:

    def prompt_input_question_list(self, agent, input_prompt):
        return Task(
            description=dedent(
                f"""
                Generate a list of questions that a good, professional prompt should cover based
                on the input prompt.

                You must use the input prompt while researching.
                
                Input Prompt: {input_prompt}
        """
            ),
            expected_output=dedent(
                f"""
                [Tasks]
                A list of questions.
        """
            ),
            agent=agent,
            async_execution=True,
        )

    def prompt_output_question_list(self, agent, input_prompt):
        return Task(
            description=dedent(
                f"""
                Research and generate a structure, format that the final output should have
                based on the input prompt.
                
                Input Prompt: {input_prompt}
        """
            ),
            expected_output=dedent(
                f"""
                [Output]
                Final Answer Structure.
        """
            ),
            agent=agent,
            async_execution=True,
        )

    def prompt_research(self, agent, input_prompt, context=None):
        return Task(
            description=dedent(
                f"""
                Find relevant topics, information, key points, and context on the given input prompt.
                
                Input Prompt: {input_prompt}
                Context: {context}
        """
            ),
            expected_output=dedent(
                f"""
                A well-structured output properly formatted with relevant information.
        """
            ),
            agent=agent,
            async_execution=True,
        )

    def prompt_build(
        self, agent, task_input_question, task_output_question, task_research
    ):
        return Task(
            description=dedent(
                f"""
                Build a prompt using the information gathered by your team.
        """
            ),
            expected_output=dedent(
                f"""
                A well-structured, clear, concise prompt build using markdown format.
        """
            ),
            agent=agent,
            context=[task_input_question, task_output_question, task_research],
        )

    def structure_task(self, agent, input_prompt, context=None):
        return Task(
            description=dedent(
                f"""
                    Create a plan to generate a prompt from the given input prompt and context.

                    The plan or points should guide the team to generate a descriptive prompt 
                    and should not provide plan to answering the input prompt.

                    Example: If the input prompt is "Prompt for nature image generation"
                    You should provide a plan that will create a indepth plan to generate a
                    prompt for nature image generation.
                
                Input Prompt: {input_prompt}
                Context: {context}
        """
            ),
            expected_output=dedent(
                f"""
                A well-structured plan that is build around the input prompt and context
                (if provided).

                The plan should be more about providing a clear and concise format that
                will guide the team to generate elaborated responses about the input prompt.
        """
            ),
            agent=agent,
        )

    def prompt_generation(self, agent, input_prompt, context=None):
        return Task(
            description=dedent(
                f"""
                Use the plan to create a well-structured, clear, concise and engaging 
                prompt that best suits the input prompt & context of the task.

                You have to build a long and more descriptive prompt based on the 
                input prompt & context and build instructions from the plan.

                Keep in mind you are building a prompt not an answer to the input prompt.

                Your response should be more about rephrasing the input prompt and 
                should not contains the plan outline.

                It should also not contain the initial prompt as title and should 
                contain instructions on achieving the goal.

                Don't answer the input prompt, just build a prompt around it.
                
                Input Prompt: {input_prompt}
                Context: {context}
        """
            ),
            expected_output=dedent(
                f"""
                A well-structured, clear, concise and engaging prompt build around the
                input prompt, context.

                Response that is not the answer of the input prompt but a prompt that
                is more descriptive about the input prompt.
        """
            ),
            agent=agent,
        )

    def markdown_formatting(self, agent):
        return Task(
            description=dedent(
                f"""
                Use your expertise to format the response in markdown syntax. Use proper 
                headings, bullet points, (extra) new lines and other markdown formatting 
                techniques to make the response more readable and structured.

        """
            ),
            expected_output=dedent(
                f"""
                A well-formatted response in markdown syntax.
        """
            ),
            agent=agent,
        )
