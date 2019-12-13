#貓眼url：http://maoyan.com/board/4?offset=0
'''
練習作業:
爬取貓眼電影名稱,主演,上映時間
使用:進程.lock.正則,
'''
import requests
import re
import json
import time
from multiprocessing import Pool,Manager
import functools


#1)對URL發起HTTP請求http request,得到相應的http response響應，我們所需的數據就在
#response的響應體裡；
MAXSLEEPTIME = 3
MINSLEEPTIME = 1
STAUS_OK = 200 #成功
MAX_PAGE_NUM = 10
##非200的範圍做處理
SERVER_ERROR_MIN = 500
SERVER_ERROR_MAX = 600
CLIENT_ERROR_MIN = 400
CLIENT_ERROR_MAX = 500

def get_one_page(URL, number = 5):
    if number == 0:
        return None
    ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    response = requests.get(URL,headers=ua_headers)
    if response.status_code == STAUS_OK:
        return response.text
    elif SERVER_ERROR_MIN < response.status_code < SERVER_ERROR_MAX:
        time.sleep(MINSLEEPTIME)
        get_one_page(URL,number-1)
    elif CLIENT_ERROR_MIN < response.status_code < CLIENT_ERROR_MAX:
         #真正好的做法是需要寫日誌
        if response.status_code == 404:
            print("Page not found") 
        elif response.status_code == 403:
            print("Have no rights")
        else:
            pass
    return None
#2)用正則表達式，XPath，BS4精確的獲取數據；
def parse_one_page(html):
    #抓取資料
    pattern = re.compile('<p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)
    for it in items:
      yield{
        "title":it[0].strip(),
        "actor":it[1].strip(),
        "time":it[2].strip()
      }


#3)存到本地的文件系統中或數據庫中；
def write_to_file(item):
    with open("貓眼.txt","a",encoding="utf-8") as f:
      f.write(json.dumps(item,ensure_ascii=False)+'\n')


#4)控制整個爬取一頁的流程
def crawl_one_page(lock, offset):
    # 拚出一個url
    url = "http://maoyan.com/board/4?offset="+str(offset)
    # 下載這個url
    html = get_one_page(url)
    # 解析每個頁面,並且把獲取到的item一個個寫入文件
    for item in parse_one_page(html):
        lock.acquire()
        write_to_file(item)
        lock.release()
    # time.sleep(random.randint(MINSLEEPTIME,MAXSLEEPTIME))

if __name__ == "__main__":
    #在進程池之間傳遞Lock需要使用Manager的Lock
    manager = Manager()
    lock = manager.Lock()
    
    #**使用偏函數對原來的函數進行一層包裝,得到一個包裝後的函數**
    #**使用包裝有傳參的優先順序問題:最優先傳入lock這個參數,在函式中,lock要第一個**
    partial_Crawl = functools.partial(crawl_one_page, lock)

    pool = Pool()#創建進程
    pool.map(partial_Crawl,[i*10 for i in range(10)])
    pool.close
    pool.join
#     for i in range(MAX_PAGE_NUM):
#       crawl_one_page(i*MAX_PAGE_NUM)


# parse_one_page(get_one_page("http://maoyan.com/board/4?offset=0"))
