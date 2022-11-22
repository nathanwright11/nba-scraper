import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.basketball-reference.com/teams/GSW/2023.html#totals")
soup = BeautifulSoup(r.content, "html.parser")