import pendulum
from datetime import datetime
from typing import Optional, List
from pydantic import validator
from ._base import _Base, Property


class GroupSummary(_Base):
    key: str
    name: str
    description: Optional[str]


class UserSummary(_Base):
    username: str
    name: str
    id: int


class Group(GroupSummary):
    parent_groups: List[GroupSummary]
    child_groups: List[GroupSummary]
    users: List[UserSummary]
    properties: List[Property]
    # roles


class User(UserSummary):
    email: str
    last_login: datetime
    properties: List[Property]
    # roles
    # groups

    @validator("last_login", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)
