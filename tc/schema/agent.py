from typing import List
from pydantic import validator
from ._base import _Base, Property


class AgentSummary(_Base):
    id: int
    name: str
    type_id: int


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
