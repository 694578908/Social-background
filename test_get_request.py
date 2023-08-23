import requests
import pytest

class TestRequest:

    def test_case_login(self):
        url = "http://higher8pre.douxiangapp.com/dboxAdmin/v1/security/manageLogin/"
        data = {"userName": "1123132", "pwd": "112321231"}
        response = requests.post(url=url, json=data)
        print(response.json())

        assert response.status_code == 200
    if __name__ == "__main__":
        pytest.main(['-vs'])

