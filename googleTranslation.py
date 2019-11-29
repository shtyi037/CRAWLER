#GOOGLE翻譯:GET請求的交互模式

from urllib import request,parse

googleUrl = "https://translate.google.com.tw/?hl=zh-TW&tab=rT&authuser=0"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
          "x-client-data":"CJW2yQEIo7bJAQjEtskBCKmdygEI4qjKAQjLrsoBCM6wygEI6bHKAQjztMoBCPe0ygEYq6TKAQ==",
          "accept":"*/*",
          }

while True:
    key = input("請輸入要翻譯的英文,退出請輸入(CloseMe):")
    if key == "CloseMe":
        break

    formdata = {"client":"webapp",
                "sl":"en",
                "tl":"zh-TW",
                "hl":"zh-TW",
                "dt":"at",
                "dt":"bd",
                "dt":"ex",
                "dt":"ld",
                "dt":"md",
                "dt":"qca",
                "dt":"rw",
                "dt":"rm",
                "dt":"ss",
                "dt":"t",
                "source":"bh",
                "ssel":"0",
                "tsel":"0",
                "kc":"1",
                "tk":"90735.511728",
                "q":key
    }

    #做urlencode
    data = bytes(parse.urlencode(formdata), encoding="utf-8")
    req = request.Request(googleUrl, data, headers, method="POST")
    repsonse = request.urlopen(req)
    info = repsonse.read().decode("utf-8")
    print(info)