import requests
import json
import urllib.parse
city = input('which city\'s weather do you want to know?')
city = urllib.parse.quote(city)
initial_url = r'http://wthrcdn.etouch.cn/weather_mini?city=%s' % city
result = requests.get(initial_url)

if result.status_code == requests.codes.ok :
    result = result.json()
    result_data = result.get('data')
    print(result_data)
    print(result_data.get('city'))
    print('当前温度:', result_data.get('wendu'),'℃')
    print(result_data.get('ganmao'))
elif result.status_code == 403 :
    first_header = {
        'User-Agent':'Chrome'
    }
    result = requests.get(initial_url, headers = first_header)
    result = result.json()
    result_data = result.get('data')
    print(result_data)
    print(result_data.get('city'))
    print('当前温度:', result_data.get('wendu'),'℃')
    print(result_data.get('ganmao'))
