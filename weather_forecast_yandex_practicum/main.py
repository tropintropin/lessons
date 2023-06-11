import json
import requests


city = input("Введите город: ")

server = "https://api.openweathermap.org/data/2.5/weather"

# Here are the Yandex Practicum's OpenWeather API ID!
parameters = "&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"

url = f'{server}?q={city}{parameters}'

weather_data = requests.get(url).json()

weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])

temperature_feels = round(weather_data['main']['feels_like'])

print(f'Сейчас в городе {city} {temperature}°C')
print(f'Ощущается как {temperature_feels}°C')

