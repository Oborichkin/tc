import os
import pytest
from dotenv import load_dotenv

load_dotenv()

from tc.client import Client


@pytest.fixture
def client():
    yield Client(os.environ["TEAMCITY_URL"], os.environ["TEAMCITY_TOKEN"])
