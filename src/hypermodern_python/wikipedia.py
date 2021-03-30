import locale

import click
import requests

API_PATH = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language):
    url = create_url(language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as error:
        message = str(error)
        raise click.ClickException(message)


def create_url(input_locale):
    user_locale = input_locale or get_default_locale()
    return API_PATH.format(language=user_locale)


def get_default_locale():
    default_locale, _ = locale.getdefaultlocale()
    return default_locale.split("_")[0]
