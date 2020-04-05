from bs4 import BeautifulSoup
from selenium import webdriver
import re
import json
import requests

url = 'https://api.bukalapak.com/product-reviews?access_token=kxOwG6j_AHxiI4Wplxaykd1ypTQzePBhdHOtnuNiwk5PkA&ratings%5B%5D=3&product_id=2fvpubr&offset=0&limit=10'
# driver = webdriver.Chrome()
# driver.get(url)
# # content = driver.page_source
# driver.quit()

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
headers = {"User-Agent" : UA}
dat = requests.get(url, headers=headers).content.decode("utf-8")
# soup = BeautifulSoup(content, 'html.parser')
# title = soup.find('h1', attrs={'class' : 'css-x7lc0h'})
# rating = soup.findAll('div', attrs={'class' : 'css-lmh7qr e1j9voh13'})
# review_container = soup.find('p', class_='css-1np3d84-unf-heading e1qvo2ff8')
# for ptag in review_container.findAll('span') :
#     print(ptag.text)

# rev = review_container.find('span')
# print(rev)
# review = test.find_all('span')
# review = soup.find_all(re.compile('span|p', {'class' : re.compile('css-1np3d84-unf-heading e1qvo2ff8')}))
# review = soup.findAll('p', attrs={'class' : 'u-mrgn-top--1 u-mrgn-bottom--0 u-txt--break-word u-fg--black qa-product-review-content'})
# for i in range(len(review)) :
#     print(review[i].text.strip())

# print(len(review))
# print(review)
dt = json.loads(dat)
json_formatted_str = json.dumps(dt, indent=2)
print(json_formatted_str)
# print(dt["data"][0]["id"])