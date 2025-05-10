import click

from src.cli.cli import ReadmeBuilderCLI


class ReadmeBuilderCLIWrapper:

    @click.command(name="build-readme")
    def build_readme_command():
        cli_instance: ReadmeBuilderCLI = ReadmeBuilderCLI()
        cli_instance.build_readme()
