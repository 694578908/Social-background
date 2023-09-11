from common.yaml_util import YamlUtil


def variable_code():
    # �� extract.yml �ж�ȡ admin_user_15881086121 ��ֵ
    code_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # ��ȡ������������
    if code_value is None:
        # �����ȡ����ΪNone�������׳��쳣���߷���һ��Ĭ��ֵ
        raise ValueError("admin_user_15881086121 is None")
    data = YamlUtil().read_testcase_yaml('get_token.yml')
    # �� admin_user_15881086121 ��ֵ�滻����������������
    data['get_token'][0]['requests']['data']['code'] = code_value
    value = YamlUtil().func_yaml(data)
    print(f"Result: {value}")
    return [value]


def variable_token():
    # �� extract.yml �ж�ȡ admin_user_15881086121 ��ֵ
    code_value = YamlUtil().read_extract_yaml('token')
    # ��ȡ������������
    if code_value is None:
        # �����ȡ����ΪNone�������׳��쳣���߷���һ��Ĭ��ֵ
        raise ValueError("token is None")
    data = YamlUtil().read_testcase_yaml('get_token.yml')
    # �� token ��ֵ�滻����������������
    data['collection'][0]['requests']['headers']['Authorization'] = code_value
    value = YamlUtil().func_yaml(data)
    print(f"Result: {value}")
    return [value]

# def variable():
#     # �� extract.yml �ж�ȡ��Ҫ�滻��ֵ
#     code_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
#
#     # ��ʼ�� token Ϊ None
#     token_value = None
#     # ��ȡ������������
#     get_token = YamlUtil().read_testcase_yaml('get_token.yml')
#     # ���������������滻��Ҫ�滻��ֵ
#     for case in get_token['get_token']:
#         if 'data' in case['requests']:
#             if 'code' in case['requests']['data']:
#                 case['requests']['data']['code'] = code_value
#     # ��� 'token' �Ƿ������ extract.yml �У�������ڣ��ٽ����滻
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
