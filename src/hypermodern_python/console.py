import click
import textwrap

from . import __version__, wikipedia


@click.command()
@click.option("--language", "-l", "input_locale", default="")
@click.version_option(version=__version__)
def main(input_locale):
    """The hypermodern Python project."""

    data = wikipedia.random_page(input_locale)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
