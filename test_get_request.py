import requests
import pytest

class TestRequest:
    #全局变量
    token = ''
    def test_case_login(self):
        url = "http://higher8pre.douxiangapp.com/dboxAdmin/v1/security/manageLogin"
        data = {"userName": "zqj", "pwd": "123456"}
        response = requests.post(url=url, json=data)
        print(response.json())
        TestRequest.token = response.json()['data']
        assert response.status_code == 200

    def test_case_collection(self):
        url = "http://higher8pre.douxiangapp.com/dboxAdmin/v1/nft"
        data = {"supplementaryType":1,"mainImageDisplay":0,"nftType":3,"isOnline":1,
        "canBuy":1,"numRandom":1,"openSend":"true","sendCloseTime":0,"sort":0,"title":"测试",
        "description":"123","mainImg":"https://dboximg.douxiangapp.com/img/nft/1692756890755.jpg",
        "displayImgs":["https://dboximg.douxiangapp.com/img/nft/1692756926707.png"],
        "authorHeadimg":"https://dboximg.douxiangapp.com/nftProd/img/nft/1672022615423.png",
        "authorId":15,"authorName":"龙之岛DOD","publishId":5,"publishHeadimg":
        "https://dboximg.douxiangapp.com/nftProd/img/nft/1672021311005.png",
        "publishName":"龙之岛DOD","detailImgs":["https://dboximg.douxiangapp.com/video/20230823/20230823101529_butf.png"],
        "tags":["12"],"price":0.01,"firstStock":"","stock":10,"limitStock":12,"publishTime":"2023-08-23 10:16:34",
        "categories":[[{"categoryId":"707","level":1,"name":"其他"},{"categoryId":"708","level":2,"name":"其他"}]],
        "openSell":"true","sellCloseDay":0,"isPriorityBuy":0,"priorityDate":"","priorityTimes":"","isGiveGift":0,"giftType":1,
        "showType":1,"giftId":"","distribution":1,"distributionProportion":"","holdPictures":[],"isOpen":0,"extraStock":33,
        "lowerShelfCooling":1,"openExclusiveBuy":0,"sellForbidden":0,"firstGetInterdiction":0,"marketGetInterdiction":0,
        "resellFixedPriceStatus":0,"fixedPriceBasis":0,"calculationFormula":0,"publishEndTime":"2023-08-24 00:00:00",
        "displayLevel":1,"limitUser":0,"displayStock":22,"branchWarehouse":2,"ordinaryRepertory":12,"pictureRepertory":12,
        "exclusiveRepertory":32,"limitBrush":1,"timesMode":1,"openDiscount":1,"discountMode":1,"nftRepertorySeparationVo":{},
        "levelId":0,"nftAttrs":[{"attrId":1,"attrValue":100,"attrInitValue":100,"attr_name":"精力值"}],
        "chainSeriesDTO":{"chainUnitDTOS":[],"templateImg":"","raceId":1},"limitRule":[],"limitType":0,"exchangeTimeOpen":0,
        "prizeGiftList":[],"integral":[{"integralType":2,"isShow":'false',"name":"电池配置"},{"integralType":3,"isShow":'false',"name":"砖块配置"},
                                       {"integralType":4,"isShow":'false',"name":"龙精配置"},{"integralType":5,"isShow":'false',"name":"金蛋配置"},
                                       {"integralType":6,"isShow":'false',"name":"龙珠配置"},{"integralType":7,"isShow":'false',"name":"龙核配置"},
                                       {"integralType":8,"isShow":'false',"name":"龙鳞配置"},{"integralType":9,"isShow":'false',"name":"龙血配置"},
                                       {"integralType":10,"isShow":'false',"name":"龙晶配置"},{"integralType":11,"isShow":'false',"name":"渣渣辉配置"},
                                       {"integralType":12,"isShow":'false',"name":"星石配置"},{"integralType":13,"isShow":'false',"name":"材料12配置"},
                                       {"integralType":14,"isShow":'false',"name":"材料13配置"},{"integralType":15,"isShow":'false',"name":"材料14配置"}],
        "nftProductionDisposition":[{"productMaterials":1,"currency":1,"orderNum":1}],"nftPowerConfig":{},
        "nftPlunderDisposition":{"durabilityLimit2":0,"durabilityLimit":0,"energy":0,"physicalPowerScore":0,"lifeScore":0},
        "nftAttrConfig":{"attrType":6,"nftAttrConfigCostBOS":[]},"lifeMode":1,"consumeMode":1}

        headers = {'Accept': 'application/json, text/plain','Accept-Language': 'zh-CN,zh;q=0.9','Authorization': TestRequest.token}

        response = requests.post(url=url,json=data,headers=headers)
        print(response.json())


    if __name__ == "__main__":
        pytest.main(['-vs'])

