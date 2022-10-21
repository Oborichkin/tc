from typing import List, Union

from .api import api
from .schema import Server, ProjectSummary, Project, BuildSummary, VcsRootSummary, VcsRoot, Build, BuildType


class Client:
    def __init__(self, *args, **kwargs):
        self.api = api
        self.api.connect(*args, **kwargs)

    def server(self) -> Server:
        return Server(**self.api.get("/app/rest/server"))

    def projects(self, id=None) -> Union[List[ProjectSummary], Project]:
        if id:
            return Project(**self.api.get(f"/app/rest/projects/id:{id}"))
        return [ProjectSummary(**data) for data in self.api.get("/app/rest/projects")["project"]]

    def builds(self, id=None) -> List[BuildSummary]:
        if id:
            return Build(**self.api.get(f"/app/rest/builds/id:{id}"))
        return [BuildSummary(**data) for data in self.api.get("/app/rest/builds")["build"]]

    def build_types(self, id=None) -> List[BuildType]:
        if id:
            return BuildType(**self.api.get(f"/app/rest/buildTypes/id:{id}"))
        return [BuildType(**data) for data in self.api.get("/app/rest/buildTypes")["buildType"]]

    def vsc_roots(self, id=None) -> Union[List[VcsRootSummary], VcsRoot]:
        if id:
            return VcsRoot(**self.api.get(f"/app/rest/vcs-roots/id:{id}"))
        return [vcs for vcs in self.api.get("/app/rest/vcs-roots")["vcs-root"]]
