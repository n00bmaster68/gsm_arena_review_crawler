# gsm_arena_review_crawler

## Overview
This project compares three different approaches to crawl websites: 

1. **Requests & BeautifulSoup (bs4):** This approach uses the `requests` library to send HTTP requests and the `BeautifulSoup` library to parse the HTML response. It provides a simple and lightweight solution for web scraping.

2. **Selenium:** This approach utilizes the `Selenium` library, which allows you to automate web browsers. It is useful when websites heavily rely on JavaScript or require user interactions.

3. **Scrapy:** This approach leverages the `Scrapy` framework, which provides a powerful and flexible way to scrape websites. It offers built-in features like automatic request handling, item pipelines, and spider middleware.

In addition to the above approaches, this project also includes a GUI application built with Scrapy. The GUI app provides a user-friendly interface to interact with the web crawler and view the scraped data.

Please, note that this project only work with GSM Arena website!

## Installation

To use this project, you need to have Python installed. 
You can install the required dependencies by running the following command:
`pip install -r requirements.txt`

## Usage
### Requests & BeautifulSoup (bs4) approach, run following commands accordingly:
1. `cd .\gsm_arena\demo_with_request`
2. `python crawl_data_with_request.py`
=> The output will save as json file after the process is done

### Selenium approach, run following commands accordingly:
1. `cd .\gsm_arena\demo_with_selenium`
2. `python crawl_data_with_selenium.py`
- => The output will save as json file after the process is done

### Scapy approach:

#### With commands:
1. `cd .\gsm_arena\gsm_arena_product_review\gsm_arena_product_review`
2. `scrapy crawl gsm_arena_product_review -o {your output file} -a start_url={your URL}`

#### With GUI:
- `cd C:\Users\84901\Desktop\phanmemmnm\gsm_arena\gui_app`
- `python app.py`
- Then a windows like this will pop up:
![[Starting UI]](app_screenshots/app_starter.png)
##### This app provides user 2 ways to crawl data:
- Crawl with one single URL
![[Single URL UI]](app_screenshots/single_url.png)
- Crawl with a file containing URLs
![[URL list UI]](app_screenshots/url_list.png)

## 🖥️ Author
Thang Le-Huy Nguyen

## Report for this project
<a href="https://www.overleaf.com/8268586649mbxymvmbdhfv#fb3d48">LaTex report</a>