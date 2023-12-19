import datetime

import click

from src.client import get_api_client
from src.commands.base import cli
from src.utils.json import pretty_print_dict
from src.utils.response import check_response


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
    client = get_api_client()
    response = client.export_project_bom(prjId, mergeSaveFlag)
    check_response(response)
    with open(f"bom_{int(datetime.datetime.now().timestamp())}.xlsx", "wb") as f:
        f.write(response.content)
    print("Success: Export project bom")


@export_project.command("bomJson")
@click.option("--prjId", "prjId", required=True, help="project id")
def export_project_bom_json(prjId):
    client = get_api_client()
    response = client.export_project_bom_json(prjId)
    check_response(response)
    pretty_print_dict(response.json())


@export.command("selfCheck")
@click.option("--selfCheckId", "selfCheckId", required=True, help="selfCheck id")
def export_self_check(selfCheckId):
    client = get_api_client()
    response = client.export_self_check(selfCheckId)
    check_response(response)
    with open(f"bom_{int(datetime.datetime.now().timestamp())}.xlsx", "wb") as f:
        f.write(response.content)
    print("Success: Export self-check")
