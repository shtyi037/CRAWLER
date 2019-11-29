import urllib

url = "https://www.google.com/search?"
keyword = input("請輸入您需要搜尋的關鍵字")
wd = {"q":keyword}
wd = urllib.parse.urlencode(wd)
fullUrl = url+wd
print(fullUrl)