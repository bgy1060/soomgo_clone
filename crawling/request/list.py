import requests
from bs4 import BeautifulSoup

num=1

cursor = ''
for i in range(10):
    req = requests.get("https://api.soomgo.com/v1/search/pro?sort=review_count&keyword=&cursor=" + cursor)
    data = req.json()
    for j in range(len(data['response']['results'])):
        print(num)
        print(data['response']['results'][j]['user']['name'])
        print(data['response']['results'][j]['companyName'])
        print(data['response']['results'][j]['score']['review_rate'])
        print(data['response']['results'][j]['score']['review_count'])
        print(data['response']['results'][j]['score']['hired_count'])
        print(data['response']['results'][j]['recentReview']['user']['name'])
        print(data['response']['results'][j]['recentReview']['contents'])
        print("=" * 50)
        num += 1

    cursor = data['response']['cursor']
