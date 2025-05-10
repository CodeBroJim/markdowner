from src.readme_builder.readme_builder import ReadmeBuilder


class ReadmeBuilderCLI:
    @staticmethod
    def build_readme():
        """Logic to build the README.md file."""
        builder = ReadmeBuilder()
        builder.build_readme()
