from bs4 import BeautifulSoup
import requests
import xlwt

wb = xlwt.Workbook()
sheet = wb.add_sheet('豆瓣电影Top250')
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')

def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html)
    list = soup.find(class_='grid_view').find_all('li')
    for item in list:
        item_name = item.find(class_='title').string
        print(item_name)
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if item.find(class_='inq'):
            item_intr = item.find(class_='inq').string
        else:
            item_intr = '空'
        sheet.write(int(item_index), 0, item_name)
        sheet.write(int(item_index), 1, item_img)
        sheet.write(int(item_index), 2, item_index)
        sheet.write(int(item_index), 3, item_score)
        sheet.write(int(item_index), 4, item_author.strip())
        sheet.write(int(item_index), 5, item_intr)
        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)
def request_douban(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


for i in range(0, 10):
    main(i)

wb.save('豆瓣最受欢迎的250部电影.xls')
