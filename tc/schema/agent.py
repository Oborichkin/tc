from datetime import datetime

import pendulum
from typing import List, TYPE_CHECKING
from pydantic import validator
from ._base import _Base, Property, Link

if TYPE_CHECKING:
    from .user import UserSummary
    from .project import ProjectSummary


class AgentSummary(_Base):
    id: int
    name: str
    type_id: int


class AgentPoolSummary(_Base):
    id: int
    name: str


class AgentLink(Link):
    def visit(cls) -> List[AgentSummary]:
        return [AgentSummary(**data) for data in cls._api.get(cls.href)["agent"]]


class Comment(_Base):
    timestamp: datetime
    text: str
    user: "UserSummary"

    @validator("timestamp", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class Info(_Base):
    status: bool
    comment: Comment


class Agent(AgentSummary):
    connected: bool
    enabled: bool
    authorized: bool
    uptodate: bool
    ip: str
    enabled_info: Info
    authorized_info: Info
    properties: List[Property]
    pool: AgentPoolSummary

    @validator("properties", pre=True)
    def property_list(cls, value):
        return value.get("property", [])


class AgentPool(AgentPoolSummary):
    projects: List["ProjectSummary"]
    agents: List[AgentSummary]

    @validator("projects", pre=True)
    def project_list(cls, value):
        return value.get("project", [])

    @validator("agents", pre=True)
    def agent_list(cls, value):
        return value.get("agent", [])
