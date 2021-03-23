from selenium import webdriver
import time

chromedriver = 'C:/Users/daily-funding/Desktop/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

driver.get('https://soomgo.com/search/pro')

for i in range(1):
    title = driver.find_elements_by_css_selector("div.list-item a")
    title[i].click()
    time.sleep(1)

    service = driver.find_elements_by_css_selector("div.profile-service-list  li")
    for s in service:
        print(s.text+"\n")

    print("="*50)