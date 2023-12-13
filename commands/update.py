import click

from client import get_api_client
from commands.base import cli
from enums.yn import YnType
from utils.file import read_file


@cli.group()
def update():
    pass


@update.group("project")
def update_project():
    pass


@update.group("selfcheck")
def update_selfcheck():
    pass


@update.group("partners")
def update_partners():
    pass


@update_project.command('watchers')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--emailList', 'emailList', required=True, help="watcher emailList")
def update_project_watchers(prjId, emailList):
    client = get_api_client()
    response = client.update_project_watchers(prjId=prjId, emailList=emailList)
    print(response)


@update_project.command('models')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--modelListToUpdate', 'modelListToUpdate', required=True)
def update_project_models(prjId, modelListToUpdate):
    client = get_api_client()
    response = client.update_project_models(prjId=prjId, modelListToUpdate=modelListToUpdate)
    print(response)


@update_project.command('modelFile')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--modelReportFile', 'modelReportFile', required=True)
def update_project_model_file(prjId, modelReportFile):
    modelReportFile = read_file(modelReportFile)
    client = get_api_client()
    response = client.update_project_model_file(prjId=prjId, modelReportFile=modelReportFile)
    print(response)


@update_project.command('bin')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--ossReport', 'ossReport')
@click.option('--binaryTxt', 'binaryTxt')
@click.option('--comment', 'comment')
@click.option('--resetFlag', 'resetFlag')
def update_project_bin(
    prjId,
    ossReport,
    binaryTxt,
    comment,
    resetFlag,
):
    if ossReport:
        ossReport = read_file(ossReport)
    if binaryTxt:
        binaryTxt = read_file(binaryTxt)
    if resetFlag:
        resetFlag = YnType(resetFlag.upper())
    client = get_api_client()
    response = client.update_project_bin(
        prjId=prjId,
        ossReport=ossReport,
        binaryTxt=binaryTxt,
        comment=comment,
        resetFlag=resetFlag,
    )
    print(response)

@update_project.command('src')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--ossReport', 'ossReport')
@click.option('--comment', 'comment')
@click.option('--resetFlag', 'resetFlag')
def update_project_src(
    prjId,
    ossReport,
    comment,
    resetFlag,
):
    if ossReport:
        ossReport = read_file(ossReport)
    if resetFlag:
        resetFlag = YnType(resetFlag.upper())
    client = get_api_client()
    response = client.update_project_src(
        prjId=prjId,
        ossReport=ossReport,
        comment=comment,
        resetFlag=resetFlag,
    )
    print(response)


@update_project.command('packages')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--packageFile', 'packageFile', required=True)
@click.option('--verifyFlag', 'verifyFlag')
def update_project_packages(prjId, packageFile, verifyFlag):
    if packageFile:
        packageFile = read_file(packageFile)
    if verifyFlag:
        verifyFlag = YnType(verifyFlag.upper())
    client = get_api_client()
    response = client.update_project_packages(
        prjId=prjId,
        packageFile=packageFile,
        verifyFlag=verifyFlag,
    )
    print(response)


@update_project.command('report')
@click.option('--selfcheckId', 'selfcheckId', required=True, help="selfcheck id")
@click.option('--name', 'name', required=True)
@click.option('--ossReport', 'ossReport')
@click.option('--resetFlag', 'resetFlag')
def update_selfcheck_report(selfcheckId, name, ossReport, resetFlag):
    if ossReport:
        ossReport = read_file(ossReport)
    if resetFlag:
        resetFlag = YnType(resetFlag.upper())
    client = get_api_client()
    response = client.update_selfcheck_report(
        selfcheckId=selfcheckId,
        name=name,
        ossReport=ossReport,
        resetFlag=resetFlag,
    )
    print(response)


@update_project.command('report')
@click.option('--selfcheckId', 'selfcheckId', required=True, help="selfcheck id")
@click.option('--emailList', 'emailList', required=True)
def update_selfcheck_watchers(selfcheckId, emailList):
    client = get_api_client()
    response = client.update_selfcheck_watchers(
        selfcheckId=selfcheckId,
        emailList=emailList,
    )
    print(response)


@update_partners.command('watchers')
@click.option('--partnerId', 'partnerId', required=True, help="partner id")
@click.option('--emailList', 'emailList', required=True)
def update_partners_watchers(partnerId, emailList):
    client = get_api_client()
    response = client.update_partners_watchers(
        partnersId=partnerId,
        emailList=emailList,
    )
    print(response)
