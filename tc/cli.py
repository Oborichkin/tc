import os
import json
from typing import List

import click
import typer
from dotenv import load_dotenv

load_dotenv()

from .client import Client
from .schema import Project
from .comp import make_builds_completion, make_projects_completion, make_generic_completer


# TODO Read URL and authorization from config first, then environment variables, then command line args
client = Client(os.environ["TEAMCITY_URL"], os.environ["TEAMCITY_TOKEN"])
app = typer.Typer()


@app.command()
def server():
    info = client.server()
    typer.echo(f"JetBrains TeamCity {info.version}\n" f"Build number: {info.build_number}\n")


@app.command()
def projects(
    name: str = typer.Argument("_Root", autocompletion=make_projects_completion(client)),
    cmd: List[str] = typer.Argument(None, autocompletion=make_generic_completer(client)),
):
    typer.echo(name)
    typer.echo(cmd)


@app.command()
def vsc(name: str):
    pass


@app.command()
def builds(
    name: str = typer.Argument(None, autocompletion=make_builds_completion(client)),
    cmd: List[str] = typer.Argument(None, autocompletion=make_generic_completer(client)),
):
    typer.echo(name)
    typer.echo(cmd)


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
