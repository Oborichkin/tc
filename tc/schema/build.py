import pendulum
from datetime import datetime
from pydantic import validator, BaseModel
from typing import Optional, List, TYPE_CHECKING
from ._base import _Base, Link, Dependency, Property, Change

from .agent import Agent, AgentLink
from .vcs import Revision
from .artifact import ArtifactLink
from .project import ProjectSummary
from .user import UserSummary


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


class Assignment(BaseModel):
    timestamp: datetime
    text: Optional[str]
    user: UserSummary

    @validator("timestamp", pre=True)
    def iso_date(cls, value):
        return pendulum.parse(value)


class Investigation(_Base):
    id: str
    state: str
    assignee: UserSummary
    # scope
    # target
    # resolution


class BuildsLink(Link):
    def visit(cls) -> List[BuildSummary]:
        return [BuildSummary(**data) for data in cls._api.get(cls.href)["build"]]


class InvestigationsLink(Link):
    def visit(cls) -> List[Investigation]:
        return [Investigation(**data) for data in cls._api.get(cls.href)["investigation"]]


class BuildTypeSummary(_Base):
    id: str
    name: str
    description: Optional[str]
    project_name: str
    project_id: str
    builds: Optional[BuildsLink]

    def __str__(cls):
        return f"{cls.name}: {cls.description}"


class BuildType(BuildTypeSummary):
    project: ProjectSummary
    builds: BuildsLink
    investigations: InvestigationsLink
    compatible_agents: AgentLink


class Build(BuildSummary):
    status_text: str
    build_type: BuildTypeSummary
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


class BuildQueue(_Base):
    pass
