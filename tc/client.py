from typing import List, Union

from .api import api
from .schema import (
    AgentSummary,
    Agent,
    AgentPoolSummary,
    AgentPool,
    Server,
    ProjectSummary,
    Project,
    BuildSummary,
    VcsRootSummary,
    VcsRoot,
    Build,
    BuildTypeSummary,
    BuildType,
    VcsRootInstance,
    VcsRootInstanceSummary,
)


class Client:
    def __init__(self, *args, **kwargs):
        self.api = api
        self.api.connect(*args, **kwargs)

    def server(self) -> Server:
        return Server(**self.api.get("/app/rest/server"))

    def agents(self, id=None) -> Union[Agent, List[AgentSummary]]:
        if id:
            return Agent(**self.api.get(f"/app/rest/agents/id:{id}"))
        return [AgentSummary(**data) for data in self.api.get("/app/rest/agents")["agent"]]

    def agent_pools(self, id=None) -> Union[AgentPool, List[AgentPoolSummary]]:
        if id:
            return AgentPool(**self.api.get(f"/app/rest/agentPools/id:{id}"))
        return [AgentPoolSummary(**data) for data in self.api.get("/app/rest/agentPools")["agentPool"]]

    def projects(self, id=None) -> Union[List[ProjectSummary], Project]:
        if id:
            return Project(**self.api.get(f"/app/rest/projects/id:{id}"))
        return [ProjectSummary(**data) for data in self.api.get("/app/rest/projects")["project"]]

    def builds(self, id=None) -> List[BuildSummary]:
        if id:
            return Build(**self.api.get(f"/app/rest/builds/id:{id}"))
        return [BuildSummary(**data) for data in self.api.get("/app/rest/builds")["build"]]

    def build_types(self, id=None) -> Union[List[BuildTypeSummary], BuildType]:
        if id:
            return BuildType(**self.api.get(f"/app/rest/buildTypes/id:{id}"))
        return [BuildTypeSummary(**data) for data in self.api.get("/app/rest/buildTypes")["buildType"]]

    def vsc_roots(self, id=None) -> Union[List[VcsRootSummary], VcsRoot]:
        if id:
            return VcsRoot(**self.api.get(f"/app/rest/vcs-roots/id:{id}"))
        return [VcsRootSummary(**vcs) for vcs in self.api.get("/app/rest/vcs-roots")["vcs-root"]]

    def vcs_root_instances(self, id=None) -> Union[List[VcsRootInstanceSummary], VcsRootInstance]:
        if id:
            return VcsRootInstance(**self.api.get(f"/app/rest/vcs-root-instances/id:{id}"))
        return [
            VcsRootInstanceSummary(**vcs) for vcs in self.api.get("/app/rest/vcs-root-instances")["vcs-root-instance"]
        ]
