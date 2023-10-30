import requests

from config import ConfigManager


class ApiClient:

    def __init__(self, server_url):
        self.server_url = server_url
        self.session = requests.Session()

    def set_token(self, token):
        self.session.headers.update({'Authorization': 'Token ' + token})

    def create_project(self, project_name, os_type, **kwargs):
        data = {
            'prjName': project_name,
            'osType': os_type
        }
        data.update(kwargs)
        return self.session.post(self.server_url + '/api/v2/projects', data=data)

    def get_projects(self, **kwargs):
        return self.session.post(self.server_url + '/api/v2/projects', params=kwargs)

    def get_project_models(self, **kwargs):
        return self.session.get(self.server_url + '/api/v2/projects/models', params=kwargs)

    def compare_project(self, project_id, compare_project_id, **kwargs):
        return self.session.get(self.server_url + f'/api/v2/projects/{project_id}/bom/compare-with/{compare_project_id}', params=kwargs)

    def export_bom_excel(self, project_id, **kwargs):
        return self.session.get(self.server_url + f'/api/v2/projects/{project_id}/bom/excel', params=kwargs)

    def export_bom_json(self, project_id, **kwargs):
        return self.session.get(self.server_url + f'/api/v2/projects/{project_id}/bom/json', params=kwargs)

    def update_project_bin(self, project_id, report_file_path=None, binary_file_path=None, comment=None):
        files = {}
        data = {}
        if report_file_path:
            files['ossReport'] = open(report_file_path, "rb")
        if binary_file_path:
            files['binaryTxt'] = open(binary_file_path, "rb")
        if comment:
            data['comment'] = comment
        return self.session.put(self.server_url + f'/api/v2/projects/{project_id}/bin', data=data, files=files)

    def update_project_src(self, project_id, report_file_path=None, comment=None):
        files = {}
        data = {}
        if report_file_path:
            files['ossReport'] = open(report_file_path, "rb")
        if comment:
            data['comment'] = comment
        return self.session.put(self.server_url + f'/api/v2/projects/{project_id}/src', data=data, files=files)

    def update_project_models(self, project_id, **kwargs):
        return self.session.put(self.server_url + f'/api/v2/projects/{project_id}/models', data=kwargs)

    def update_project_model_file(self, project_id, model_file_path):
        with open(model_file_path, 'rb') as f:
            files = {
                "modelReport": f,
            }
            return self.session.put(self.server_url + f'/api/v2/projects/{project_id}/models/upload', files=files)

    def upload_project_models(self, project_id, models):
        data = {}
        data['modelListToUpdate'] = models
        return self.session.put(self.server_url + f'/api/v2/projects/{project_id}/models', data=data)

    def update_project_packages(self, project_id, package_file_path, verifyFlag=None):
        data = {}
        files = {}
        files['packageFile'] = open(package_file_path, 'rb')
        if verifyFlag:
            data['verifyFlag'] = verifyFlag
        return self.session.put(self.server_url + f'/api/v2/projects/{project_id}/packages', files=files, data=data)

    def update_project_watchers(self, project_id, watchers):
        data = {}
        data['emailList'] = watchers
        return self.session.put(self.server_url + f'/api/v2/projects/{project_id}/watchers', data=data)

    def get_license(self, name):
        data = {}
        data['licenseName'] = name
        return self.session.get(self.server_url + '/api/v2/licenses', params=data)

    def get_oss(self, name, version=None, download_location=None):
        data = {}
        data['ossName'] = name
        if version:
            data['ossVersion'] = version
        if download_location:
            data['downloadLocation'] = download_location
        return self.session.get(self.server_url + '/api/v2/oss', params=data)

    def create_oss(self, **kwargs):
        return self.session.post(self.server_url + '/api/v2/oss', data=kwargs)

    def get_partners(self, **kwargs):
        return self.session.get(self.server_url + '/api/v2/partners', params=kwargs)

    def update_watchers(self, **kwargs):
        return self.session.put(self.server_url + '/api/v2/watchers', data=kwargs)

    def get_max_vulnerability(self, **kwargs):
        return self.session.get(self.server_url + '/api/v2/max-vulnerabilities', params=kwargs)

    def get_vulnerability(self, **kwargs):
        return self.session.get(self.server_url + '/api/v2/vulnerabilities', params=kwargs)

    def create_selfcheck(self, project_name, **kwargs):
        data = {
            "prjName": project_name,
        }
        data.update(kwargs)
        return self.session.post(self.server_url + '/api/v2/selfchecks', data=data)

    def export_selfcheck(self, selfcheck_id, **kwargs):
        return self.session.get(self.server_url + f'/api/v2/selfchecks/{selfcheck_id}/export', params=kwargs)

    def update_selfcheck_report(self, selfcheck_id, report_file_path=None, project_name=None):
        files = {}
        data = {}
        if report_file_path:
            files['ossReport'] = open(report_file_path, "rb")
        if project_name:
            data['name'] = project_name
        return self.session.put(self.server_url + f'/api/v2/selfchecks/{selfcheck_id}/report', files=files, data=data)

    def update_selfcheck_watchers(self, selfcheck_id, watchers):
        data = {}
        data["emailList"] = watchers
        return self.session.put(self.server_url + f'/api/v2/selfchecks/{selfcheck_id}/watchers', data=data)

    def get_codes(self, type, detail_value):

        return self.session.get(self.server_url + '/api/v2/codes', params=kwargs)


def get_api_client():
    config = ConfigManager().read_config()
    client = ApiClient(config.server_url)
    client.set_token(config.token)
    return client
