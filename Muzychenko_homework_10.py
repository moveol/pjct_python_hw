import requests

# Функція для перевірки статус коду
def check_status_code(response):
    if response.status_code == 200:
        return True
    else:
        print(f'Error: {response.status_code}')
        return False

# 1. Create a program that will ask user to search a word.
# Search this word in Giphy (use their API). Return links to these GIFs as a result
user_search = input('Enter a word to search for: ').strip()
response_giphy = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key=\
JanjMRJfUYGj36YC2BlPRud5B4FCSUtb&q={user_search}&limit=25&offset=0&rating=g&lang=en')
if check_status_code(response_giphy):
    for gif in response_giphy.json()['data']:
        print(gif['url'])

# 2. Взяти API-weather, розпарсити і вивезти погоду від користувача
user_city = input('Enter city name: ').strip().capitalize()
response_open_weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_city}&\
appid=38c90b55812d1743119071db5332847f')
if check_status_code(response_open_weather):
    weather_data = response_open_weather.json()
    weather = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    print(f'Weather: {weather}, Temperature: {temperature} K, Feels like: {feels_like} K, Humidity: {humidity}%, Wind speed: {wind_speed} m/s')

# 3. Вивеcти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json
response_astronauts = requests.get('http://api.open-notify.org/astros.json')
if check_status_code(response_astronauts):
    number_of_astronauts = response_astronauts.json()['number']
    print(f"Number of astronauts: {number_of_astronauts}")
    for astronaut in response_astronauts.json()['people']:
        print(astronaut['name'])
