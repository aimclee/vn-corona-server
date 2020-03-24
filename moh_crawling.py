import requests
from bs4 import BeautifulSoup
url = "https://ncov.moh.gov.vn/" # 감염된 사례 수, 내용들 크롤링 해오기
response = requests.get(url, verify=False)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
# url_corona = soup.find_all('div', {'class': 'journal-content-article'})
#현재 감염자 수
print("감염자 수: ")
infected_num = soup.select_one('.font24')
print(infected_num.get_text())
# 감염자 사례
print("감염자 사례: ")
infected_ex = soup.select('.col-md-9 p span strong')
# infected_ex = unicodedata.normalize("NFKD", temp)
# t = str(temp)
# infected_ex = t.strip()
# .col-md-9 p span strong strong -> 제거
# inf = soup.select('.col-md-9 p span strong strong')
# for infected in inf:
#     infected.decompose()
# print(soup)
infected_ex_array = []
for i in infected_ex:
    a = i.get_text(strip=True)
    print(a) # 리스트 형태로 바꾸기 이전
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
# print(infected_ex_array[2:]) # 리스트 형태로 바꾼 이후. 단, \xa0 이란 값이 계속 들어오는데 어떻게 제거해야할 지 모르겠다.
inf = infected_ex_array[2:]
# print(inf)
#받아온 리스트의 {홀수(key): 짝수(value)} 인덱스 값으로 나누고 딕셔너리로 변환
odd = inf[0::2]
even = inf[1::2]
# print(odd, even)
kv = [odd,even]
infected_ex_dict = dict(zip(*kv))
print(infected_ex_dict)
# 짝수번째를 키값, 홀수번째를 밸류값으로 지정한다.
# print(infected_ex_dict)
# for key, value