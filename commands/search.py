import click

from client import get_api_client
from commands.base import cli


@cli.group()
def search():
    pass


@search.command("licenses")
@click.option("--name", required=True, help="license name")
def search_license(name):
    client = get_api_client()
    client.get_license(name=name)


@search.command("oss")
@click.option("--name", required=True, help="oss name")
@click.option("--version", required=False, help="oss version")
@click.option("--location", required=False, help="download location")
def search_oss(name, version, location):
    client = get_api_client()
    client.get_license(name=name, version=version, location=location)


@search.command("partners")
def search_partner():
    pass


@search.command("project")
def search_project():
    pass


@search.command("vulnerability")
def search_vulnerability():
    pass


@search.command("selfcheck")
def search_selfcheck():
    pass


@search.command("code")
def search_code():
    pass
