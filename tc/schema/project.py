from pydantic import validator
from typing import Optional, List
from ._base import _Base, Property, ProjectSummary
from .build import BuildTypeSummary
from .template import Template


class Project(ProjectSummary):
    parent_project: Optional[ProjectSummary]
    build_types: Optional[List[BuildTypeSummary]]
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
