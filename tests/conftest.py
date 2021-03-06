import os

import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"


@pytest.fixture
def release_dict():
    return {
        "name": "A new hope",
        "descriptionHTML": "<p>yay</p>",
        "url": "https://example.com",
        "tagName": "1.0.0",
        "publishedAt": "2000-01-01",
        "isDraft": False,
    }


@pytest.fixture
def github_payload(release_dict):
    return {"data": {"repository": {"releases": {"nodes": [release_dict]}}}}


@pytest.fixture(autouse=True)
def env():
    old_env = os.environ.copy()
    os.environ.pop("SPHINX_GITHUB_CHANGELOG_TOKEN", None)
    yield os.environ
    os.environ.clear()
    os.environ.update(old_env)
