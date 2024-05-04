import requests
from bs4 import BeautifulSoup
import json

url = input("Enter the URL: ")
domain = url.split("/")[2]
protocol = url.split("/")[0] + "//"
reviews = []

while True:
    print(f"Processing: {url}")
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        divs = soup.find_all("p", class_="uopin")

        for div in divs:
            text = div.text
            reviews.append(text)
    else:
        print("Error: ", response.status_code)
        break
    
    nav_page = soup.find("div", class_="nav-pages")
    all_a_tags = nav_page.find_all("a")
    if all_a_tags[-1].get("title") == "Next page":
        url = protocol + domain + '/' + all_a_tags[-1].get("href")
    else: 
        print("No more pages, save reviews to json file")
        with open('reviews.json', 'w') as file:
            json.dump(reviews, file)
        break
