from bs4 import BeautifulSoup
from decimal import *
import requests
from bs4 import BeautifulSoup

def convert(amount, cur_from, cur_to, date, requests):
    params = {
        'date_req': date
    }
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?', params)

    soup = BeautifulSoup(response.content, "xml")

    money = Decimal(amount)
    if(cur_from!="RUR"):
        nominal = Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string)
        money = (soup.find('CharCode', text=cur_from).find_next_sibling('Value').string)
        money = money.replace(',', '.', 1)
        money = Decimal(money)
        money = money/nominal
        money = money*amount

    money1 = 1
    if(cur_to!='RUR'):
        nominal1 = Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string)
        money1 = (soup.find('CharCode', text=cur_to).find_next_sibling('Value').string)
        money1 = money1.replace(',', '.', 1)
        money1 = Decimal(money1)
        money1 = money1 / nominal1

    response = money/money1
    response = round(response,4)
    return response  # не забыть про округление до 4х знаков после запятой

