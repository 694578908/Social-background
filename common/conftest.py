import pytest
from common.yaml_util import YamlUtil
from common.redis_extract import read_redis


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()