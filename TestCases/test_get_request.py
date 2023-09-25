import json
import jsonpath
import pytest
from common import log_util
from common.redis_extract import read_redis
from common.request_util import RequestUtil
from common.variable import variable_token, variable_code
from common.yaml_util import YamlUtil
from common.count import count
import allure


@allure.epic("龙之岛商家后台")
class TestRequest:

    def set_dynamic_title(self, case):
        allure.dynamic.title(case['name'])

    # 登录账号密码
    @allure.feature("登录账号密码")
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('case_data.yml')['login'])
    def test_case_login(self, case):
        count(case)  # 打印用例执行次数
        if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
            if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                    and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
                self.set_dynamic_title(case)
                headers = case['requests']['headers']
                url = case['requests']['url']
                data = case['requests']['data']
                method = case['requests']['method']
                result = RequestUtil().send_requests(method, url, headers, data)
                res = (json.loads(result))
                read_redis()  # 调取redis并把验证码写入extract.yml文件里
                log_util.log_info('用例标题:{},请求地址为:{}, 请求参数为:{}'.format(case['name'], url, data))
                log_util.log_info('实际结果接口返回信息为:{}'.format(result))
                log_util.log_info('预期结果：code 应为: {}'.format(case['validate'][0]['equals']['code']))
                assert res['code'] == case['validate'][0]['equals']['code']
            else:
                print("在yml文件requests目录下必须要有method,url,data")
        else:
            print("yml一级关键字必须包含:name,requests,validate")

    # 提交验证码
    @allure.feature("提交验证码")
    def test_case_gettoken(self):
        data = variable_code()
        value = data[0]['code_token']
        for case in value:
            count(case)  # 打印用例执行次数
            if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
                if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                        and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
                    self.set_dynamic_title(case)
                    headers = case['requests']['headers']
                    url = (case['requests']['url'])
                    method = (case['requests']['method'])
                    data = (case['requests']['data'])
                    result = RequestUtil().send_requests(method, url, headers, data)
                    res = (json.loads(result))
                    log_util.log_info('用例标题:{},请求地址为:{}, 请求参数为:{}'.format(case['name'], url, data))
                    log_util.log_info('实际结果接口返回信息为:{}'.format(result))
                    message = json.loads(result)['message']
                    YamlUtil().write_extract_yaml({'token': message})
                    log_util.log_info('预期结果：code 应为: {}'.format(case['validate'][0]['equals']['code']))
                    assert res['code'] == case['validate'][0]['equals']['code']
                else:
                    print("在yml文件requests目录下必须要有method,url,data,headers")
            else:
                print("yml一级关键字必须包含:name,requests,validate")

    @allure.feature("功能模块")
    def test_case_nft(self):
        data = variable_token()
        value = data[0]['nft']
        for case in value:
            count(case)  # 打印用例执行次数
            if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
                if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                        and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
                    self.set_dynamic_title(case)
                    headers = case['requests']['headers']
                    url = (case['requests']['url'])
                    method = (case['requests']['method'])
                    data = (case['requests']['data'])
                    result = RequestUtil().send_requests(method, url, headers, data)
                    res = (json.loads(result))
                    log_util.log_info('用例标题:{},请求地址为:{}, 请求参数为:{}'.format(case['name'], url, data))
                    log_util.log_info('实际结果接口返回信息为:{}'.format(result))
                    log_util.log_info('预期结果：code 应为: {}'.format(case['validate'][0]['equals']['code']))

                    with allure.step("检查接口返回的 code"):
                        allure.attach(f"实际 code: {res['code']}", name="实际 code")
                        allure.attach(f"预期 code: {case['validate'][0]['equals']['code']}", name="预期 code")
                        assert res['code'] == case['validate'][0]['equals']['code']
                    with allure.step("附件：接口请求参数和响应"):
                        allure.attach(str(data), name="请求参数")
                        allure.attach(result, name="接口响应")
                else:
                    print("在yml文件requests目录下必须要有method,url,data,headers")
            else:
                print("yml一级关键字必须包含:name,requests,validate")
