import click

from typing import Any, Dict

from readme_builder.cli.cli import ReadmeBuilderCLI


class ReadmeBuilderCLIWrapper:

    @staticmethod
    def dispatch_generate(target: str):
        cli_instance: ReadmeBuilderCLI = ReadmeBuilderCLI()

        dispatch_map: Dict[str, Any] = {
            "context": cli_instance.generate_context,
            "readme": cli_instance.generate_readme,
            "pre-commit": cli_instance.get_static_pre_commit,
            "pre-push": cli_instance.get_static_pre_push,
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
            ["context", "pre-commit", "pre-push", "readme",],
            case_sensitive=False
        )
    )
    def generate_command(target):
        ReadmeBuilderCLIWrapper.dispatch_generate(target)
