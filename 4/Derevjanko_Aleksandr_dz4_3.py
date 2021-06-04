from requests import get, utils
from datetime import datetime
response_1 = get('http://www.cbr.ru/scripts/XML_daily.asp')
encoding_1 = utils.get_encoding_from_headers(response_1.headers)
string_1 = (response_1.content.decode(encoding=encoding_1))
list_1 = string_1.split('ID=')
response_1.close()


def currency_rates(char):
    """  Введите код валюты  """
    index_1 = string_1.find('ValCurs Date=')
    day_1 = int(string_1[(index_1 + 14):(index_1 + 16)])
    month_1 = int(string_1[(index_1 + 17):(index_1 + 19)])
    year_1 = int(string_1[(index_1 + 20):(index_1 + 24)])
    date_1 = datetime(year=year_1, month=month_1, day=day_1)
    char = char.upper()
    for item in list_1:
        if item.find(char) != -1:
            start_1 = item.find('<Nominal>')
            end_1 = item.find('</Nominal>')
            start_2 = item.find('<Value>')
            end_2 = item.find('</Value>')
            nominal = float(item[(start_1 + 9):end_1])
            value = float(item[(start_2 + 7):end_2].replace(',', '.'))
            return '{} на {}'.format((value / nominal), date_1.date())


print(currency_rates('usd'))
print(currency_rates('EUR'))
