import pendulum
from datetime import datetime
from pydantic import validator
from typing import Optional, List, TYPE_CHECKING
from ._base import _Base, Link, Dependency, Property, Change

from .agent import Agent
from .vcs import Revision
from .artifact import ArtifactLink


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


class BuildQueue(_Base):
    pass
