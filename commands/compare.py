import click

from client import get_api_client
from commands.base import cli


@cli.group()
def compare():
    pass


@compare.command(name="bom")
@click.argument('old_project_id', required=True)
@click.argument('new_project_id', required=True)
def compare_bom(old_project_id, new_project_id):
    get_api_client().compare_project(old_project_id, new_project_id)
