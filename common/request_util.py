import requests
import json


class RequestUtil:

    session = requests.session()

    def send_requests(self, method, url, data, **kwargs):
        method = str(method).lower()
        rep = None
        if method == 'get':
            rep = RequestUtil.session.request(method=method, url=url, params=data, **kwargs)
        else:
            data = json.dumps(data)
            rep = RequestUtil.session.request(method=method, url=url, data=data, **kwargs)
        return rep.text
