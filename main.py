import requests
from lxml import html
import time


# https://sinoptik.ua/погода-name_city/year-month-day
# данные о температуре хранятся в классе temperature
# данные о времени температуры хранятся в классе gray time
# данные, о том как ощущается, хранятся в классе temperatureSens
# данные о давление, скорости и направление ветра хранятся в классе gray
# и вся эта красота хранится в классе tabsContent; или в clearfix
# данные о закате и восходе солнышка хранятся в классе infoDaylight


def func_temperature_today(city: str = "Москва") -> dict:
    if city == "" or " " == city:
        city = "Москва"
    if len(city.split()) == 1:
        page = f'https://sinoptik.ua/погода-{city.lower()}'
    else:
        txt = '-'.join(city.lower().split())
        page = f'https://sinoptik.ua/погода-{txt}'
    req = requests.get(page)
    dict_hour = dict()
    string = req.text
    par = html.fromstring(string)
    count_time = 0
    count = 0
    # xpath_month = par.xpath('//*[@id="bd1"]/p[3]/text()')[0]
    # xpath_day = par.xpath('//*[@id="bd1"]/p[2]/text()')[0]
    # print(f'{xpath_day} {xpath_month}')
    for i in range(1, 9):
        ma_div_temp = par.xpath(f'//*[@id="bd1c"]/div[1]/div[2]/table/tbody/tr[3]/td[{i}]')[0].text_content().encode(
            'utf-8')
        ma_div_weather = par.xpath(f'//*[@id="bd1c"]/div[1]/div[2]/table/tbody/tr[2]/td[{i}]/div/@title')[0]
        if count_time - time.localtime().tm_hour >= 0 and count == 0:
            dict_hour['now'] = [f'{ma_div_temp.decode()}', f'{ma_div_weather.lower()}']
            count += 1
        else:
            # для смены дня нужно менять циферку в bd1c
            dict_hour[count_time] = [f'{ma_div_temp.decode()}',
                                     f'{ma_div_weather.lower()}']
        count_time += 3
    return dict_hour
    # for i in range(1, 9):
    #     ma_div = par.xpath(f'//*[@id="bd1c"]/div[1]/div[2]/table/tbody/tr[2]/td[{i}]/div/@title')[0]
    #     print(f'В {count_time}:00 было {ma_div.lower()}')
    #     count_time += 3


# //*[@id="bd1c"]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div
# //*[@id="bd1c"]/div[1]/div[2]/table/tbody/tr[2]/td[1]/div
def func_return_values(dict_values_func: dict) -> tuple:
    return list(map(lambda x: x[0], dict_values_func.values())), \
        list(map(lambda x: x[1], dict_values_func.values()))

