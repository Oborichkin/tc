import uuid
import pendulum
from typing import Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, validator, PrivateAttr

# if TYPE_CHECKING:
from .api import API, api


def to_camel(text: str) -> str:
    s = text.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(text) == 0:
        return text
    return s[0] + "".join(i.capitalize() for i in s[1:])


class _Base(BaseModel):
    _api: API = PrivateAttr()

    def __init__(self, *args, **kwargs):
        self._api = api
        super().__init__(*args, **kwargs)

    class Config:
        alias_generator = to_camel


class Server(_Base):
    version: str
    build_number: int
    version_major: int
    version_minor: int
    start_time: datetime
    current_time: datetime
    build_date: datetime
    internal_id: uuid.UUID

    @validator("start_time", "current_time", "build_date", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class BuildType(_Base):
    id: str
    name: str
    description: Optional[str]
    project_name: str
    project_id: str
    href: str


class Template(BuildType):
    template_flag: bool

    @validator("template_flag", pre=True)
    def str_to_bool(cls, value):
        return value == "true"


class Property(_Base):
    name: str
    value: Any


class ProjectSummary(_Base):
    id: str
    name: str
    description: Optional[str]
    parent_project_id: Optional[str]
    web_url: str
    href: str


class Project(ProjectSummary):
    build_types: List[BuildType]
    templates: List[Template]
    parameters: List[Property]
    projects: List[ProjectSummary]

    @validator("build_types", "templates", pre=True)
    def build_type_list(cls, value):
        return value.get("buildType", [])

    @validator("parameters", pre=True)
    def property_list(cls, value):
        return value.get("property", [])

    @validator("projects", pre=True)
    def project_list(cls, value):
        return value.get("project", [])
