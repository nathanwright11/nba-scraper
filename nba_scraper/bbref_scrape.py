import requests
from bs4 import BeautifulSoup
import numpy as np
import csv

r = requests.get("https://www.basketball-reference.com/teams/GSW/2023.html")
soup = BeautifulSoup(r.content, "html.parser")
#Isolates to only the 'Totals' stats table
totals = soup.find(id="totals")

#Isolates the data headers (rank, name, age, stat_categories)
t_head = totals.find("thead")

#Collects all the stat categories (with HTML tags)
headers_html = t_head.find_all("th")

#Removes HTML tags and puts all categories into an array. One entry will be trash and 
#needs to be replaced with 'name' category
header = [header.text for header in headers_html]
#Removes rank category
header.remove("Rk")
#Replaces trash entry with 'Name' category
header[0] = 'Name'
#Converts list to array
header = np.array(header)

#Isolates the player stats
t_body = totals.find("tbody")

#isolates players and all their stats (rank, name, age, stat_categories)
players = t_body.find_all("td")

#Removes HTML tags and puts all categories into an array
player_stats = [player.text for player in players]
#Converys list to array
player_stats = np.array(player_stats)

#Splits up player_stats array into individual arrays of each player. Need to add a
#way to determine/verify number of players in the table
player_stats = np.split(player_stats, 15)

#Writing the stats to a csv file
with open('player_stats.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    #Adds header with format (rank, name, age, stat_categories)
    writer.writerow(header)
    #Adds each player's stats on their own row
    for player in player_stats:
        writer.writerow(player)

print("CSV file updated")