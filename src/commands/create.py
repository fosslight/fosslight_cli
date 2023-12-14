import click

from src.client import get_api_client
from src.commands.base import cli
from src.enums.distribution_type import DistributionType
from src.enums.os_type import OsType
from src.enums.priority import Priority
from src.enums.yn import YnType


@cli.group()
def create():
    pass


@create.command("project")
@click.option('--prjName', 'prjName', required=True, help="Name of the Project")
@click.option('--osType', 'osType', required=True, type=click.Choice(OsType.choices(), case_sensitive=False), help="OS type of the Project")
@click.option('--distributionType', 'distributionType', required=True, type=click.Choice(DistributionType.choices(), case_sensitive=False), help="")
@click.option('--networkServerType', 'networkServerType', required=True, type=click.Choice(YnType.choices(), case_sensitive=False), help="")
@click.option('--priority', 'priority', required=True, type=click.Choice(Priority.choices(), case_sensitive=False), help="")
@click.option('--osTypeEtc', 'osTypeEtc', help="")
@click.option('--prjVersion', 'prjVersion', help="")
@click.option('--publicYn', 'publicYn', type=click.Choice(YnType.choices(), case_sensitive=False), help="")
@click.option('--comment', 'comment', help="")
@click.option('--userComment', 'userComment', help="")
@click.option('--watcherEmailList', 'watcherEmailList', help="")
@click.option('--modelListToUpdate', 'modelListToUpdate', help="")
@click.option('--modelReportFile', 'modelReportFile', help="")
def create_project(
    prjName,
    osType,
    distributionType,
    networkServerType,
    priority,
    osTypeEtc,
    prjVersion,
    publicYn,
    comment,
    userComment,
    watcherEmailList,
    modelListToUpdate,
    modelReportFile,
):
    osType = OsType(osType.upper())
    distributionType = DistributionType(distributionType.upper())
    networkServerType = YnType(networkServerType.upper())
    priority = Priority(priority.upper())
    publicYn = YnType(publicYn.upper()) if publicYn else None

    print("create_project")
    response = get_api_client().create_project(
        prjName=prjName,
        osType=osType,
        distributionType=distributionType,
        networkServerType=networkServerType,
        priority=priority,
        osTypeEtc=osTypeEtc,
        prjVersion=prjVersion,
        publicYn=publicYn,
        comment=comment,
        userComment=userComment,
        watcherEmailList=watcherEmailList,
        modelListToUpdate=modelListToUpdate,
        modelReportFile=modelReportFile,
    )
    print(response)


@create.command("self_check")
@click.option('--name', '-n', required=True, help="Name of the Project")
def create_self_check(name):
    print("create_self_check")
    get_api_client().create_selfcheck(project_name=name)
