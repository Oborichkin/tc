import json
import requests as r

from .responses import (
    server,
    projects,
    project,
    builds,
    vcs_root,
    vcs_root_instances,
    vcs_roots,
    vcs_root_instance,
    build_types,
    build_type,
    agent,
    agents,
)


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
        elif url == "/app/rest/vcs-root-instances":
            return vcs_root_instances
        elif url.startswith("/app/rest/vcs-root-instances/id:"):
            return vcs_root_instance
        elif url == "/app/rest/buildTypes":
            return build_types
        elif url.startswith("/app/rest/buildTypes/id:"):
            return build_type
        elif url == "/app/rest/agents":
            return agents
        elif url.startswith("/app/rest/agents/id:"):
            return agent
