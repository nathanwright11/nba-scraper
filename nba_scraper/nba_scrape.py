import requests
import beautifulsoup4


#dictionary of teams and their nba.com team_id
team_id = {
    "warriors_id": 1610612744
}

stats_url = "https://www.nba.com/stats/players/advanced?"

print(stats_url + team_id["warriors_id"])


r = requests.get(stats_url + team_id["warriors_id"])
soup = beautifulsoup4(r, "html.parser")

players = soup.find_all("a", attrs={"class":"Anchor_anchor__cSc3P"})

for player in players:
    print(player.text)