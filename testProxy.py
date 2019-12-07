import urllib
import re


def chechProxy(proxy_addr):
    data = ""
    url = "http://www.baidu.com"
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    #替換handler,實現可以處理Proxy
    opener = urllib.request.build_opener(proxy)
    #把opener裝載進urllib庫中,準備使用
    urllib.request.install_opener(opener)
    try:
        response = urllib.request.urlopen(url, timeout=10)   
        data = response.read().decode('utf-8')
    except:
        pass
    
    pattern = re.compile("<title>百度一下，你就知道</title>")
    title = re.findall(pattern, data)
    print(title)
    #list的長度為0,代表沒有獲取到訊息
    if len(title) == 0:
        return False
    else:
        return True
    
print(chechProxy("185.106.121.98:1080"))
                 #"name:password@ip:port"    





