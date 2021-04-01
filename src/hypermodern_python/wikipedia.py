"""Client for the Wikipedia REST API, version 1."""
import locale

import click
import requests
from pydantic import BaseModel

API_PATH = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


class Page(BaseModel):
    """Page resource.

    Attributes:
        title: The title of the Wikipedia page.
        extract: A plain text summary.
    """

    title: str
    extract: str


def random_page(language: str) -> Page:
    """Return a random page.

    Performs a GET request to the /page/random/summary endpoint.

    Args:
        language: The Wikipedia language edition. By default, the English
            Wikipedia is used ("en").

    Returns:
        A page resource.

    Raises:
        ClickException: The HTTP request failed or the HTTP response
            contained an invalid body.

    Example:
        >>> from hypermodern_python import wikipedia
        >>> page = wikipedia.random_page(language="en")
        >>> bool(page.title)
        True
    """
    url = create_url(language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return Page(**response.json())
    except (requests.exceptions.RequestException, TypeError) as error:
        message = str(error)
        raise click.ClickException(message)


def create_url(input_locale: str) -> str:
    """Create a url with the given locale."""
    user_locale = input_locale or get_default_locale()
    return API_PATH.format(language=user_locale)


def get_default_locale() -> str:
    """Get system default locale."""
    default_locale, _ = locale.getdefaultlocale()
    if not default_locale:
        return "en"

    return default_locale.split("_")[0]
