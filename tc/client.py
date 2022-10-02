from typing import List

from .api import api
from .schema import Server, ProjectSummary, Project, BuildSummary, VscRootSummary, VscRoot, Build


class Client:
    def __init__(self, *args, **kwargs):
        self.api = api
        self.api.connect(*args, **kwargs)

    def server(self) -> Server:
        return Server(**self.api.get("/app/rest/server"))

    def projects(self, id=None) -> List[ProjectSummary]:
        if id:
            return Project(**self.api.get(f"/app/rest/projects/id:{id}"))
        return [ProjectSummary(**data) for data in self.api.get("/app/rest/projects")["project"]]

    def builds(self, id=None) -> List[BuildSummary]:
        if id:
            return Build(**self.api.get(f"/app/rest/builds/id:{id}"))
        return [BuildSummary(**data) for data in self.api.get("/app/rest/builds")["build"]]

    def vsc_roots(self, id=None) -> List[VscRootSummary]:
        if id:
            return VscRoot(**self.api.get(f"/app/rest/vcs-roots/id:{id}"))
        return [vcs for vcs in self.api.get("/app/rest/vcs-roots")["vcs_roots"]]
