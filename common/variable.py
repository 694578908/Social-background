from common.yaml_util import YamlUtil


def variable():
    # �� extract.yml �ж�ȡ admin_user_15881086121 ��ֵ
    key = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # ��ȡ������������
    if key is None:
        # �����ȡ����ΪNone�������׳��쳣���߷���һ��Ĭ��ֵ
        raise ValueError("admin_user_15881086121 is None")
    get_token = YamlUtil().read_testcase_yaml('get_token.yml')
    # �� admin_user_15881086121 ��ֵ�滻����������������
    get_token['get_token'][0]['requests']['data']['code'] = key
    value = YamlUtil().func_yaml(get_token)
    print(f"Result: {value}")
    return [value]
