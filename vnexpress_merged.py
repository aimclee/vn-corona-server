import requests
from bs4 import BeautifulSoup

# 페이지의 주소 가져오기(첫 페이지의 10개 뉴스만 가져올 것.)

URL = 'https://timkiem.vnexpress.net/'
params = {
    'q':'covid'
}

res = requests.get(URL, params=params)
data = res.text
soup = BeautifulSoup(data, 'html.parser')

# 뉴스 제목 10개

print('뉴스제목 10개: ')
print('\n')

title = soup.select('.title_news a')

title_array = []
for t in title:
    a = t.get('title')
    title_array.append(a)
print(title_array)

# 뉴스 제목에 대한 내용 10개 크롤링

print('\n')
print('뉴스내용 10개: ')
print('\n')

contents = soup.select('.description')

contents_array = []
for content in contents:
    b = content.get_text()
    c = b.strip('\r\n')
    d = c.strip()
    contents_array.append(d)
print(contents_array)


# 뉴스 이미지 크롤링

print('\n')
print('뉴스 이미지 10개: ')
print('\n')

image = soup.select('.thumb_art img')

image_array = []
for i in image:
    img = i.get('src')
    image_array.append(img)
print(image_array)
