import requests
from bs4 import BeautifulSoup


def vn_express ():

    URL = 'https://timkiem.vnexpress.net/'
    params = {
        'q':'covid'
    }

    res = requests.get(URL, params=params)
    data = res.text
    soup = BeautifulSoup(data, 'html.parser')

    # 뉴스 제목 10개

    title = soup.select('.title_news a')

    title_array = []
    for t in title:
        a = t.get('title')
        title_array.append(a)
    print(len(title_array))
    # 뉴스 제목에 대한 내용 10개 크롤링

    contents = soup.select('.description')

    contents_array = []
    for content in contents:
        b = content.get_text()
        c = b.strip('\r\n')
        d = c.strip()
        contents_array.append(d)
    print(len(contents_array))


    # 뉴스 이미지 크롤링

    image = soup.select('.thumb_art img')

    image_array = []
    for i in image:
        img = i.get('src')
        image_array.append(img)
    print(len(image_array))
    dic = {}
    for text in range(len(image_array)):
        dic[title_array[text]] = [contents_array[text], image_array[text]]
    return dic


a = vn_express()
print(a)
