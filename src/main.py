import click

from src.cli.cli_wrapper import ReadmeBuilderCLIWrapper


@click.group()
def cli():
    pass


cli.add_command(ReadmeBuilderCLIWrapper.build_readme_command)

if __name__ == "__main__":
    cli()
