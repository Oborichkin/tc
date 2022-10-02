import os
import typer
import json
import click
from typing import List
from dotenv import load_dotenv
from .client import Client

load_dotenv()


# TODO Read URL and authorization from config first, then environment variables, then command line args
client = Client(os.environ["TEAMCITY_URL"], os.environ["TEAMCITY_TOKEN"])
app = typer.Typer()

COMPLETION_MAP = {
    "projects": ["parent", "build_types", "template", "parameter", "vcs", "feature", "projects"],
    "vcs_roots": ["project", "properties", "vcs_root_instances"],
    "build": [],
    "build_types": ["builds"],
}


def make_project_completion(parent=None):
    def project_completion():
        if parent:
            return [(proj.id, proj.description) for proj in client.project(parent).projects]
        return [(proj.id, proj.description) for proj in client.projects()]

    return project_completion


f = open("debug", "a")


def generic_completer(ctx: typer.Context, incomplete: str):
    cmd = [ctx.command.name, ctx.params["name"], *ctx.params["cmd"]]
    f.write(json.dumps(cmd) + "\n")
    if cmd[-2] in COMPLETION_MAP:
        return COMPLETION_MAP[cmd[-2]]
    elif cmd[-1] in COMPLETION_MAP:
        obj = getattr(client, cmd[-3])
        f.write(str(obj) + "\n")
        obj = obj(ctx.params["name"])
        f.write(str(obj) + "\n")
        obj = getattr(obj, cmd[-1])
        f.write(str(obj) + "\n")
        return [o.id for o in obj]
    return ["SHOULD_NOT_BE_HERE"]


@app.command()
def server():
    info = client.server()
    typer.echo(f"JetBrains TeamCity {info.version}\n" f"Build number: {info.build_number}\n")


@app.command()
def projects(
    name: str = typer.Argument("_Root", autocompletion=make_project_completion()),
    cmd: List[str] = typer.Argument(None, autocompletion=generic_completer),
):
    pass


@app.command()
def vsc(name: str):
    pass


@app.command()
def build(name: str):
    pass


@app.command()
def user(name: str):
    pass


@app.command()
def groups(name: str):
    pass


@app.command()
def agent(name: str):
    pass


@app.command()
def queue(name: str):
    pass


@app.command()
def pool(name: str):
    pass


@app.command()
def investigation(name: str):
    pass


@app.command()
def mute(name: str):
    pass


if __name__ == "__main__":
    app()
