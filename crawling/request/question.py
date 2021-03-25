import requests
from bs4 import BeautifulSoup
import openpyxl

cursor = ""
req = requests.get("https://api.soomgo.com/v1/search/pro?sort=review_count&keyword=&cursor="+cursor)
data = req.json()

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(['id','question','answer','uid_id'])

user_list = data['response']['results']

num=1

for i in range(len(user_list)):
    uid = user_list[i]['user']['id']
    user_info = requests.get("https://api.soomgo.com/v2/user/"+str(uid)+"/profile?role=provider&is_read_counting=true")
    info_data = user_info.json()
    qna = info_data['response']['qna']
    for j in range(len(qna)):
        question = qna[j]['question'].replace("'","").strip()
        answer = qna[j]['answer'].replace("'","").strip()
        print(question)
        print(answer)
        print("="*50)
        sheet.append([num, str(question),str(answer), i + 1])
        num+=1

wb.save("qna.xlsx")