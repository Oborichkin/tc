from typing import List
from ._base import Link, File


class ArtifactLink(Link):
    def visit(cls) -> List[File]:
        return [File(**data) for data in cls._api.get(cls.href)["file"]]
