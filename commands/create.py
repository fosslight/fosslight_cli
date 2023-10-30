import click

from client import get_api_client
from commands.base import cli


@cli.group()
def create():
    pass


@create.command("project")
@click.option('--name', '-n', required=True, help="Name of the Project")
@click.option('--ostype', '-o', required=True, help="OS type of the Project")
def create_project(name, ostype):
    print("create_project")
    get_api_client().create_project(project_name=name, os_type=ostype)


@create.command("self_check")
@click.option('--name', '-n', required=True, help="Name of the Project")
def create_self_check(name):
    print("create_self_check")
    get_api_client().create_selfcheck(project_name=name)
