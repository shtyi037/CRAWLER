#貓眼url：http://maoyan.com/board/4?offset=0
import requests
import re
import json

#1)對URL發起HTTP請求http request,得到相應的http response響應，我們所需的數據就在
#response的響應體裡；
def get_one_page(URL):
    ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    response = requests.get(URL,headers=ua_headers)
    if response.status_code == 200:
      return response.text
    return None
#2)用正則表達式，XPath，BS4精確的獲取數據；
def parse_one_page(html):
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
def crawl_one_page(offset):
    # 拚出一個url
    url = "http://maoyan.com/board/4?offset="+str(offset)
    # 下載這個url
    html = get_one_page(url)
    # 解析每個頁面,並且把獲取到的item一個個寫入文件
    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == "__main__":        
    for i in range(10):
      crawl_one_page(i*10)


parse_one_page(get_one_page("http://maoyan.com/board/4?offset=0"))
