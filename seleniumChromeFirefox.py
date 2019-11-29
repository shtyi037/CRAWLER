from selenium import webdriver
import time
import urllib

#Chrome
# driver = webdriver.Chrome()
# driver.get("https://www.google.com.tw/")
# search_input = driver.find_element_by_name("q")
# search_input.send_keys('python is awesome')
# start_search_btn = driver.find_element_by_name("btnK")
# start_search_btn.click()

# with open("ChromeSearch.html", "wb") as f:
#     f.write(driver.page_source.encode("utf-8"))


# time.sleep(5)
# driver.quit()
# driver.close()


#Firefox
# driver = webdriver.Firefox()
# driver.get("http://www.bing.com")
# time.sleep(2)
# driver.find_element_by_id('sb_form_q').send_keys('python')
# driver.find_element_by_id('sb_form_go').click()
# with open("bingSearch.html", "wb") as f:
#     f.write(driver.page_source.encode("utf-8"))
# time.sleep(5)

# driver.quit()
# driver.close()


#自動登入帳號密碼
# driver = webdriver.Firefox()
# driver.get("http://www.renren.com/")
# driver.find_element_by_id('email').send_keys('yyyy')        # 用戶名
# driver.find_element_by_id('password').send_keys('xxxxxxxx') # 密碼
# driver.find_element_by_id('login').click()



#cookie
#anonymid=jhlopkol7jjtbs; depovince=BJ; jebecookies=598ed5ea-874b-4d3c-8cd4-be09fe30b407|||||; _r01_=1; JSESSIONID=abc1qnh7W5WwRc0b5vwow; ick_login=723cae2a-c57b-400f-93e1-3c2b006de3d4; jebe_key=b43d7595-4355-434f-bd34-411ed0e3a7b9%7C65617699d9107c4fa92a82edbc369e2a%7C1527236707731%7C1%7C1527236506627; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; _de=7113E26C6AAF3646A83FD76533146E3C; p=618fd9a4f10e78c0189b16848a0462be9; t=d455a8e8e214d69f3e72c64123d059b49; societyguester=d455a8e8e214d69f3e72c64123d059b49; id=961482489; xnsid=6999487e; ch_id=10016; wp_fold=0
# url = "http://www.renren.com/961482489/profile"

# ua_headers = {"Cookie":"anonymid=jhlopkol7jjtbs; depovince=BJ; jebecookies=598ed5ea-874b-4d3c-8cd4-be09fe30b407|||||; _r01_=1; JSESSIONID=abc1qnh7W5WwRc0b5vwow; ick_login=723cae2a-c57b-400f-93e1-3c2b006de3d4; jebe_key=b43d7595-4355-434f-bd34-411ed0e3a7b9%7C65617699d9107c4fa92a82edbc369e2a%7C1527236707731%7C1%7C1527236506627; first_login_flag=1; ln_uact=18210577472; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; _de=7113E26C6AAF3646A83FD76533146E3C; p=618fd9a4f10e78c0189b16848a0462be9; t=d455a8e8e214d69f3e72c64123d059b49; societyguester=d455a8e8e214d69f3e72c64123d059b49; id=961482489; xnsid=6999487e; ch_id=10016; wp_fold=0",
#               "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
#               "Connection":"keep-alive",
#               "Host":"www.renren.com"
#               }

# req = urllib.request.Request(url, headers=ua_headers)
# response = urllib.request.urlopen(req)

# with open("myRenren.html", "wb") as f:
#     f.write(response.read())
