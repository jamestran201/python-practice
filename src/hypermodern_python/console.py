import textwrap

import click

from . import __version__
from . import wikipedia


@click.command()
@click.option("--language", "-l", "input_locale", default="")
@click.version_option(version=__version__)
def main(input_locale: str) -> None:
    """The hypermodern Python project."""

    page = wikipedia.random_page(input_locale)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
