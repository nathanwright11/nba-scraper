import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.basketball-reference.com/teams/GSW/2023.html#totals")
soup = BeautifulSoup(r.content, "html.parser")

#isolates the player stat totals
totals = soup.find(id="div_totals")

#isolates playrs and all their stats
players = totals.find_all("td")

for player in players:
    print(player.text)

#print(players[1].text)



# print(totals.text)
# print(totals.text.split())