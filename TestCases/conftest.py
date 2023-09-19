import pytest
from common.yaml_util import YamlUtil

# # 用于统计总的执行次数
# total_test_count = 0
#
# # 用于分隔线
# separator = '>' * 20
#
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_protocol(item, nextitem):
#     global total_test_count
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call':
#         total_test_count += 1
#         print_centered_ansi(f"\n{separator}这是第{total_test_count}条用例{separator}\n", '33')
#
#
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
    yield

