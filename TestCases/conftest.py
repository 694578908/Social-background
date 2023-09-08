import pytest
from common.yaml_util import YamlUtil


@pytest.fixture(params=['login', 'get_token'], autouse=True)
def case_type(request):
    return request.param


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
    yield


