import click

from client import get_api_client
from commands.base import cli


@cli.group()
def get():
    pass


@get.command("project")
@click.option("--createDate", "createDate")
@click.option("--creator", "creator")
@click.option("--division", "division")
@click.option("--modelName", "modelName")
@click.option("--prjIdList", "prjIdList")
@click.option("--status", "status")
@click.option("--updateDate", "updateDate")
def get_project(
    createDate,
    creator,
    division,
    modelName,
    prjIdList,
    status,
    updateDate,
):
    client = get_api_client()
    response = client.get_projects(
        createDate=createDate,
        creator=creator,
        division=division,
        modelName=modelName,
        prjIdList=prjIdList,
        status=status,
        updateDate=updateDate,
    )
    print(response)


@get.command("projectModels")
@click.option("--prjIdList", "prjIdList")
def get_project_models(prjIdList):
    client = get_api_client()
    response = client.get_project_models(prjIdList=prjIdList)
    print(response)


@get.command("license")
@click.option("--licenseName", "licenseName", required=True, help="license name")
def get_license(licenseName):
    client = get_api_client()
    response = client.get_licenses(licenseName=licenseName)
    print(response)


@get.command("oss")
@click.option("--ossName", "ossName", required=True, help="oss name")
@click.option("--ossVersion", "ossVersion", help="oss version")
@click.option("--downloadLocation", "downloadLocation", help="download location")
def get_oss(ossName, ossVersion, downloadLocation):
    client = get_api_client()
    response = client.get_oss(
        ossName=ossName,
        ossVersion=ossVersion,
        downloadLocation=downloadLocation,
    )
    print(response)


@get.command("partner")
@click.option("--createDate", "createDate")
@click.option("--creator", "creator")
@click.option("--division", "division")
@click.option("--partnerIdList", "partnerIdList")
@click.option("--status", "status")
@click.option("--updateDate", "updateDate")
def get_partner(
    createDate,
    creator,
    division,
    partnerIdList,
    status,
    updateDate,
):
    client = get_api_client()
    response = client.get_partners(
        createDate=createDate,
        creator=creator,
        division=division,
        partnerIdList=partnerIdList,
        status=status,
        updateDate=updateDate,
    )
    print(response)


@get.command("maxVulnerability")
@click.option("--ossName", "ossName", required=True, help="oss name")
@click.option("--ossVersion", "ossVersion", help="oss version")
def get_max_vulnerability(ossName, ossVersion):
    client = get_api_client()
    response = client.get_max_vulnerability(ossName=ossName, ossVersion=ossVersion)
    print(response)


@get.command("vulnerability")
@click.option("--cveId", "cveId", help="cve id")
@click.option("--ossName", "ossName", help="oss name")
@click.option("--ossVersion", "ossVersion", help="oss version")
def get_vulnerability(cveId, ossName, ossVersion):
    client = get_api_client()
    response = client.get_vulnerability(
        cveId=cveId,
        ossName=ossName,
        ossVersion=ossVersion,
    )
    print(response)


@get.command("code")
@click.option("--codeType", "codeType", required=True, help="code type")
@click.option("--detailValue", "detailValue", help="detail value")
def get_code(codeType, detailValue):
    client = get_api_client()
    response = client.get_codes(codeType=codeType, detailValue=detailValue)
    print(response)
