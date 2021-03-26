import requests
from bs4 import BeautifulSoup
import openpyxl

cursor = ""
req = requests.get("https://api.soomgo.com/v1/search/pro?sort=review_count&keyword=&cursor="+cursor)
data = req.json()

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(['id','service','uid_id'])

raw = requests.get("https://soomgo.com/search/pro")
html = BeautifulSoup(raw.text, "html.parser")

num = 1
title = html.select("div.list-item a")

uid = []
for t in title:
    uid.append(t["href"].split('/')[3].split('?')[0])

num = 1

for i in range(len(uid)):
    print(num)
    user_info = requests.get("https://soomgo.com/profile/users/" + uid[
        i] + "?prev=searchPro&from=%EC%A7%80%EC%A0%95%EC%9A%94%EC%B2%AD%EC%84%9C")

    user_info_html = BeautifulSoup(user_info.text, "html.parser")

    service = user_info_html.select("div.profile-service-list li")

    for j in range(len(service)):
        print(service[j].text.strip())
        sheet.append([num,service[j].text.strip(),i+1])
        num += 1
    print("-" * 50)

wb.save('service.xlsx')