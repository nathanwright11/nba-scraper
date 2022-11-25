import requests
from bs4 import BeautifulSoup


#dictionary of teams and their nba.com team_id
team_id = {
    "warriors_id": 1610612744
}

stats_url = "https://www.nba.com/stats/players/advanced?"
#print(f"{stats_url}TeamID={team_id['warriors_id']}")

#Automates going through each team's stats pages
r = requests.get(f"{stats_url}TeamID={team_id['warriors_id']}")
#print(r.content)

soup = BeautifulSoup(r.content, "html.parser")

main_content = soup.find(class_="Layout_mainContent__jXliI")
node = main_content.find(class_="Block_blockContent__6iJ_n")
tbody = node.find("tbody")
print(tbody)
#players_html = tbody.find_all("tr")
#print(players_html[0])