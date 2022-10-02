import json
import typer
import inspect

from .client import Client
from .schema import Link

COMPLETION_MAP = {
    "projects": ["parent", "build_types", "template", "parameter", "vcs", "feature", "projects"],
    "vcs_roots": ["project", "properties", "vcs_root_instances"],
    "builds": ["last_changes", "snapshot_dependencies", "artifact-dependencies", "artifacts"],
    "build_types": ["builds"],
    "artifacts": [""]
}


def make_projects_completion(client: Client, parent=None):
    def project_completion():
        if parent:
            return [(proj.id, proj.description) for proj in client.projects(parent).projects]
        return [(proj.id, proj.description) for proj in client.projects()]
    return project_completion


def make_builds_completion(client: Client):
    def builds_completion():
        return [build.id for build in client.builds()]
    return builds_completion

f = open("debug", "a")


def make_generic_completer(client: Client):
    def generic_completer(ctx: typer.Context, incomplete: str):
        cmd = [ctx.command.name, ctx.params["name"], *ctx.params["cmd"]]
        f.write(json.dumps(cmd) + "\n")

        if cmd[-2] in COMPLETION_MAP:
            # Select from available properties
            return COMPLETION_MAP[cmd[-2]]
        elif cmd[-1] in COMPLETION_MAP:
            # Get possibilities from API
            parent_section_getter = getattr(client, cmd[-3])
            parent_section = parent_section_getter(cmd[-2])
            section = getattr(parent_section, cmd[-1])
            if isinstance(section, Link):
                f.write(f"VISITING: {section.href}\n")
                section = section.visit()
            if section and hasattr(section[0], "id"):
                return [(obj.id, str(obj)) for obj in section]
            else:
                return [(obj.name, str(obj)) for obj in section]
        return ["SHOULD_NOT_BE_HERE"]

    return generic_completer
