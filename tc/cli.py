import os
import typer
from dotenv import load_dotenv
from .client import Client

load_dotenv()


client = Client(os.environ["TEAMCITY_URL"], os.environ["TEAMCITY_TOKEN"])
app = typer.Typer()


def complete_project():
    return [(proj.name, proj.description) for proj in client.projects]


@app.command()
def project(project: str = typer.Argument("_Root", help="Project ID", autocompletion=complete_project)):
    print(project)


@app.command()
def server():
    print(client.server)


if __name__ == "__main__":
    app()
