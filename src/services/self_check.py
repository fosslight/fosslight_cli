from requests import Response

from src.client import get_api_client
from src.utils.file import read_file
from src.utils.response import check_response


class SelfCheckService:

    def create(self, prjName, prjVersion) -> str:
        response = get_api_client().create_self_check(prjName, prjVersion)
        check_response(response)
        return response.json()['prjId']

    def export(self, selfCheckId) -> Response:
        client = get_api_client()
        response = client.export_self_check(selfCheckId)
        check_response(response)
        return response

    def update_report(self, selfCheckId, ossReport=None, resetFlag=None):
        response = get_api_client().update_self_check_report(
            selfCheckId=selfCheckId,
            ossReport=read_file(ossReport) if ossReport else None,
            resetFlag=resetFlag,
        )
        check_response(response)

    def update_watchers(self, selfCheckId, emailList):
        response = get_api_client().update_selfCheck_watchers(
            selfCheckId=selfCheckId,
            emailList=emailList,
        )
        check_response(response)
