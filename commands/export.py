import click

from client import get_api_client
from commands.base import cli
from enums.yn import YnType


@cli.group()
def export():
    pass


@export.group("project")
def export_project():
    pass


@export_project.command("bom")
@click.option("--prjId", "prjId", required=True, help="project id")
@click.option("--mergeSaveFlag", "mergeSaveFlag", help="mergeSaveFlag")
def export_project_bom(prjId, mergeSaveFlag):
    mergeSaveFlag = YnType(mergeSaveFlag.upper()) if mergeSaveFlag else None
    client = get_api_client()
    response = client.export_project_bom(prjId, mergeSaveFlag)
    print(response)


@export_project.command("bomJson")
@click.option("--prjId", "prjId", required=True, help="project id")
def export_project_bom_json(prjId):
    client = get_api_client()
    response = client.export_project_bom_json(prjId)
    print(response)


@export.command("selfcheck")
@click.option("--selfcheckId", "selfcheckId", required=True, help="selfcheck id")
def export_selfcheck(selfcheckId):
    print("export_selfcheck")
    client = get_api_client()
    response = client.export_selfcheck(selfcheckId)
    print(response)
