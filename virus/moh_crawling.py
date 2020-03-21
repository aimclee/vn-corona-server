import requests
from bs4 import BeautifulSoup

# def moh_crawling():
url = "https://ncov.moh.gov.vn/"
response = requests.get(url, verify=False)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
url_corona = soup.find_all('div', {'class': 'journal-content-article'})

result = []

print(url_corona)
