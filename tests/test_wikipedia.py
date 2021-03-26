import pytest

from hypermodern_python import wikipedia

@pytest.mark.skip
def test_random_page_uses_given_language(mock_requests_get):
    wikipedia.call_api(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]
