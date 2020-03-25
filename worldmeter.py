from bs4 import BeautifulSoup
import requests


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

a = coronaParsing()
print(a)