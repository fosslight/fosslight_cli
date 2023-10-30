import click

from client import get_api_client
from commands.base import cli


@cli.group()
def update():
    pass


@update.command('project')
@click.option('--id', required=True, help="project id")
@click.option('--models', required=False, help="model list")
@click.option('--model-file', required=False, help="model file")
@click.option('--report', required=False, help="FOSSLight Report file")
@click.option('--bin', required=False, help="fosslight_binary file")
@click.option('--bin-comment', required=False, help="fosslight_binary file")
@click.option('--src', required=False, help="source file")
@click.option('--src-comment', required=False, help="source file")
@click.option('--pkg', required=False, help="package file")
@click.option('--watchers', required=False, help="watchers' email list")
def update_project(id, models, model_file, report, bin, bin_comment, src, src_comment, pkg, watchers):
    print("update_project")
    # TODO: check bin, src, pkg file path is valid
    # TODO: validate at least one of argument exist
    # TODO: check response
    client = get_api_client()
    if models:
        client.update_project_models(project_id=id, models=models)
    if model_file:
        client.update_project_model_file(project_id=id, model_file_path=model_file)
    if report or bin or bin_comment:
        client.update_project_bin(project_id=id, report_file_path=report, binary_file_path=bin, comment=bin_comment)
    if src or src_comment:
        client.update_project_src(project_id=id, report_file_path=src, comment=src_comment)
    if pkg:
        client.update_project_packages(project_id=id, package_file_path=pkg)
    if watchers:
        client.update_project_watchers(project_id=id, watchers=watchers)


@update.command("selfcheck")
@click.option('--id', required=True, help="project id")
@click.option('--report', required=False, help="FOSSLight Report file")
@click.option('--name', required=False, help="project name")
@click.option('--watchers', required=False, help="watchers' email list")
def update_selfcheck(id, report, name, watchers):
    client = get_api_client()
    if report or name:
        client.update_selfcheck_report(selfcheck_id=id, report_file_path=report, project_name=name)
    if watchers:
        client.update_selfcheck_watchers(selfcheck_id=id, watchers=watchers)
