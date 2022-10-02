import json
import requests as r

from .responses import *


class ApiMock:

    @staticmethod
    def get(url, *args, **kwargs):
        if url == "/app/rest/server":
            return server
        elif url == "/app/rest/projects":
            return projects
        elif url.startswith("/app/rest/projects/id:"):
            return project
        elif url == "/app/rest/builds":
            return builds
