from selenium import webdriver
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup as bs
import json
import time

url = input("Enter the URL: ")
domain = url.split("/")[2]
protocol = url.split("/")[0] + "//"
reviews = []

driver = webdriver.Chrome()  # or Firefox or Edge

while True:
    print(f"Processing: {url}")
    driver.get(url)
    time.sleep(3)  

    divs = driver.find_elements(By.CSS_SELECTOR, "p.uopin")
    # source = driver.page_source
    # soup = bs(source, "html.parser")

    for div in divs:
        text = div.text
        reviews.append(text)

    nav_page = driver.find_element(By.CSS_SELECTOR, "div.nav-pages")
    all_a_tags = nav_page.find_elements(By.TAG_NAME, "a")
    if all_a_tags[-1].get_attribute("title") == "Next page":
        url = all_a_tags[-1].get_attribute("href")
    else:
        print("No more pages, save reviews to json file")
        with open('reviews.json', 'w') as file:
            json.dump(reviews, file)
        break

driver.quit()