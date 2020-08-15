from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from utils import save_image, name_image
from class_post import Posts, Post

# Instanciate Variable and Posts object
url = "https://null-byte.wonderhowto.com/how-to/linux-basics/"
posts = Posts()

# Selenium Drivers
driver = webdriver.Chrome()
driver.get(url)
first_response = requests.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

try:
    # Get all articles as a list
    articles = soup.find_all('article', class_='article-item')
except Exception as e:
    articles = None

for article in articles:
    try:
        # Browse article on the main page to retrieve article information
        title = article.find('h3', class_="article-headline").text.strip().split(':')[1:]
        title = ' '.join(title).strip()
        summary = article.find('div', class_='details').p.text.strip()
        link = article.find('h3', class_="article-headline").a['href']
        image = article.find('img', class_="lazy-img")['data-src']
        #! TEST
        picture_fn = name_image(image)

        # Browse article through link to retrieve article information
        driver.get(link)
        first_response = requests.get(link)
        sub_soup = BeautifulSoup(driver.page_source, 'lxml')
        article_content = sub_soup.find('article', class_='article-container').text

        # Create Post Object
        post = Post(link, title, summary, image, picture_fn, article_content)

        # Append Post Object to Posts Object
        posts.add_post(post)

    except Exception as e:
        pass

# Save_json method from Posts Class
posts.save_json('null_byte_export.json')
