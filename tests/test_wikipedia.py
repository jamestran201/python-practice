from unittest.mock import Mock

import click
import pytest

from hypermodern_python import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get):
    page = wikipedia.random_page("en")
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page("en")


def test_create_url_with_specific_locale():
    got = wikipedia.create_url("fr")
    want = wikipedia.API_PATH.format(language="fr")

    assert got == want


def test_create_url_with_default_locale(mocker):
    mock = mocker.patch("hypermodern_python.wikipedia.get_default_locale")
    mock.return_value = "jp"

    got = wikipedia.create_url("")
    want = wikipedia.API_PATH.format(language="jp")

    assert got == want
