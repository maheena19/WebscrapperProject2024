from bs4 import BeautifulSoup

with open('', 'r') as weather_file:
    content = weather_file.read()
    print(content)