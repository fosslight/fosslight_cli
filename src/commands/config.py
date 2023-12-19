import click

from src.commands.base import cli
from src.config import ConfigManager


@cli.group()
def config():
    pass


@config.command(name="server")
@click.option('--server', '-s', help="Server url")
@click.option('--token', '-t', help="Account token")
def config_variable(server, token):
    config_info = ConfigManager.read_config()
    if server:
        config_info.server_url = server
    if token:
        config_info.token = token
    ConfigManager.save_config(server_url=config_info.server_url, token=config_info.token)
    print("Success: config")
