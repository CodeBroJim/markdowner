import click

from readme_builder.cli.cli_wrapper import ReadmeBuilderCLIWrapper


@click.group(invoke_without_command=True)
@click.option(
    "--generate", "-g",
    type=click.Choice(
        ["readme", "pre-commit", "pre-push"],
        case_sensitive=False
    ),
    help="Generate a supported file (readme, pre-commit, pre-push)."
)
@click.pass_context
def cli(ctx, generate):
    if generate:
        ReadmeBuilderCLIWrapper.dispatch_generate(generate)
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


cli.add_command(ReadmeBuilderCLIWrapper.generate_command)

if __name__ == "__main__":
    cli()
