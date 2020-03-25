from django.shortcuts import render

# Create your views here.
import django
import requests
from bs4 import BeautifulSoup
from rest_framework import viewsets
from .models import Nhandan_Title, VnExpress, Moh_Tracker, WorldMeter
from .serializers import NhandanSerializer, VnExpressSerializer, Moh_TrackerSerializer, WorldMeterSerializer
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../corona.settings")

django.setup()


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


"""
Moh
"""
# def moh_number ():
#     url = "https://ncov.moh.gov.vn/" # 감염된 사례 수, 내용들 크롤링 해오기
#     response = requests.get(url, verify=False)
#     data = response.text
#     soup = BeautifulSoup(data, 'html.parser')

#     infected_num = soup.select_one('.font24').text
#     return infected_num
def moh_crawling():
    url = "https://ncov.moh.gov.vn/" # 감염된 사례 수, 내용들 크롤링 해오기
    response = requests.get(url, verify=False)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    infected_num = soup.select_one('.font24')

    infected_ex = soup.select('.col-md-9 p span strong')

    infected_ex_array = []
    for i in infected_ex:
        a = i.get_text(strip=True)
        infected_ex_array.append(a)
        if a == None:
            del infected_ex_array[-1]
        else:
            c = a.strip('*')
            d = c.strip('.')
            e = d.strip()
            del infected_ex_array[-1]
            infected_ex_array.append(e)
    infected_ex_array = [s for s in infected_ex_array if s]

    inf = infected_ex_array[2:]


    dic = {}
    key_name = []
    value_name = []
    for i in range(len(inf)):
        if "BN" in inf[i] and len(inf[i]) <7:
            key_name.append(inf[i])
        else:
            value_name.append(inf[i])

    del value_name[value_name.index("29 tuổi, ở Quận Bình Thạnh, TP. Hồ Chí Minh. Bệnh nhân từ Paris – Pháp về tới sân bay Tân Sơn Nhất ngày 18/3/2020 trên chuyến bay của hãng hàng không AirFrance số hiệu AF258")]
    key_answer = key_name[:51]
    value_answer = value_name[:-16]

    for text in range(len(key_answer)):
        dic[key_answer[text]] = value_answer[text]
    return dic


"""
베트남 총 감염자 수, 사망자 수, 회복자 수, 신규 감염자 수
"""


def coronaParsing():

    url = 'https://www.worldometers.info/coronavirus/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    url_corona = soup.find_all('div', {'class': 'maincounter-number'})

    ###
    title = []  # title[0], title[1], title[2] -> world confirmed case

    # world confirmed Case
    # for text in range(len(url_corona)):
    #     title.append(url_corona[text].find('span').text)

    # vietnam corona case
    viet = []
    chart = soup.find('table', attrs={'id': "main_table_countries_today"})
    chart_body = chart.find('tbody')
    rows = chart_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        viet.append([ele for ele in cols if ele])

    for vietnam in viet:
        if vietnam[0] == 'Vietnam':
            title.append(vietnam[vietnam.index('Vietnam') + 1])  # 전체 감염자 수
            if vietnam[vietnam.index('Vietnam') + 2] == ' ':
                title.append('0')
            else:
                title.append(vietnam[vietnam.index('Vietnam') + 2])   # 사망자 수
            title.append(vietnam[vietnam.index('Vietnam') + 3])  # 회복자 수
            title.append(vietnam[vietnam.index('Vietnam') + 4])  # 신규 감염자수


    return title





class NhandanViewSet(viewsets.ModelViewSet):
    blog_data_dict = news_title()
    for t, l in blog_data_dict.items():
        Nhandan_Title(news_title=t,page_link=l[1], summary=l[0], img=l[2]).save()

    queryset = Nhandan_Title.objects.all()
    serializer_class = NhandanSerializer

class VnExpressViewSet(viewsets.ModelViewSet):
    blog_data_dict = vn_express()
    for t, l in blog_data_dict.items():
        VnExpress(news_title=t,page_link=l[1], summary=l[0], img=l[2]).save()

    queryset = VnExpress.objects.all()
    serializer_class = VnExpressSerializer


class Moh_TrackerViewSet(viewsets.ModelViewSet):
    blog_data_dict = moh_crawling()
    for t,l in blog_data_dict.items():
        Moh_Tracker(location=t, tracker=l).save()

    queryset = Moh_Tracker.objects.all()
    serializer_class = Moh_TrackerSerializer


class WorldMeterViewSet(viewsets.ModelViewSet):
    blog_data_dict = coronaParsing()
    WorldMeter(total_infected = blog_data_dict[0], total_death= blog_data_dict[1], total_recovery= blog_data_dict[2], new_infected= blog_data_dict[3]).save()

    queryset = WorldMeter.objects.all()
    serializer_class = WorldMeterSerializer