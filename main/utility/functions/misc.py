import requests

from main.utility.functions import LoggingService

log = LoggingService()


class GetRequests:
    def __init__(self, url) -> None:
        self.url = url

    def get_request(self):

        resp = requests.request(method="get", url=self.url)

        if resp.ok:
            result = resp.json()
            log.debug(result)
            return result
        else:
            result = {"error": {"message": resp.reason, "status": resp.status_code}}
            log.error(result)
            return resp

        # except Exception as ex:
        #     # result = {"error": {"message": resp.reason(), "status": resp.status_code()}}
        #     result = {"error": {"message": str(ex)}}
        # log.error(result)

