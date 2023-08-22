import requests
import pytest
def test_case_login():
    url = "http://higher8pre.douxiangapp.com/dboxAdmin/v1/security/manageLogin/"
    data = {"userName": "1123132", "pwd": "112321231"}
    response = requests.post(url=url, json=data)
    print(response.json())
if __name__ == "__main__":
    pytest.main()

