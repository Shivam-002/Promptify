from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:

    def structure_task(self, agent, input_prompt):
        return Task(
            description=dedent(
                f"""
            Use your expertise to structure the given input prompt in a way that will guide the team to generate high-quality responses.
            Analyze the input prompt and create a clear and concise structure that will help the team understand the task.
            Use Symbols and Keywords to create a structured prompt that will guide the team to generate accurate and informative responses.

            Input Prompt: {input_prompt}
        """
            ),
            expected_output=dedent(
                f"""
            The structured prompt should be clear, concise, and easy to understand.
            It should include symbols and keywords that will guide the team to generate high-quality responses.
            The structure should be well-organized and provide a clear direction for the team to follow.
        """
            ),
            agent=agent,
        )

    def keyword_generation(self, agent, input_prompt):
        return Task(
            description=dedent(
                f"""
            Create a list of relevant keywords based on the given input prompt.
            Use the tools and your expertise to identify high-impact keywords that will guide the team to generate accurate and informative responses.
            Response should be in proper format and structure.

            Input Prompt: {input_prompt}
        """
            ),
            expected_output=dedent(
                f"""
            The list of keywords should be relevant to the input prompt and help guide the team to generate high-quality responses.
            The keywords should be well-researched and provide valuable insights for the team to consider.
            The response should be in a proper format and structure that is easy to understand and use.
        """
            ),
            agent=agent,
        )

    def context_analysis(self, agent, input_prompt, context=None):
        return Task(
            description=dedent(
                f"""
            Analyze the input prompt against the additional context provided by the User.
            Identify key details and context that will enhance the quality of the generated content.
            Provide relevant information that will help guide the team to generate accurate and informative responses.
            Note: If context is not provided, analyze the prompt based on the given input. 

            Input Prompt: {input_prompt}
            Context: {context}
        """
            ),
            expected_output=dedent(
                f"""
            The analysis should provide relevant information that will help guide the team to generate accurate and informative responses.
            Key details and context should be identified and highlighted to enhance the quality of the generated content.
            The response should be clear, concise, and easy to understand.
        """
            ),
            agent=agent,
        )

    def ethics_check(self, agent, input_prompt):
        return Task(
            description=dedent(
                f"""
            Analyze the input prompt and check for any ethical concerns or issues.
            Identify any sensitive topics or information that may need to be addressed or avoided.
            Provide guidance on how to handle the prompt in an ethical manner.

            Input Prompt: {input_prompt}
        """
            ),
            expected_output=dedent(
                f"""
            The analysis should identify any ethical concerns or issues in the input prompt.
            Sensitive topics or information should be highlighted and guidance provided on how to handle them in an ethical manner.
            The response should be clear, concise, and provide actionable recommendations.
        """
            ),
            agent=agent,
        )

    def creativity_check(self, agent, input_prompt):
        return Task(
            description=dedent(
                f"""
            Analyze the input prompt and check for any creative opportunities or ideas.
            Identify areas where the team can add creativity or innovation to the responses.
            Provide suggestions on how to enhance the prompt with creative elements.

            Input Prompt: {input_prompt}
        """
            ),
            expected_output=dedent(
                f"""
            The analysis should identify creative opportunities or ideas in the input prompt.
            Suggestions should be provided on how to enhance the prompt with creative elements and innovative solutions.
            The response should be clear, concise, and provide actionable recommendations.
        """
            ),
            agent=agent,
        )

    def markdown_check(self, agent, input_prompt):
        return Task(
            description=dedent(
                f"""
            Check the input prompt for any markdown formatting issues.
            Identify any missing or incorrect markdown syntax and provide corrections.
            Ensure that the prompt is properly formatted and structured.

            Input Prompt: {input_prompt}
        """
            ),
            expected_output=dedent(
                f"""
            The analysis should identify any markdown formatting issues in the input prompt.
            Corrections should be provided for any missing or incorrect markdown syntax.
            The response should ensure that the prompt is properly formatted and structured.
        """
            ),
            agent=agent,
        )
