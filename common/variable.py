from common.yaml_util import YamlUtil


def variable():
    # �� extract.yml �ж�ȡ admin_user_15881086121 ��ֵ
    admin_user_value = YamlUtil().read_extract_yaml('admin_user_15881086121')
    # ��ȡ������������
    data = YamlUtil().read_testcase_yaml('get_token.yml')
    # �� admin_user_15881086121 ��ֵ�滻����������������
    data['get_token'][0]['requests']['data']['code'] = admin_user_value
    mes = YamlUtil().func_yaml(data)
    print(f"Result: {mes}")
    return [mes]
