from bs4 import BeautifulSoup
import requests

url = "https://www.msn.com/en-us/weather/forecast/in-League-City,TX"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
job = soup.find()
daily_weather = job.find()

print(daily_weather)



