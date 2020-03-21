import requests
from bs4 import BeautifulSoup

url = "https://ncov.moh.gov.vn/ban-do-vn"
response = requests.get(url, verify=False)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

url_corona = soup.find_all('div', attrs={'class': 'mat-list-item-ripple'})

print(url_corona)
