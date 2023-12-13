from dataclasses import asdict
from typing import Optional, List, Union

import requests

from config import ConfigManager
from enums.distribution_type import DistributionType
from enums.os_type import OsType
from enums.priority import Priority
from enums.yn import YnType


class ApiClient:

    def __init__(self, server_url):
        self.server_url = server_url
        self.session = requests.Session()

    def set_token(self, token):
        self.session.headers.update({'Authorization': token})

    def post(self, path, *args, **kwargs):
        return self.session.post(self.server_url + path, *args, **kwargs)

    def put(self, path, *args, **kwargs):
        return self.session.put(self.server_url + path, *args, **kwargs)

    def get(self, path, *args, **kwargs):
        return self.session.get(self.server_url + path, *args, **kwargs)

    def create_project(
        self,
        prjName: str,
        osType: Union[OsType, str],
        distributionType: Union[DistributionType, str],
        networkServerType: Union[YnType, str],
        priority: Union[Priority, str],
        osTypeEtc: Optional[str] = None,
        prjVersion: Optional[str] = None,
        publicYn: Optional[Union[YnType, str]] = None,
        comment: Optional[str] = None,
        userComment: Optional[str] = None,
        watcherEmailList: Optional[List[str]] = None,
        modelListToUpdate: Optional[List[str]] = None,
        modelReportFile: Optional[str] = None,
    ):
        data = {
            "prjName": prjName,
            "osType": osType.api_value,
            "distributionType": distributionType.api_value,
            "networkServerType": networkServerType.api_value,
            "priority": priority.api_value,
            "osTypeEtc": osTypeEtc,
            "prjVersion": prjVersion,
            "publicYn": publicYn.api_value if publicYn else None,
            "comment": comment,
            "userComment": userComment,
            "watcherEmailList": watcherEmailList,
            "modelListToUpdate": modelListToUpdate,
            "modelReportFile": modelReportFile,
        }
        return self.post('/api/v2/projects', data=data)

    def update_project_watchers(self, prjId, emailList: List[str]):
        data = {"emailList": emailList}
        return self.post(f'/api/v2/projects/{prjId}/watchers', data=data)

    def update_project_models(self, prjId, modelListToUpdate: List[str]):
        data = {"modelListToUpdate": modelListToUpdate}
        return self.put(f'/api/v2/projects/{prjId}/models', data=data)

    def update_project_model_file(self, prjId, modelReportFile: bytes):
        files = {
            "modelReport": modelReportFile,
        }
        return self.put(f'/api/v2/projects/{prjId}/models/upload', files=files)

    def update_project_bin(
        self,
        prjId: int,
        ossReport: Optional[bytes] = None,
        binaryTxt: Optional[bytes] = None,
        comment: Optional[str]=None,
        resetFlag: Optional[YnType] = None,
    ):
        files = {
            "ossReport": ossReport,
            "binaryTxt": binaryTxt,
        }
        data = {
            "resetFlag": resetFlag.api_value if resetFlag else None,
            "comment": comment,
        }
        return self.put(f'/api/v2/projects/{prjId}/bin', data=data, files=files)

    def update_project_src(self, prjId: int, ossReport: Optional[bytes] = None, comment: Optional[str] = None, resetFlag: Optional[YnType] = None):
        files = {"ossReport": ossReport}
        data = {
            "resetFlag": resetFlag.api_value if resetFlag else None,
            "comment": comment,
        }
        return self.put(f'/api/v2/projects/{prjId}/src', data=data, files=files)

    def update_project_packages(self, prjId: int, packageFile: bytes, verifyFlag: Optional[YnType] = None):
        data = {"verifyFlag": verifyFlag.api_value if verifyFlag else None}
        files = {"packageFile": packageFile}
        return self.put(f'/api/v2/projects/{prjId}/packages', files=files, data=data)

    def get_projects(
        self,
        createDate: Optional[str] = None,
        creator: Optional[str] = None,
        division: Optional[str] = None,
        modelName: Optional[str] = None,
        prjIdList: Optional[str] = None,
        status: Optional[str] = None,
        updateDate: Optional[str] = None,
    ):
        params = {
            "createDate": createDate,
            "creator": creator,
            "division": division,
            "modelName": modelName,
            "prjIdList": prjIdList,
            "status": status,
            "updateDate": updateDate,
        }
        return self.get('/api/v2/projects', params=params)

    def get_project_models(self, prjIdList: Optional[int] = None):
        params = {"prjIdList": prjIdList}
        return self.get('/api/v2/projects/models', params=params)

    def compare_project_bom(self, prjId: int, compareId: int):
        return self.get(f'/api/v2/projects/{prjId}/bom/compare-with/{compareId}')

    def export_project_bom(self, prjId: int, mergeSaveFlag: Optional[YnType] = None):
        params = {"mergeSaveFlag": mergeSaveFlag.api_value if mergeSaveFlag else None}
        return self.get(f'/api/v2/projects/{prjId}/bom/export', params=params)

    def export_project_bom_json(self, prjId: int):
        return self.get(f'/api/v2/projects/{prjId}/bom/json')

    def get_licenses(self, licenseName: str):
        data = {"licenseName": licenseName}
        return self.get('/api/v2/licenses', params=data)

    def get_oss(self, ossName: str, ossVersion: Optional[str] = None, downloadLocation: Optional[str] = None):
        params = {
            "ossName": ossName,
            "ossVersion": ossVersion,
            "downloadLocation": downloadLocation,
        }
        return self.get('/api/v2/oss', params=params)

    def get_partners(
        self,
        createDate: Optional[str] = None,
        creator: Optional[str] = None,
        division: Optional[str] = None,
        partnerIdList: Optional[str] = None,
        status: Optional[str] = None,
        updateDate: Optional[str] = None,
    ):
        params = {
            "createDate": createDate,
            "creator": creator,
            "division": division,
            "partnerIdList": partnerIdList,
            "status": status,
            "updateDate": updateDate,
        }
        return self.get('/api/v2/partners', params=params)

    def update_partners_watchers(self, partnerId: int, emailList: List[str]):
        data = {"emailList": emailList}
        return self.put(f"/api/v2/partners/{partnerId}/watchers", data=data)

    def get_max_vulnerability(self, ossName: str, ossVersion: Optional[str] = None):
        params = {
            "ossName": ossName,
            "ossVersion": ossVersion
        }
        return self.get('/api/v2/max-vulnerabilities', params=params)

    def get_vulnerability(self, cveId: Optional[str] = None, ossName: Optional[str] = None, ossVersion: Optional[str] = None):
        params = {
            "cveId": cveId,
            "ossName": ossName,
            "ossVersion": ossVersion
        }
        return self.get('/api/v2/vulnerabilities', params=params)

    def create_selfcheck(self, prjName: str, prjVersion: Optional[str] = None):
        data = {"prjName": prjName, "prjVersion": prjVersion}
        return self.post('/api/v2/selfchecks', data=data)

    def update_selfcheck_report(self, selfcheckId: int, name: str, ossReport: bytes=None, resetFlag: YnType=None):
        files = {}
        if ossReport:
            files['ossReport'] = ossReport
        data = {
            "name": name,
            "resetFlag": resetFlag
        }
        return self.put(f'/api/v2/selfchecks/{selfcheckId}/report', files=files, data=data)

    def update_selfcheck_watchers(self, selfcheckId: int, emailList: List[str]):
        return self.put(f'/api/v2/selfchecks/{selfcheckId}/watchers', data={"emailList": emailList})

    def export_selfcheck(self, selfcheckId: int):
        return self.get(f'/api/v2/selfchecks/{selfcheckId}/export')

    def get_codes(self, codeType: str, detailValue: str = None):
        params = {"codeType": codeType, "detailValue": detailValue}
        return self.get('/api/v2/codes', params=params)


def get_api_client():
    config = ConfigManager.read_config()
    if not config.server_url or not config.token:
        raise Exception('Please set server_url and token')
    client = ApiClient(config.server_url)
    client.set_token(config.token)
    return client
