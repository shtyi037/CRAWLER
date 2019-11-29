# 有道翻譯,POST請求的交互方式
from urllib import request, parse
import json

youdaoUrl = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
           "Accept": "application/json, text/javascript, */*; q=0.01",
           "X-Requested-With": "XMLHttpRequest"
           }

while True:
    key = input("請輸入要翻譯的英文,離開請輸入(CloseMe):")
    if key == "CloseMe":
        print("已離開")
        break
    formdata = {"i": key,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "15746842448475",
                "sign": "d1981ff8038a7469a915db46a9ffd96c",
                "ts": "1574684244847",
                "bv": "bc250de095a39eeec212da07435b6924",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlME",
                }
    #需要發送bytes類型的數據,所以要轉成bytes                
    data = bytes(parse.urlencode(formdata), encoding="utf-8")
    req = request.Request(youdaoUrl, data, headers, method="POST")
    # bytes -> json str
    repsonse = request.urlopen(req)
    info = repsonse.read().decode("utf-8")
    dicInfo = json.loads(info)
    print(dicInfo)
    translateResult = dicInfo['translateResult'][0][0]['tgt']
    print(translateResult)