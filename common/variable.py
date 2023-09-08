from common.yaml_util import YamlUtil


def variable():
    # 从 extract.yml 中读取 admin_user_15881086121 的值
    key = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # 读取测试用例数据
    if key is None:
        # 如果提取数据为None，可以抛出异常或者返回一个默认值
        raise ValueError("admin_user_15881086121 is None")
    get_token = YamlUtil().read_testcase_yaml('get_token.yml')
    # 将 admin_user_15881086121 的值替换到测试用例数据中
    get_token['get_token'][0]['requests']['data']['code'] = key
    value = YamlUtil().func_yaml(get_token)
    print(f"Result: {value}")
    return [value]
