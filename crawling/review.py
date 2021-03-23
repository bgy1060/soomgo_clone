from selenium import webdriver
import time

chromedriver = 'C:/Users/daily-funding/Desktop/chromedriver.exe'


driver = webdriver.Chrome(chromedriver)

driver.get('https://soomgo.com/search/pro')

for i in range(2):
    title = driver.find_elements_by_css_selector("div.list-item a")
    title[i].click()
    time.sleep(1)
    review = driver.find_elements_by_css_selector("ul.review-container div.profile-review-item")

    for r in review:
        author = driver.find_element_by_css_selector("span.author").text
        content = driver.find_element_by_css_selector("div.collapsed-text-line.content").text
        date = driver.find_element_by_css_selector("span.date").text
        print(author+"\n")
        print(content+"\n")
        print(date + "\n")
        print("="*30)

    driver.get('https://soomgo.com/search/pro')
