import locale

import click
import requests
from pydantic import BaseModel

API_PATH = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


class Page(BaseModel):
    title: str
    extract: str


def random_page(language: str) -> Page:
    url = create_url(language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return Page(**response.json())
    except (requests.exceptions.RequestException, TypeError) as error:
        message = str(error)
        raise click.ClickException(message)


def create_url(input_locale: str) -> str:
    user_locale = input_locale or get_default_locale()
    return API_PATH.format(language=user_locale)


def get_default_locale() -> str:
    default_locale, _ = locale.getdefaultlocale()
    if not default_locale:
        return "en"

    return default_locale.split("_")[0]
