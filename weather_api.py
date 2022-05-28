import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input('City: \n').title()
params = {
    'q': city,
    'appid': '5a051cb1903556e79631b033688903c8',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
template = 'Current temperature in {} is {}'
print(template.format(city, res.json()['main']['temp']))
