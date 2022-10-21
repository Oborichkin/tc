import uuid
import pendulum
from typing import Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, validator, PrivateAttr

from .api import API, api
from .utils import to_camel


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


class Server(_Base):
    version: str
    build_number: str
    version_major: int
    version_minor: int
    start_time: datetime
    current_time: datetime
    build_date: datetime
    internal_id: uuid.UUID

    @validator("start_time", "current_time", "build_date", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class BuildSummary(_Base):
    id: str
    build_type_id: str
    number: str
    status: str
    state: str
    branch_name: Optional[str]
    default_branch: Optional[str]

    def __str__(cls):
        return f"#{cls.number} ({cls.status}) [{cls.state}]"


class BuildsLink(Link):
    def visit(cls) -> List[BuildSummary]:
        return [BuildSummary(**data) for data in cls._api.get(cls.href)["build"]]


class BuildType(_Base):
    id: str
    name: str
    description: Optional[str]
    project_name: str
    project_id: str
    builds: Optional[BuildsLink]

    def __str__(cls):
        return f"{cls.name}: {cls.description}"


class BuildQueue(_Base):
    pass


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


class VcsRootInstancesLink(Link):
    def visit(cls) -> List[VcsRootInstance]:
        return [VcsRootInstance(**data) for data in cls._api.get(cls.href)["vcs-root-instances"]]


class Revision(_Base):
    version: str
    vcs_branch_name: str
    vcs_root_instance: Optional[VcsRootInstance]


class Agent(_Base):
    name: str
    type_id: str


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


class ArtifactLink(Link):
    def visit(cls) -> List[File]:
        return [File(**data) for data in cls._api.get(cls.href)["file"]]


class Build(BuildSummary):
    status_text: str
    build_type: BuildType
    queued_date: datetime
    start_date: datetime
    finish_date: datetime
    last_changes: Optional[List[Change]]
    revisions: Optional[List[Revision]]
    versioned_settings_revision: Optional[Revision]
    agent: Agent
    # test_occurances
    artifacts: ArtifactLink
    # relatedIssues
    properties: List[Property]
    # statistics
    snapshot_dependencies: Optional[List[Dependency]]
    artifact_dependencies: Optional[List[Dependency]]

    def __str__(cls):
        return f"{cls.build_type} [{cls.status_text}]"

    @validator("last_changes", pre=True)
    def property_list(cls, value):
        return value.get("lastChanges", [])

    @validator("revisions", pre=True)
    def revisions_list(cls, value):
        return value.get("revisions", [])

    @validator("properties", pre=True)
    def properties_list(cls, value):
        return value.get("properties", [])

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
    build_types: Optional[List[BuildType]]
    templates: Optional[List[Template]]
    parameters: Optional[List[Property]]
    projects: List[ProjectSummary]
    # vsc_roots
    # project_features

    @validator("build_types", "templates", pre=True)
    def _build_type_list(cls, value):
        return value.get("buildType", [])

    @validator("parameters", pre=True)
    def _property_list(cls, value):
        return value.get("property", [])

    @validator("projects", pre=True)
    def _project_list(cls, value):
        return value.get("project", [])


class VcsRootSummary(_Base):
    id: str
    name: str


class VcsRoot(VcsRootSummary):
    vcs_name: str
    modification_check_interval = int
    project: ProjectSummary
    properties: List[Property]
    vcs_root_instances: VcsRootInstancesLink

    @validator("properties", pre=True)
    def properties_list(cls, value):
        return value.get("property", [])


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
