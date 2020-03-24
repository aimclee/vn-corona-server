import requests
from bs4 import BeautifulSoup

def news_title():
    URL = 'https://nhandan.com.vn/tim-kiem'

    # 페이지의 주소 가져오기(1페이지의 14개 뉴스만 가져올 것.)
    i = 1
    params = {
        'searchword': 'covid',
        'p': i,
    }

    res = requests.get(URL, params=params)
    data = res.text
    soup = BeautifulSoup(data, 'html.parser')

    title = soup.select('.mt-0 a')
    answer = []
    for j in title:
        answer.append(j.string)

    content = soup.select('.media-body p')

    # 빈 리스트 생성 후 각각의 뉴스에 대한 내용들 담기
    content_array = []
    for con in content:
        texts = con.get_text()  # texts는 string형
        content_array.append(texts)

    temp = set()
    result = []
    for item in content_array:
        if item not in temp:
            temp.add(item)
            result.append(item)
    result = result[:14]

    # 이미지 링크 업로드
    URL_image = 'https://nhandan.com.vn/tim-kiem'
    res_img = requests.get(URL_image, params=params)
    data_img = res_img.text
    soup_img = BeautifulSoup(data_img, 'html.parser')
    url_img = 'https://nhandan.com.vn'
    image = soup_img.select('.media-body a img[src]')
    img = []
    for i in image:
        # 'https://nhandan.com.vn/' + img의 src
        full = url_img + i.get('src')
        img.append(full)

    # link
    links = soup.select('.mt-0 a[href]')
	
    link_array = []
    for link in links:
        l = link.get('href')
        i = 'https://nhandan.com.vn' + l
        link_array.append(i)
    print(link_array)
    # 최종
    dic = {}
    for text in range(len(answer)):
        dic[answer[text]] = [result[text],link_array[text], img[text]]

    return dic


"""
VN Express Crawling
"""

def vn_express():

    URL = 'https://timkiem.vnexpress.net/'
    params = {
        'q':'covid',
        'latest': 'on'
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

    # 뉴스 제목에 대한 내용 10개 크롤링

    contents = soup.select('.description')

    contents_array = []
    for content in contents:
        b = content.get_text()
        c = b.strip('\r\n')
        d = c.strip()
        contents_array.append(d)


    # 뉴스 이미지 크롤링
    image = soup.select('.thumb_art img')

    image_array = []
    for i in image:
        img = i.get('src')
        image_array.append(img)

    
    links = soup.select('.title_news a')

    link_array =[]
    for link in links:
        l = link.get('href')
        link_array.append(l)

    dic = {}
    for text in range(len(image_array)):
        dic[title_array[text]] = [contents_array[text],link_array[text], image_array[text]]
    return dic

a = news_title()

print(a)