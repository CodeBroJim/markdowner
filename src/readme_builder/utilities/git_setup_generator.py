# from textwrap import dedent

from src.readme_builder.utilities.base_class import BaseClass


class GitSetupGenerator(BaseClass):
    """
    This class handles the logic used to generate and save the user's
    pre-commit and pre-push files.

    This allows the user to decide if they would rather have the README.md
    generated upon git commit or git push commands.
    """

    def __init__(self) -> None:
        super().__init__()

    def get_pre_commit_template(self) -> None:
        self.get_template_file(template_name="pre-commit")

    def get_pre_push_template(self) -> None:
        self.get_template_file(template_name="pre-push")
