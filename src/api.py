import random
import string
import time
import requests
from bs4 import BeautifulSoup


headers = {
    'authority': 'prnt.sc',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

#driver = webdriver.Firefox()
def get_url():
    url = "https://prnt.sc/"+ random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + str(random.randint(1000,9999))
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    img_tag = soup.find('img', {'id': 'screenshot-image'})
    if req.status_code != 200:
        print("Unable to fetch data")

    if img_tag:
        tmp =  requests.get(img_tag.get("src"), headers=headers)
        if tmp.status_code == 200:
            return url
    else:
        print("Link invalid")
    time.sleep(2)
