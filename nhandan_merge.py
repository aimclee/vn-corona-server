from virus.models import Nhandan_Title  # 승태 추가

import requests
from bs4 import BeautifulSoup
import os  # 승태추가
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "corona.settings")  # 승태추가
# # 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django  # 승태 추가
django.setup()  # 승태추가


# news title


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
    return answer


# 리스트에 중복이 되는 값을 없애기 위해서 집합 자료형으로 바꾸고 진행

# 뉴스 요약 내용 리스트


def contentArray():
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
    return result[:14]


def news_image():
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
    url = 'https://nhandan.com.vn'
    image = soup.select('.media-body a img[src]')
    answer = []
    for i in image:
        # 'https://nhandan.com.vn/' + img의 src
        full = url + i.get('src')
        answer.append(full)
    return answer


