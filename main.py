import requests
from lxml import html
import time
import datetime


# https://sinoptik.ua/погода-name_city/year-month-day
# данные о температуре хранятся в классе temperature
# данные о времени температуры хранятся в классе gray time
# данные, о том как ощущается, хранятся в классе temperatureSens
# данные о давление, скорости и направление ветра хранятся в классе gray
# и вся эта красота хранится в классе tabsContent; или в clearfix
# данные о закате и восходе солнышка хранятся в классе infoDaylight


def func_temperature_today(city: str = "Москва", day='сегодня') -> dict or int:
    if len(city.split()) == 1:
        page = f'https://sinoptik.ua/погода-{city.lower()}'
    else:
        txt = '-'.join(city.lower().split())
        page = f'https://sinoptik.ua/погода-{txt}'

    if day == 'сегодня':
        page += f'/{datetime.date.today()}'
        xpath_varib = '//*[@id="bd1c"]/div[1]/div[2]/table/tbody/'
    elif day == 'завтра':
        varib = str(datetime.date.today()).split('-')
        varib[2] = str(int(varib[2]) + 1)
        varib = '-'.join(varib)
        page += f'/{varib}'
        xpath_varib = '//*[@id="bd2c"]/div[1]/div[2]/table/tbody/'

    req = requests.get(page)
    dict_hour = dict()
    string = req.text
    par = html.fromstring(string)
    count_time = 0
    count = 0

    try:
        for i in range(1, 9):
            ma_div_temp = par.xpath(xpath_varib + f'tr[3]/td[{i}]')[0].text_content().encode('utf-8')
            ma_div_weather = par.xpath(xpath_varib + f'tr[2]/td[{i}]/div/@title')[0]
            if count_time - time.localtime().tm_hour >= 0 and count == 0:
                dict_hour['Погода сейчас'] = [f'{ma_div_temp.decode()}', f'{ma_div_weather.lower()}']
                count += 1
            else:
                if count_time == 3:
                    var = 'часа'
                elif count_time == 21:
                    var = 'час'
                else:
                    var = 'часов'
                dict_hour[f'Погода в {count_time} {var}'] = [f'{ma_div_temp.decode()}',
                                                             f'{ma_div_weather.lower()}']
            count_time += 3
        return list(map(lambda x: x[0], dict_hour.values())), \
            list(map(lambda x: x[1], dict_hour.values())), \
            list(map(lambda x: x, dict_hour.keys()))
    except IndexError:
        return 0

# //*[@id="bd1c"]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div
# //*[@id="bd1c"]/div[1]/div[2]/table/tbody/tr[2]/td[1]/div



