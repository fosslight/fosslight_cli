import click

from src.client import get_api_client
from src.commands.base import cli
from src.enums import CodeType
from src.utils.codes import get_code_value
from src.utils.response import check_response


@cli.group()
def create():
    pass


@create.command("project")
@click.option('--prjName', 'prjName', required=True, help="Name of the Project")
@click.option('--osType', 'osType', required=True, help="OS type of the Project")
@click.option('--distributionType', 'distributionType', required=True, help="")
@click.option('--networkServerType', 'networkServerType', required=True, help="")
@click.option('--priority', 'priority', required=True, help="")
@click.option('--osTypeEtc', 'osTypeEtc', help="")
@click.option('--prjVersion', 'prjVersion', help="")
@click.option('--publicYn', 'publicYn', help="")
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
    response = get_api_client().create_project(
        prjName=prjName,
        osType=get_code_value(osType, CodeType.OS_TYPE),
        distributionType=get_code_value(distributionType, CodeType.DISTRIBUTION_TYPE),
        networkServerType=networkServerType,
        priority=get_code_value(priority, CodeType.PRIORITY),
        osTypeEtc=osTypeEtc,
        prjVersion=prjVersion,
        publicYn=publicYn,
        comment=comment,
        userComment=userComment,
        watcherEmailList=watcherEmailList,
        modelListToUpdate=modelListToUpdate,
        modelReportFile=modelReportFile,
    )
    check_response(response)
    prjId = response.json()['prjId']
    print(prjId)
    return prjId


@create.command("selfCheck")
@click.option('--prjName', 'prjName', required=True, help="Name of the Project")
@click.option('--prjVersion', 'prjVersion', help="Version of the Project")
def create_self_check(prjName, prjVersion):
    response = get_api_client().create_self_check(prjName=prjName, prjVersion=prjVersion)
    check_response(response)
    prjId = response.json()["prjId"]
    print(prjId)
    return prjId
