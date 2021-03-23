from selenium import webdriver
import time

chromedriver = 'C:/Users/daily-funding/Desktop/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

driver.get('https://soomgo.com/search/pro')

for i in range(1):
    title = driver.find_elements_by_css_selector("div.list-item a")
    title[i].click()
    time.sleep(1)
    while True:
        try:
            print("시도함")
            more = driver.find_element_by_css_selector("div.all-review div.text")
            print("클릭함")
            more.click()
            print("send key")
            time.sleep(4)

        except:
            print("끝")
            break

    question = driver.find_elements_by_css_selector("div.profile-qna li")
    for q in question:
        question = q.find_element_by_css_selector("div.question").text
        answer = q.find_element_by_css_selector("div.answer").text
        print(question + "\n")
        print(answer + "\n")

        print("=" * 30)

    driver.get('https://soomgo.com/search/pro')
