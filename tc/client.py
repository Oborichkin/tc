from typing import List

from .api import api
from .schema import Server, ProjectSummary, Project


class Client:
    def __init__(self, *args, **kwargs):
        self.api = api
        self.api.connect(*args, **kwargs)

    @property
    def server(self) -> Server:
        return Server(**self.api.get("/app/rest/server"))

    @property
    def projects(self) -> List[ProjectSummary]:
        return [ProjectSummary(**data) for data in self.api.get("/app/rest/projects")["project"]]

    def project(self, id):
        return Project(**self.api.get(f"/app/rest/projects/id:{id}"))
