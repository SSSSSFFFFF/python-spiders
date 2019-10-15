import requests
from bs4 import BeautifulSoup
import os
def request_page(url):
    try:
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        response = session.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def download(url):
    html = request_page(url)
    soup = BeautifulSoup(html)
    total = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string
    title = soup.find('h2').string
    image_list = []
    for i in range(int(total)):
        html = request_page(url + '/%s' % (i + 1))
        print(html)
        soup = BeautifulSoup(html)
        img_url = soup.find('img').get('src')
        # print(img_url)
        image_list.append(img_url)
    # print("image_list",image_list)
    download_Pic(title, image_list)
    # download_Pic(title, image_list)
def get_page_urls():
    for i in range(1,2):
        baseurl = 'https://www.mzitu.com/page/{}'.format(i)
        html = request_page(baseurl)
        soup = BeautifulSoup(html)
        list = soup.find(class_='postlist').find_all('li')
        urls = []
        for item in list:
            url = item.find('span').find('a').get('href')
            urls.append(url)
            download(url)
    # print(urls)
    # return urls


def download_Pic(title, image_list):

    # 新建文件夹
    # os.mkdir(title)
    j = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
    # 下载图片
    for item in image_list:
        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        img = session.get(item, headers=headers)
        print("img",item,img)
        filename = '%s/%s.jpg' % (title, str(j))
        print('downloading....%s : NO.%s' % (title, str(j)))
        with open(filename, 'wb') as f:
            img = requests.get(item, headers=headers).content
            print(img)
            f.write(img)
        j += 1


get_page_urls()




