from selenium import webdriver
import time

chromedriver = 'C:/Users/daily-funding/Desktop/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

driver.get('https://soomgo.com/search/pro')

for i in range(20):
    title = driver.find_elements_by_css_selector("div.list-item a")
    title[i].click()
    time.sleep(1)
    print("============기본정보===============")
    basic_info = driver.find_elements_by_css_selector("div.profile-basic-info ul li ")
    for b in basic_info:
        print(b.text+"\n")

    print("============추가정보===============")
    added_info = driver.find_elements_by_css_selector("div.profile-added-info ul li ")
    for a in added_info:
        print(a.text+"\n")

    print("="*50)
    driver.get('https://soomgo.com/search/pro')