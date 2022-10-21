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
        elif url == "/app/rest/vcs-roots":
            return vcs_roots
        elif url.startswith("/app/rest/vcs-roots/id:"):
            return vcs_root
        elif url.startswith("/app/rest/vcs-root-instances/id:"):
            return vcs_root_instances
