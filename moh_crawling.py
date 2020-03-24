import requests
from bs4 import BeautifulSoup


def moh_number ():
    url = "https://ncov.moh.gov.vn/" # 감염된 사례 수, 내용들 크롤링 해오기
    response = requests.get(url, verify=False)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    infected_num = soup.select_one('.font24').text
    return infected_num
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

