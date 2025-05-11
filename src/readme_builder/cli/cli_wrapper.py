import click

from typing import Any, Dict

from src.readme_builder.cli.cli import ReadmeBuilderCLI


class ReadmeBuilderCLIWrapper:

    @staticmethod
    def dispatch_generate(target: str):
        cli_instance: ReadmeBuilderCLI = ReadmeBuilderCLI()

        dispatch_map: Dict[str, Any] = {
            "readme": cli_instance.generate_readme,
            "pre-commit": cli_instance.generate_pre_commit,
            "pre-push": cli_instance.generate_pre_push,
        }

        if target in dispatch_map:
            dispatch_map[target]()
        else:
            raise click.ClickException(
                f"Unsupported generate target: {target}"
            )

    @click.command(name="generate")
    @click.argument(
        "target",
        type=click.Choice(
            ["readme", "pre-commit", "pre-push"],
            case_sensitive=False
        )
    )
    def generate_command(target):
        ReadmeBuilderCLIWrapper.dispatch_generate(target)
