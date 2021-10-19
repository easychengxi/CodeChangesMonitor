import time
import re
import requests
from webscreen import screenshot
from emailing import SendEmail
import datetime
import random
from fake_useragent import UserAgent
import http.client

def request(web):
    http.client._MAXLINE = 1000000
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
    #                 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}     #设置headers信息，模拟成浏览器取访问网站

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    headers['User-Agent'] = random.choice(user_agent_list)

    req = requests.get(web, headers=headers, allow_redirects=False,timeout=None)   #向网站发起请求，并获取响应对象
    content = req.text   #获取网站源码
    #'href="/files/(.*?)</a>'
    # https://www.cms.gov/Medicare/Coding/HCPCSReleaseCodeSets/HCPCS-Quarterly-Update \
    # https://www.cms.gov/medicare/icd-10/2022-icd-10-cm \
    # https://www.cms.gov/medicare/icd-10/2022-icd-10-pcs

    #'<a href="/Medicare/Coding/ICD10/(.*?)</a>'
    # https://www.cms.gov/Medicare/Coding/ICD10

    #'<a href="/practice-management/cpt/(.*?)</a>'
    # https://www.ama-assn.org/practice-management/cpt

    #'<a href="https://www.ama-assn.org/(.*?)</a>'
    # https://www.ama-assn.org/practice-management/cpt/category-i-vaccine-codes \
    # https://www.ama-assn.org/practice-management/cpt/category-iii-codes \
    # https://www.ama-assn.org/practice-management/cpt/cpt-pla-codes

    # '<td headers=(.*?)</a>'
    #https: // www.cms.gov / Medicare / Coding / HCPCSReleaseCodeSets / Alpha - Numeric - HCPCS

    pattern = re.compile('href="/files/(.*?)</a>').findall(content) + \
              re.compile('<a href="/Medicare/Coding/ICD10/(.*?)</a>').findall(content) + \
              re.compile('<a href="/practice-management/cpt/(.*?)</a>').findall(content) + \
              re.compile('<a href="https://www.ama-assn.org/(.*?)</a>').findall(content) + \
              re.compile('<td headers=(.*?)</a>').findall(content)
    return pattern  #运行qingqiu()函数，会返回pattern的值


def monitor(webs):
    print("running")
    while True:
        try:
            for web in webs:
                old_pattern = request(web)
                time.sleep(3600)
                # perform the get request and store it in a var
                new_pattern = request(web)
                if (new_pattern != old_pattern):  # 判断内容列表是否更新
                    #Take web screenshot
                    screenshot(web)
                    #sending emails out
                    SendEmail(web).emailout()

                else:
                    now = datetime.datetime.now()
                    print(now,"%s has no updates"%web)



        # To handle exceptions
        except Exception as e:
            print(e)
            break

