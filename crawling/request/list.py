import requests
from bs4 import BeautifulSoup

raw = requests.get("https://soomgo.com/search/pro")
html = BeautifulSoup(raw.text, "html.parser")

container = html.select("div.search-pro--item")
num = 1
for cont in container:
    title = cont.select_one("h5.profile-name ").text.strip()
    intro = cont.select_one("p.profile-company-name").text.strip()
    review_rating = cont.select_one("span.review-rate").text.strip()
    review_count = cont.select_one("span.review-count").text.strip()
    hired_count = cont.select_one("div.profile-badges").text.strip()
    recent_reviewer = cont.select_one("div.profile-review>strong").text.strip()
    recent_review = cont.select_one("blockquote").text.strip()

    print(num)
    print(title)
    print(intro)
    print(review_rating)
    print(review_count)
    print(hired_count)
    print(recent_reviewer)
    print(recent_review)
    print("=" * 50)
    num += 1

cursor = 'MjQzJjI2MTgzOQ%3D%3D'
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
