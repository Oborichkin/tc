from typing import List
from pydantic import validator
from ._base import _Base
from .agent import AgentSummary
from .project import ProjectSummary


class AgentPoolSummary(_Base):
    id: int
    name: str


class AgentPool(AgentPoolSummary):
    projects: List[ProjectSummary]
    agents: List[AgentSummary]

    @validator("projects", pre=True)
    def property_list(cls, value):
        return value.get("project", [])

    @validator("agents", pre=True)
    def project_list(cls, value):
        return value.get("agent", [])
