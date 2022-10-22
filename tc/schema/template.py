from pydantic import validator

from .build import BuildType


class Template(BuildType):
    template_flag: bool

    @validator("template_flag", pre=True)
    def str_to_bool(cls, value):
        return value == "true"
