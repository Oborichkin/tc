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
    href: Optional[str]
    webUrl: Optional[str]

    def __init__(self, *args, **kwargs):
        self._api = api
        super().__init__(*args, **kwargs)

    class Config:
        alias_generator = to_camel


class Property(_Base):
    name: str
    value: Any


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


class BuildSummary(_Base):
    id: str
    build_type_id: str
    number: str
    status: str
    state: str
    branch_name: Optional[str]
    default_branch: Optional[str]


class Change(_Base):
    id: str
    version: str
    username: str
    date: datetime

    @validator("date", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class VcsRootInstance(_Base):
    id: str
    vcs_root_id: str
    name: str


class Revision(_Base):
    version: str
    vcs_branch_name: str
    vsc_root_instance: VcsRootInstance


class Agent(_Base):
    name: str
    type_id: str


class Dependency(_Base):
    id: str
    build_type_id: str
    number: str
    status: str
    state: str


class Build(BuildSummary):
    status_text: str
    build_type: BuildType
    queued_date: datetime
    start_date: datetime
    finish_date: datetime
    last_changes: List[Change]
    revisions: List[Revision]
    versioned_settings_revision: Revision
    agent: Agent
    # test_occurances
    # artifacts
    # relatedIssues
    properties: List[Property]
    # statistics
    snapshot_dependencies: List[Dependency]
    artifact_dependencies: List[Dependency]

    @validator("queued_date", "start_date", "finish_date", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class Template(BuildType):
    template_flag: bool

    @validator("template_flag", pre=True)
    def str_to_bool(cls, value):
        return value == "true"


class ProjectSummary(_Base):
    id: str
    name: str
    description: Optional[str]
    parent_project_id: Optional[str]


class Project(ProjectSummary):
    parent_project: Optional[ProjectSummary]
    build_types: List[BuildType]
    templates: Optional[List[Template]]
    parameters: Optional[List[Property]]
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


class VscRootSummary(_Base):
    id: str
    name: str


class VscRoot(VscRootSummary):
    project: ProjectSummary
    properties: List[Property]
