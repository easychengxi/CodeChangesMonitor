#Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
from emailing import SendEmail
from webscreen import screenshot
import time
import re
import requests
import datetime
import smtplib


# web = 'http://localhost:8888/notebooks/Documents/Python%20Scripts/Web%20Monitor.ipynb'
# # setting the URL you want to monitor
# url = Request(web,
#               headers={'User-Agent': 'Mozilla/5.0'})

def request(web):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
                    (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}     #设置headers信息，模拟成浏览器取访问网站
    req = requests.get(web, headers=headers)   #向网站发起请求，并获取响应对象
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

    pattern = re.compile('href="/files/(.*?)</a>').findall(content) + \
              re.compile('<a href="/Medicare/Coding/ICD10/(.*?)</a>').findall(content) + \
              re.compile('<a href="/practice-management/cpt/(.*?)</a>').findall(content) + \
              re.compile('<a href="https://www.ama-assn.org/(.*?)</a>').findall(content)
    return pattern  #运行qingqiu()函数，会返回pattern的值


def monitor(web):
    print("running")
    old_pattern = request(web)
    time.sleep(3600)
    while True:
        try:
            # perform the get request and store it in a var
            new_pattern = request(web)
            if (new_pattern != old_pattern):  # 判断内容列表是否更新
                #pass new_pattern to old
                old_pattern = new_pattern
                #Take web screenshot
                screenshot(web)
                #sending emails out
                SendEmail(web).emailout()

            else:
                now = datetime.datetime.now()
                print(now,"No updates")
            time.sleep(3600) # check every hour


        # To handle exceptions
        except Exception as e:
            print(e)
            break

