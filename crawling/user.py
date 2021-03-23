from selenium import webdriver
import time

chromedriver = 'C:/Users/daily-funding/Desktop/chromedriver.exe'

driver = webdriver.Chrome(chromedriver)

driver.get('https://soomgo.com/search/pro')

for i in range(1):
    user = driver.find_elements_by_css_selector("div.list-item a")
    title = driver.find_elements_by_css_selector("h5.profile-name")
    intro = driver.find_elements_by_css_selector("p.profile-company-name")
    hire_count = driver.find_elements_by_css_selector("span.hired-count")

    print(title[i].text + "\n")
    print(intro[i].text + "\n")
    print(hire_count[i].text + "\n")

    user[i].click()
    time.sleep(1)