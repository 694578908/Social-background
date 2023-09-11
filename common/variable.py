from common.yaml_util import YamlUtil


def variable_code():
    # 从 extract.yml 中读取 admin_user_15881086121 的值
    code_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # 读取测试用例数据
    if code_value is None:
        # 如果提取数据为None，可以抛出异常或者返回一个默认值
        raise ValueError("admin_user_15881086121 is None")
    data = YamlUtil().read_testcase_yaml('get_token.yml')
    # 将 admin_user_15881086121 的值替换到测试用例数据中
    data['get_token'][0]['requests']['data']['code'] = code_value
    value = YamlUtil().func_yaml(data)
    print(f"Result: {value}")
    return [value]


def variable_token():
    # 从 extract.yml 中读取 admin_user_15881086121 的值
    code_value = YamlUtil().read_extract_yaml('token')
    # 读取测试用例数据
    if code_value is None:
        # 如果提取数据为None，可以抛出异常或者返回一个默认值
        raise ValueError("token is None")
    data = YamlUtil().read_testcase_yaml('get_token.yml')
    # 将 token 的值替换到测试用例数据中
    data['collection'][0]['requests']['headers']['Authorization'] = code_value
    value = YamlUtil().func_yaml(data)
    print(f"Result: {value}")
    return [value]

# def variable():
#     # 从 extract.yml 中读取需要替换的值
#     code_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
#
#     # 初始化 token 为 None
#     token_value = None
#     # 读取测试用例数据
#     get_token = YamlUtil().read_testcase_yaml('get_token.yml')
#     # 遍历测试用例，替换需要替换的值
#     for case in get_token['get_token']:
#         if 'data' in case['requests']:
#             if 'code' in case['requests']['data']:
#                 case['requests']['data']['code'] = code_value
#     # 检查 'token' 是否存在于 extract.yml 中，如果存在，再进行替换
#     if 'token' in get_token:
#         token_value = YamlUtil().read_extract_yaml('token')
#         if token_value is not None:
#             for case in get_token['collection']:
#                 if 'requests' in case and 'headers' in case['requests']:
#                     headers = case['requests']['headers']
#                     if 'Authorization' in headers:
#                         headers['Authorization'] = headers['Authorization'].format(token_value)
#     value = YamlUtil().func_yaml(get_token)
#     print(f"Result: {value}")
#     return [value]
