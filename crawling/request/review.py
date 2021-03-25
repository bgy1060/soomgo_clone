import requests
from bs4 import BeautifulSoup
import openpyxl
import pymysql.cursors

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(['id','point','Content','reviewResponse','date','reviewer','uid_id'])
raw = requests.get("https://soomgo.com/search/pro")
html = BeautifulSoup(raw.text, "html.parser")

num = 1
title = html.select("div.list-item a")

uid = []
for t in title:
    uid.append(t["href"].split('/')[3].split('?')[0])


for i in range(20):
    req = requests.get("https://api.soomgo.com/v2/user/" + uid[i] + "/profile?role=provider&is_read_counting=true")
    data = req.json()

    reviewer = data['response']['recentReview']

    for j in range(len(reviewer['data'])):
        print(num)
        point = int(reviewer['data'][j]['reviewRating'])
        content = reviewer['data'][j]['contents'].replace("'","").replace("\n"," ")
        date = reviewer['data'][j]['createdAt']
        reviewer_name = reviewer['data'][j]['userName']

        print(reviewer['data'][j]['id'])
        print(reviewer_name)
        print(point)
        print(content)
        try:
            print(reviewer['data'][j]['comments'][0]['contents'])
            reviewResponse = reviewer['data'][j]['comments'][0]['contents'].replace("'","")
        except:
            print(reviewer['data'][j]['comments'])
            reviewResponse = ""
        print(date)

        print("=" * 50)
        sheet.append([num, point, content, reviewResponse, date, reviewer_name, i+1])
        num += 1

    after = str(reviewer['after'])

    while after != str(-1):

        more_review = requests.get(
                'https://api.soomgo.com/v1/user/246964/review?after=' + after + '&limit=3&role=provider')
        more_review_data = more_review.json()

        for k in range(len(more_review_data['data'])):
            print(num)
            point = int(more_review_data['data'][k]['reviewRating'])
            content = more_review_data['data'][k]['contents'].replace("'","")
            date = more_review_data['data'][k]['createdAt']
            reviewer_name = more_review_data['data'][k]['userName']

            print(more_review_data['data'][k]['id'])
            print(reviewer_name)
            print(point)
            print(content)
            try:
                print(more_review_data['data'][k]['comments'][0]['contents'])
                reviewResponse = more_review_data['data'][k]['comments'][0]['contents'].replace("'","")

            except:
                print(more_review_data['data'][k]['comments'])
                reviewResponse = ""
            print(date)

            print("=" * 50)
            num += 1

            sheet.append([num, point, content, reviewResponse, date, reviewer_name, i+1])

        after = str(more_review_data['after'])


wb.save("review_total.xlsx")
print("끝!")
