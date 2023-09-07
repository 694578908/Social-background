from common.yaml_util import YamlUtil


def variable():
    # 从 extract.yml 中读取 admin_user_15881086121 的值
    admin_user_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # 读取测试用例数据
    data = YamlUtil().read_testcase_yaml('get_token.yml')
    # 将 admin_user_15881086121 的值替换到测试用例数据中
    data['get_token'][0]['requests']['data']['code'] = admin_user_value
    mes = YamlUtil().func_yaml(data)
    print(f"Result: {mes}")
    return [mes]
