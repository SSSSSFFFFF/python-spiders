import requests
from bs4 import BeautifulSoup
def get_page_urls():
    for i in range(1,212):
        # baseurl = 'https://www.mzitu.com/page/{}'.format(i)
        baseurl = 'https://www.mzitu.com/page/1'
        html = request_page(baseurl)
        soup = BeautifulSoup(html)
        list = soup.find(class_='postlist').find_all('li')
        urls = []
        for item in list:
            url = item.find('span').find('a').get('href')
            urls.append(url)
    print(urls)
    return urls
def request_page(url):
    try:
        response = requests.get(url)
        print(response.text)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None
get_page_urls()