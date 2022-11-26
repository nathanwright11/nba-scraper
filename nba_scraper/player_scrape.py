import requests
from bs4 import BeautifulSoup
#import numpy as np
import csv


###Collecting Game log of Players###

#URL for Steph Curry game logs
curry_url = "https://www.basketball-reference.com/players/c/curryst01/gamelog/2022"

r = requests.get(curry_url)
soup = BeautifulSoup(r.content, "html.parser")

#Isolates regular season stats
reg_stat = soup.find("table", id="pgl_basic")

#Isolates stat categories
thead = reg_stat.find("thead")
#Grabs stats categories
stat_html = thead.find_all("th")

stat_ctgs = []
for stat in stat_html:
    stat_ctgs.append(stat.text)

#Isolates game stats
tbody = reg_stat.find("tbody")
games = tbody.find_all("tr")

#An array of arrays. Each game will be an array of their own stats, combined into
#the game_logs array
game_log = []

#Loops through each game and pulls all the stats or INACTIVE status
for game in games:
    #Created inside loop so it is empty before the start of every game
    stats = []
    #Pulls all possible stats from game (accounts for INACTIVE status)
    game_stats = game.find_all("td")

    #Puts each stat into array as their own item
    for stat in game_stats:
        stats.append(stat.text)
    
    #Adds the stats array to the game_log array so each game is their own array
    game_log.append(stats)


#Writing the stats to a csv file
with open('curry_games.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    #Adds header with format (rank, name, age, stat_categories)
    writer.writerow(stat_ctgs)
    #Adds each player's stats on their own row
    for game in game_log:
        writer.writerow(game)

print("CSV file updated")