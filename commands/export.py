import click

from client import get_api_client
from commands.base import cli


@cli.group()
def export():
    pass


@export.group()
def project():
    pass


@project.command("bom")
@click.option('--id', required=True, help="Project ID")
@click.option('--excel', is_flag=True, show_default=True, help="export with excel")
@click.option('--json', is_flag=True, show_default=True, default=True, help="export with json")
def export_project_bom(id, excel, json):
    print("export project bom")
    client = get_api_client()
    if json:
        client.export_bom_json(id)
    else:
        client.export_bom_excel(id)


@export.command("selfcheck")
def export_selfcheck(id):
    print("export_selfcheck")
    client = get_api_client()
    client.export_selfcheck(id)
