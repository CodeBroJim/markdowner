from src.readme_builder.generator.readme_builder import ReadmeBuilder
from src.readme_builder.utilities.git_setup_generator import GitSetupGenerator


class ReadmeBuilderCLI:
    @staticmethod
    def generate_readme():
        """Logic to build the README.md file."""
        builder: ReadmeBuilder = ReadmeBuilder()
        builder.build_readme()

    @staticmethod
    def generate_pre_commit():
        git_helper: GitSetupGenerator = GitSetupGenerator()
        git_helper.get_pre_commit_template()

    @staticmethod
    def generate_pre_push():
        git_helper: GitSetupGenerator = GitSetupGenerator()
        git_helper.get_pre_push_template()
