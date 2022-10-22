import uuid
import pendulum
from datetime import datetime
from pydantic import validator
from ._base import _Base


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
