from bs4 import BeautifulSoup
import urllib.requests

url = "https://www.msn.com/en-us/weather/forecast/in-League-City,TX?"
page = requests.get(url)
# used html.parser because it's the best for post 3.2 versions
soup = BeautifulSoup(page.text, "html.parser")

league_city_daily = soup.find_all("li", style_="display: inline-block")

for weather in league_city_daily:
    info = {'Day': weather.find("p", class_="headerV3-DS-EntryPoint1-1"),
            'High': weather.find("div", class_="topTemp-DS-EntryPoint1-1 temp-D5-EntryPoint1-1"),
            'Low': weather.find("div", class_="temp-DS-EntryPoint1-1")}
    print(info['High'])
