import os
import pytest
from dotenv import load_dotenv

load_dotenv()

from tc.client import Client
from .api_mock import ApiMock


@pytest.fixture
def client(monkeypatch):
    client = Client("https://teamcity.com", "SUPA_SECRET_TOKEN")
    monkeypatch.setattr(client, "api", ApiMock())
    yield client
