import click

from src.client import get_api_client
from src.commands.base import cli
from src.dto.scan_result import ScanResult
from src.scanner import FosslightScanner
from src.utils.file import read_file
from src.utils.response import check_response


@cli.group()
def update():
    pass


@update.group("project")
def update_project():
    pass


@update.group("selfCheck")
def update_self_check():
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
    check_response(response)
    print("success")


@update_project.command('models')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--modelListToUpdate', 'modelListToUpdate', required=True)
def update_project_models(prjId, modelListToUpdate):
    client = get_api_client()
    response = client.update_project_models(prjId=prjId, modelListToUpdate=modelListToUpdate)
    check_response(response)
    print("Success: Update project model")


@update_project.command('modelFile')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--modelReportFile', 'modelReportFile', required=True)
def update_project_model_file(prjId, modelReportFile):
    modelReportFile = read_file(modelReportFile)
    client = get_api_client()
    response = client.update_project_model_file(prjId=prjId, modelReportFile=modelReportFile)
    check_response(response)
    print("Success: Update project model file")


@update_project.command('scan')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--dir', 'dir', required=True, help="project directory path")
def update_project_scan(prjId, dir):
    result: ScanResult = FosslightScanner.scan_all(dir)
    print("Success: scan directory")
    client = get_api_client()
    ossReport = None
    binaryTxt = None
    if report_file_path := result.report_file_path:
        ossReport = read_file(report_file_path)
    if binary_file_path := result.binary_file_path:
        binaryTxt = read_file(binary_file_path)

    if binaryTxt:
        response = client.update_project_bin(
            prjId=prjId,
            ossReport=ossReport,
            binaryTxt=binaryTxt,
        )
        check_response(response)
        print("Success: Upload project bin")

    if ossReport:
        response = client.update_project_src(
            prjId=prjId,
            ossReport=ossReport,
        )
        check_response(response)
        print("Success: Upload project src")


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
    client = get_api_client()
    response = client.update_project_bin(
        prjId=prjId,
        ossReport=ossReport,
        binaryTxt=binaryTxt,
        comment=comment,
        resetFlag=resetFlag,
    )
    check_response(response)
    print("Success: Upload project bin")


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
    client = get_api_client()
    response = client.update_project_src(
        prjId=prjId,
        ossReport=ossReport,
        comment=comment,
        resetFlag=resetFlag,
    )
    check_response(response)
    print("Success: Upload project src")


@update_project.command('packages')
@click.option('--prjId', 'prjId', required=True, help="project id")
@click.option('--packageFile', 'packageFile', required=True)
@click.option('--verifyFlag', 'verifyFlag')
def update_project_packages(prjId, packageFile, verifyFlag):
    if packageFile:
        packageFile = read_file(packageFile)
    client = get_api_client()
    response = client.update_project_packages(
        prjId=prjId,
        packageFile=packageFile,
        verifyFlag=verifyFlag,
    )
    check_response(response)
    print("Success: Upload project packages")


@update_self_check.command('report')
@click.option('--selfCheckId', 'selfCheckId', required=True, help="selfCheck id")
@click.option('--ossReport', 'ossReport')
@click.option('--resetFlag', 'resetFlag')
def update_self_check_report(selfCheckId, ossReport, resetFlag):
    if ossReport:
        ossReport = read_file(ossReport)
    client = get_api_client()
    response = client.update_self_check_report(
        selfCheckId=selfCheckId,
        ossReport=ossReport,
        resetFlag=resetFlag,
    )
    check_response(response)
    print("Success: Upload self-check report")


@update_self_check.command('watchers')
@click.option('--selfCheckId', 'selfCheckId', required=True, help="selfCheck id")
@click.option('--emailList', 'emailList', required=True)
def update_self_check_watchers(selfCheckId, emailList):
    client = get_api_client()
    response = client.update_selfCheck_watchers(
        selfCheckId=selfCheckId,
        emailList=emailList,
    )
    check_response(response)
    print("Success: Update self-check watchers")


@update_partners.command('watchers')
@click.option('--partnerId', 'partnerId', required=True, help="partner id")
@click.option('--emailList', 'emailList', required=True)
def update_partners_watchers(partnerId, emailList):
    client = get_api_client()
    response = client.update_partners_watchers(
        partnersId=partnerId,
        emailList=emailList,
    )
    check_response(response)
    print("Success: Update partners watchers")
