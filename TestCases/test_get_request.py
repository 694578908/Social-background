import pytest
import json
from common.yaml_util import YamlUtil
from common.redis_extract import read_redis
from common.request_util import RequestUtil
import jsonpath
from common import log_util
from common.variable import variable_code, variable_token


class TestRequest:

    # @pytest.mark.smoke
    # 登录账号密码
    @pytest.mark.parametrize('case', YamlUtil().read_testcase_yaml('get_token.yml')['login'])
    def test_case_login(self, case):
        if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
            if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                    and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
                print(case['name'])
                print(case['validate'])
                headers = case['requests']['headers']
                url = case['requests']['url']
                data = case['requests']['data']
                method = case['requests']['method']
                result = RequestUtil().send_requests(method, url, headers, data)
                res = (json.loads(result))
                log_util.log_info('用例标题:{},请求地址为:{}, 请求参数为:{}'.format(case['name'], url, data))
                log_util.log_info('实际结果接口返回信息为:{}'.format(result))
                read_redis()  # 调取redis并把验证码写入extract.yml文件里
                log_util.log_info('预期结果：code 应为: {}'.format(case['validate'][0]['equals']['code']))
                assert res['code'] == case['validate'][0]['equals']['code']

            else:
                print("在yml文件requests目录下必须要有method,url,data")
        else:
            print("yml一级关键字必须包含:name,requests,validate")

    # 提交验证码
    def test_case_gettoken(self):
        data = variable_code()
        value = data[0]['get_token']
        for case in value:
            if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
                if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                        and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
                    print(case['name'])
                    print(case['validate'])
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

    # 创建藏品
    def test_case_collection(self):
        data = variable_token()
        value = data[0]['collection']
        for case in value:
            print(case)
            if 'name' in case.keys() and 'requests' in case.keys() and 'validate' in case.keys():
                if jsonpath.jsonpath(case, '$..url') and jsonpath.jsonpath(case, '$..method') \
                        and jsonpath.jsonpath(case, '$..data') and jsonpath.jsonpath(case, '$..headers'):
                    print(case['name'])
                    print(case['validate'])
                    headers = case['requests']['headers']
                    url = (case['requests']['url'])
                    method = (case['requests']['method'])
                    data = (case['requests']['data'])
                    result = RequestUtil().send_requests(method, url, headers, data)
                    res = json.loads(result)
                    log_util.log_info('用例标题:{},请求地址为:{}, 请求参数为:{}'.format(case['name'], url, data))
                    log_util.log_info('实际结果接口返回信息为:{}'.format(result))
                    log_util.log_info('预期结果：code 应为: {}'.format(case['validate'][0]['equals']['code']))
                    assert res['code'] == case['validate'][0]['equals']['code']
                else:
                    print("在yml文件requests目录下必须要有method,url,data,headers")
            else:
                print("yml一级关键字必须包含:name,requests,validate")


#     # 编辑藏品
#     def test_case_editcollection(self):
#         url = 'higher8pre.douxiangapp.com/dboxAdmin/v1/nft/10000148'
#         data = {"id": "10000148", "title": "编辑自动化测试", "selfCode": "null","description":"编辑自动化测试",
#                 "mainImg":"https://dboximg.douxiangapp.com/img/nft/1692963675800.png","displayImgs":["https://dboximg.douxiangapp.com/img/nft/1692963680385.png"],
#                 "authorId":16,"authorName":"中传云创（成都）文化发展有限公司",
#                 "authorHeadimg":"https://dboximg.douxiangapp.com/nftProd/img/nft/1660735513767.png_720x720q90g.jpg",
#                 "publishId":7,"publishName":"四川天眼网络科技有限公司","publishHeadimg":"https://dboximg.douxiangapp.com/nftProd/img/nft/1660735878572.png",
#                 "detailImgs":["https://dboximg.douxiangapp.com/video/20230825/20230825194127_pvr4.png",
#                               "https://dboximg.douxiangapp.com/video/20230825/20230825194135_9u4c.png",
#                               "https://dboximg.douxiangapp.com/video/20230825/20230825194137_4x5s.png",
#                               "https://dboximg.douxiangapp.com/video/20230825/20230825194139_oaga.png",
#                               "https://dboximg.douxiangapp.com/video/20230825/20230825194141_pe5i.png"],
#                 "price":0.01,"stock":10,"limitStock":13,"publishTime":"2023-08-23 10:16:34","sort":0,"tags":["12","自动化测试标签"],
#                 "categories":[[{"categoryId":"727","level":1,"name":"盖亚巨龙"},{"categoryId":"728","level":2,"name":"盖亚巨龙"}]],
#                 "isOnline":1,"saledNum":0,"openSell":"true","sellCloseDay":0,"openSend":"true","sendCloseDay":0,"showType":1,"zipName":"null",
#                 "canBuy":1,"marketingRightsCard":"null","isGiveGift":0,"rightsCardId":"null","giftType":1,"giftId":"null","isPriorityBuy":0,
#                 "priorityTimes":"null","priorityDate":"null","distribution":1,"distributionProportion":"null","numRandom":1,"extraStock":33,
#                 "limitUser":0,"surplusStock":43,"firstStock":10,"firstExtraStock":33,"displayStock":5555,"initialStock":43,
#                 "lowerShelfCooling":1,"shelfTime":"null","blockChain":0,"openExclusiveBuy":0,"nftExclusiveBuyDTOS":[],
#                 "marketStatus":"null","serviceRate":0,"marketMaintainStatus":"false","marketMaintainStart":"null","marketMaintainEnd":"null",
#                 "resellFixedPriceStatus":0,"fixedPriceBasis":0,"calculationFormula":0,"minFixedPrice":0,"maxFixedPrice":0,"dataClear":"false",
#                 "resellInterdiction":"false","dayExemptFrequency":"null","firstGetInterdiction":0,"marketGetInterdiction":0,"sellForbidden":0,
#                 "sendCloseTime":0,"publishEndTime":"2130-01-01 00:00:00","isOpen":0,"holdLimitStock":0,"limitBrush":1,"timesMode":1,
#                 "openDiscount":1,"discountMode":1,"holdPictures":[],
#                 "nftRepertorySeparationVo":{"ordinaryRepertory":"null","pictureRepertory":"null","exclusiveRepertory":"null","ordinaryCurrentRepertory":"null",
#                                             "pictureCurrentRepertory":"null","exclusiveCurrentRepertory":"null","ordinaryRepertorySold":"null",
#                                             "pictureRepertorySold":"null","exclusiveRepertorySold":"null","stockSold":"0"},
#                 "branchWarehouse":2,"num":0,"isShow":0,"nftNumber":"","levelId":51,"levelName":"null","lifeMode":1,"isBind":0,
#                 "nftAttrs":[{"attrId":1,"attrValue":1000,"attrInitValue":1000,"attr_name":"精力值"}],
#                 "holdCount":"null","circulationNum":"null","openPrivilege":"fasle","displayPngImgs":"null","unitImgs":"","unitImgList":"null",
#                 "exchangeTimeOpen":0,"exchangeTime":0,"prizeGiftList":[],"nftType":3,"numberOfHolders":0,"salesNum":0,"pages":"null",
#                 "chainSeriesDTO":"null","displayLevel":1,"chainSeriesId":"0","limitType":0,"limitRule":[],
#                 "limitLevels":[{"levelId":1,"isChoose":"null","levelName":"null","levelType":"null"},{"levelId":2,"isChoose":"null","levelName":"null","levelType":"null"},
#                                {"levelId":3,"isChoose":"null","levelName":"null","levelType":"null"},{"levelId":4,"isChoose":"null","levelName":"null","levelType":"null"},
#                                {"levelId":5,"isChoose":"null","levelName":"null","levelType":"null"},{"levelId":6,"isChoose":"null","levelName":"null","levelType":"null"},
#                                {"levelId":1001,"isChoose":"null","levelName":"null","levelType":"null"},{"levelId":1002,"isChoose":"null","levelName":"null","levelType":"null"},
#                                {"levelId":1003,"isChoose":"null","levelName":"null","levelType":"null"},{"levelId":1004,"isChoose":"null","levelName":"null","levelType":"null"},
#                                {"levelId":1005,"isChoose":"null","levelName":"null","levelType":"null"},{"levelId":1006,"isChoose":"null","levelName":"null","levelType":"null"},
#                                {"levelId":1007,"isChoose":"null","levelName":"null","levelType":"null"}],"limitNfts":[],
#                 "integral":[{"createTime":"null","id":"null","prizeId":"null","integralType":2,"isShow":"false","grantNum":"null","prizeTitle":"null","prizeImg":"null",
#                              "prizeExtraStock":"null"},{"createTime":"null","id":"null","prizeId":"null","integralType":3,"isShow":"false","grantNum":"null",
#                                                       "prizeTitle":"null","prizeImg":"null","prizeExtraStock":"null"},{"createTime":"null","id":"null","prizeId":"null",
#                                                                                                                  "integralType":4,"isShow":"false","grantNum":"null",
#                                                                                                                  "prizeTitle":"null","prizeImg":"null","prizeExtraStock":"null"},
#                             {"createTime":"null","id":"null","prizeId":"null","integralType":5,"isShow":"null","grantNum":"null","prizeTitle":"null","prizeImg":"null",
#                              "prizeExtraStock":"null"},{"createTime":"null","id":"null","prizeId":"null","integralType":6,"isShow":"false","grantNum":"null",
#                                                       "prizeTitle":"null","prizeImg":"null","prizeExtraStock":"null"}],"raceId":"null","factionsId":"null",
#                 "compoundCoolingShow":0,"compoundCoolingTime":"null","nftProductionDisposition":[{"productMaterials":1,"orderNum":1}],"mainImageDisplay":0,
#                 "supplementaryType":1,"nftPowerConfig":{"gameInstructions":"0","maxPower":0,"initPower":0,"consume":0},
#                 "nftPlunderDisposition":"null","consumeMode":1,"nftAttrConfig":"null","recommend":"null","ordinaryRepertory":"null",
#                 "pictureRepertory":"null","exclusiveRepertory":"null"}
#         response = requests.request("put", url=url, json=data)
#         print(response.json())
#         assert response.json()['code'] == 0
