import requests
from bs4 import BeautifulSoup
resp = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(resp.content, "xml")
money = soup.find('CharCode', text='RUR').find_next_sibling('Value').string
nominal = soup.find('CharCode', text='EUR').find_next_sibling('Nominal').string
print(nominal)
print(money)