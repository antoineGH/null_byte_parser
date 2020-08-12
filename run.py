from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json
from utils import save_image, post_posts, save_json, posts

url = "https://null-byte.wonderhowto.com/how-to/linux-basics/"

driver = webdriver.Chrome()
driver.get(url)
first_response = requests.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

try:
    articles = soup.find_all('article', class_='article-item')
except Exception as e:
    articles = None

for article in articles:
    try:
        title = article.find('h3', class_="article-headline").text.strip().split(':')[1:]
        title = ' '.join(title).strip()
        print(title)
    except Exception as e:
        title = None

    try:
        summary = article.find('div', class_='details').p.text.strip()
    except Exception as e:
        summary = None

    try:
        link = article.find('h3', class_="article-headline").a['href']
    except Exception as e:
        link = None

    try:
        image = article.find('img', class_="lazy-img")['data-src']
    except Exception as e:
        image = None

    try:
        picture_fn = save_image(image, 'null_byte')
    except Exception as e:
        pass

    try:
        post_posts(title, summary, link, image, picture_fn)
    except Exception as e:
        pass

save_json(posts)

with open("posts.json", "r") as read_file:
    data = json.load(read_file)
    for obj in data:
        print(obj)
        print('\n')