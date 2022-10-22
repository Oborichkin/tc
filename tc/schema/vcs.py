from typing import Optional, List, TYPE_CHECKING
from pydantic import validator
from ._base import _Base, Link, Property
from .project import ProjectSummary


class VcsRootSummary(_Base):
    id: str
    name: str


class VcsRootInstanceSummary(_Base):
    id: str
    vcs_root_id: str
    name: str


class VcsRootInstancesLink(Link):
    def visit(cls) -> List[VcsRootInstanceSummary]:
        return [VcsRootInstanceSummary(**data) for data in cls._api.get(cls.href)["vcs-root-instances"]]


class VcsRoot(VcsRootSummary):
    vcs_name: str
    modification_check_interval = int
    project: ProjectSummary
    properties: List[Property]
    vcs_root_instances: VcsRootInstancesLink

    @validator("properties", pre=True)
    def properties_list(cls, value):
        return value.get("property", [])


class VcsRootInstance(VcsRootInstanceSummary):
    vcs_name: str
    modification_check_interval: int
    last_version: str
    vcs_root: VcsRoot


class Revision(_Base):
    version: str
    vcs_branch_name: str
    vcs_root_instance: Optional[VcsRootInstanceSummary]
