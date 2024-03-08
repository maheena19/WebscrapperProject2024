#The library used to break down HTML information into easily traversable objects
from bs4 import BeautifulSoup
#The library used to be able to access internet URLs
import urllib.request

#Url used
url = "https://www.msn.com/en-us/weather/forecast/in-League-City,TX?"
page = urllib.request.Request(
    url,
    data = None,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
)

# used html.parser because it's the best for post 3.2 versions
f = urllib.request.urlopen(page)
soup = BeautifulSoup(f, "html.parser")

#Finds days, as well as the highs and lows from the coming 10 days in league city and extracts data from them
league_city_daily = soup.find_all("li", style_="display: inline-block")
print(league_city_daily)
for weather in league_city_daily:
    info = {'Day': weather.find("p", class_="headerV3-DS-EntryPoint1-1"),
            'High': weather.find("div", class_="topTemp-DS-EntryPoint1-1 temp-D5-EntryPoint1-1"),
            'Low': weather.find("div", class_="temp-DS-EntryPoint1-1")}
    print(info['High'])
