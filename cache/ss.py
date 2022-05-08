import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.douyu.com/52876")
demo = r.text
print(demo)
print("\n\n\n")
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())