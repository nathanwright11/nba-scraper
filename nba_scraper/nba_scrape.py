import requests
from bs4 import BeautifulSoup


#dictionary of teams and their nba.com team_id
team_id = {
    "warriors_id": 1610612744
}

stats_url = "https://www.nba.com/stats/players/advanced?"
#print(f"{stats_url}TeamID={team_id['warriors_id']}")

r = requests.get(f"{stats_url}TeamID={team_id['warriors_id']}")
#print(r.content)

soup = BeautifulSoup(r.content, "html.parser")

#players = soup.find_all("a", attrs={"class":"Anchor_anchor__cSc3P"})
#players = soup.find_all("div", attrs={"class":"Layout_mainContent__jXliI"})
players = soup.find_all("tr")

for player in players:
    print(player.text)