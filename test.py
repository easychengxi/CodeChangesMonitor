import time
import re
import requests
import datetime


web = 'https://www.ama-assn.org/practice-management/cpt/category-i-vaccine-codes'
proxies={
        "http": "http://68.114.205.121:443" #must use ""
        "https" "https://68.114.205.121:443"
    }
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
                    (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}     #设置headers信息，模拟成浏览器取访问网站
req = requests.get(web, headers=headers, proxies=proxies,allow_redirects=False)   #向网站发起请求，并获取响应对象
content = req.text   #获取网站源码
pattern = re.compile('<a href="https://www.ama-assn.org/(.*?)</a>').findall(content)

#print(content)


# for web in webs:
#     old_pattern = request(web)
#     time.sleep(3600)
#     # perform the get request and store it in a var
#     new_pattern = request(web)
#     if (new_pattern != old_pattern):  # 判断内容列表是否更新
#         # Take web screenshot
#         screenshot(web)
#         # sending emails out
#         SendEmail(web).emailout()
#
#     else:
#         now = datetime.datetime.now()
#         print(now, "%s has no updates" % web)

import time
import re
import requests
import datetime


def request(web):
    proxies={
        "http": "http://68.114.205.121:443" #must use ""
        "https" "https://68.114.205.121:443"
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
                    (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}     #设置headers信息，模拟成浏览器取访问网站
    req = requests.get(web, headers=headers, proxies=proxies,allow_redirects=False)   #向网站发起请求，并获取响应对象
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
              # re.compile('<a href = "https://www.ama-assn.org/system/files/(.*?)</a>').findall(content) + \
    return pattern  #运行qingqiu()函数，会返回pattern的值


webs = {'https://www.cms.gov/Medicare/Coding/HCPCSReleaseCodeSets/HCPCS-Quarterly-Update',
        'https://www.cms.gov/Medicare/Coding/ICD10',
        'https://www.cms.gov/medicare/icd-10/2022-icd-10-cm',
        'https://www.cms.gov/medicare/icd-10/2022-icd-10-pcs',
        'https://www.ama-assn.org/practice-management/cpt',
        'https://www.ama-assn.org/practice-management/cpt/category-i-vaccine-codes',
        'https://www.ama-assn.org/practice-management/cpt/category-iii-codes',
        'https://www.ama-assn.org/practice-management/cpt/cpt-pla-codes',
        'https://www.cms.gov/Medicare/Coding/HCPCSReleaseCodeSets/Alpha-Numeric-HCPCS'
        }
#Assign patterns as old patterns
old_patterns = {}
new_patterns = {}
for web in webs:
    old_patterns.update({web: request(web)})

#time.sleep(3600)

for web in webs:
    new_patterns.update({web: request(web)})

diffkeys = [k for k in new_patterns if new_patterns[k] != old_patterns[k]]
if diffkeys !=[]:
    #Take web screenshot
    screenshot(web)
    # sending emails out
    SendEmail(web).emailout()
else:
    now = datetime.datetime.now()
    print(now, "%s has no updates" % web)

    # if (new_pattern != old_pattern):  # 判断内容列表是否更新
    #     # Take web screenshot
    #     screenshot(web)
    #     # sending emails out
    #     SendEmail(web).emailout()
    #
    # else:
    #     now = datetime.datetime.now()
    #     print(now, "%s has no updates" % web)


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

#pattern = re.compile('<a href="https://www.ama-assn.org/(.*?)</a>').findall(content) + \


    #运行qingqiu()函数，会返回pattern的值


#request('https://www.ama-assn.org/practice-management/cpt/category-i-vaccine-codes')