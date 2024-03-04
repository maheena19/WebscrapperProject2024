from bs4 import BeautifulSoup
import requests

url = "https://www.msn.com/en-us/weather/forecast/in-League-City,TX"
page = requests.get(url)
# used html.parser because it's the best for post 3.2 versions
soup = BeautifulSoup(page.text, "html.parser")

league_city_daily = soup.find_all("li", class_="display:inline")

for weather in league_city_daily:
    info = {}
    info['Day'] = weather.find("p", class_="headerV3-DS-EntryPoint1-1")
    info['High'] = weather.find("topTemp-E1_1 temp")