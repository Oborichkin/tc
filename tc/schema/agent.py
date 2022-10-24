from typing import List
from pydantic import validator
from ._base import _Base, Property, Link


class AgentSummary(_Base):
    id: int
    name: str
    type_id: int


class AgentLink(Link):
    def visit(cls) -> List[AgentSummary]:
        return [AgentSummary(**data) for data in cls._api.get(cls.href)["agent"]]


class Agent(AgentSummary):
    connected: bool
    enabled: bool
    authorized: bool
    uptodate: bool
    ip: str
    # enabled_info
    # authorized_info
    properties: List[Property]
    # pool
