import requests
import openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(['id', 'folder', 'uid_id'])
raw = requests.get("https://soomgo.com/search/pro")
html = BeautifulSoup(raw.text, "html.parser")

num = 1
title = html.select("div.list-item a")

uid = []
for t in title:
    uid.append(t["href"].split('/')[3].split('?')[0])

num = 1

for i in range(1):
    user_info = requests.get("https://soomgo.com/profile/users/" + uid[
        i] + "?prev=searchPro&from=%EC%A7%80%EC%A0%95%EC%9A%94%EC%B2%AD%EC%84%9C")
    user_info_html = BeautifulSoup(user_info.text, "html.parser")

    image_url = user_info_html.select("div.profile-media-list")
    print(image_url)
    '''
    additional_info = user_info_html.select("div.profile-added-info li")
    for j in range(len(primary_info)):
        print(primary_info[j].text.strip())
        sheet.append([num,primary_info[j].text.strip(),'p',i+1])
        num += 1
    print("-" * 50)
    for j in range(len(additional_info)):
        print(additional_info[j].text.strip())
        sheet.append([num, additional_info[j].text.strip(), 'a', i+1])
        num += 1
    print("=" * 50)
    '''


