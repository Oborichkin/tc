from datetime import datetime
from typing import Optional, Any

import pendulum
from pydantic import BaseModel, PrivateAttr, validator

from ..api import API, api
from ..utils import to_camel


class _Base(BaseModel):
    _api: API = PrivateAttr()
    href: Optional[str]
    webUrl: Optional[str]

    def __init__(self, *args, **kwargs):
        self._api = api
        super().__init__(*args, **kwargs)

    class Config:
        alias_generator = to_camel


class Link(_Base):
    pass


class Property(_Base):
    name: str
    value: Any


class Change(_Base):
    id: str
    version: str
    username: str
    date: datetime

    @validator("date", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class Dependency(_Base):
    id: str
    build_type_id: str
    number: str
    status: str
    state: str


class File(_Base):
    name: str
    size: int
    modification_time: datetime

    @validator("modification_time", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class ProjectSummary(_Base):
    id: str
    name: str
    description: Optional[str]
    parent_project_id: Optional[str]


class _Status(_Base):
    status: str
    requestorType: str
    timestamp: datetime

    @validator("timestamp", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class Status(_Base):
    current: _Status
