import click

from src.client import get_api_client
from src.commands.base import cli
from src.utils.json import pretty_print_dict
from src.utils.response import check_response


@cli.group()
def compare():
    pass


@compare.command(name="projectBom")
@click.option('--prjId', 'prjId', required=True)
@click.option('--compareId', 'compareId', required=True)
def compare_project_bom(prjId, compareId):
    response = get_api_client().compare_project_bom(prjId, compareId)
    check_response(response)
    pretty_print_dict(response.json())
