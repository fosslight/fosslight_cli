import click

from client import get_api_client
from commands.base import cli


@cli.group()
def compare():
    pass


@compare.command(name="projectBom")
@click.option('--prjId', 'prjId', required=True)
@click.option('--compareId', 'compareId', required=True)
def compare_project_bom(prjId, compareId):
    print("compare_project_bom")
    response = get_api_client().compare_project_bom(prjId, compareId)
    print(response)
