import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '66cf62dfc081008ed65dabd9649f6829', 'q':'Arlington,US'}

response = requests.get(baseUrl, params = parameters)
print(response.content)
