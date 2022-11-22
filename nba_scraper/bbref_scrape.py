import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.basketball-reference.com/teams/GSW/2023.html")
soup = BeautifulSoup(r.content, "html.parser")
#Isolates to only the 'Totals' stats table
totals = soup.find(id="totals")

#Isolates the data headers (rank, name, age, stat_categories)
# t_head = totals.find("thead")

# #Collects all the stat categories (with HTML tags)
# headers = t_head.find_all("th")

# #Removes HTML tags and puts all categories into an array. One entry will be trash and 
# #needs to be replaced with 'name' category
# stat_ctgs = [header.text for header in headers]


#Isolates the player stats
t_body = totals.find("tbody")

#isolates players and all their stats (rank, name, age, stat_categories)
players = t_body.find_all("td")

#Removes HTML tags and puts all categories into an array
player_stats = [player.text for player in players]
print(player_stats)