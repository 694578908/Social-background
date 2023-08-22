import requests
import pytest
def test_case_login():
    print("Test case is running!")
    url = "http://higher8pre.douxiangapp.com/dboxAdmin/v1/security/manageLogin/"
    data = {"userName": "1123132", "pwd": "112321231"}
    response = requests.post(url=url, json=data)
    res = response.json()
    print("Response JSON:", res)
    assert response.status_code == 200
if __name__ == "__main__":
    pytest.main(test_case_login)11

