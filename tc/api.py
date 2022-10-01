import os
import dotenv
import requests as r
from requests.auth import HTTPBasicAuth


class API:
    def __init__(self, timeout=10):
        self.url = None
        self.headers = {"accept": "application/json"}
        self.timeout = timeout

    def connect(self, url, token):
        self.url = url
        self.headers["authorization"] = f"Bearer {token}"
        self.session = r.Session()

    def __getattr__(self, item):
        def __request_runner(url, json=None):
            url = f"{self.url}{url}"
            runner = getattr(self.session, item.lower())
            resp = runner(url, json=json, headers=self.headers, timeout=self.timeout)
            if resp.status_code != 200:
                raise Exception(str(resp))
            return resp.json()

        return __request_runner


api = API()
