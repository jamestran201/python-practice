import click
import locale
import textwrap
import requests

from . import __version__

API_PATH = "/api/rest_v1/page/random/summary"

@click.command()
@click.option('-l', 'input_locale', default='')
@click.version_option(version=__version__)
def main(input_locale):
    """The hypermodern Python project."""
    url_to_use = url(input_locale)
    request_success, data = call_api(url_to_use)
    if not request_success:
        return

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))

def url(input_locale):
    user_locale = input_locale or get_locale()
    return "https://%s.wikipedia.org%s" % (user_locale, API_PATH)

def get_locale():
    default_locale, _ = locale.getdefaultlocale()
    return default_locale.split("_")[0]

def call_api(url):
    request_success = True
    data = {}
    with requests.get(url) as response:
        try:
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as exc:
            click.echo("An error has occurred while calling the API:")
            click.echo(exc.response.text)
            request_success = False

    return request_success, data

