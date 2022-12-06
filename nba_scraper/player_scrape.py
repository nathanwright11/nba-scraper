import requests
from bs4 import BeautifulSoup
import csv


######-------------------Game Log Collection Steps------------------######
#
#    1. Create url of season to grab game logs
#
#    2. Grab html of that seasons' game log
#    
#    3. Isolate regular season game stats
#
#    4. Grab stats for all 82 games (stats/INACTIVE)
#
#    5. Write stats to csv
#
######--------------------------------------------------------------######


#takes result from GET request, isolates regular season stats, puts all game 
#stats into array
def get_game_stats(url_request):
    
    #parsers html of url_request
    soup = BeautifulSoup(url_request.content, "html.parser")

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
    game_logs = []

    #Loops through each game and pulls all stats/INACTIVE status
    for game in games:
        stats = []
        #Pulls all possible stats from game (accounts for INACTIVE status)
        game_stats = game.find_all("td")

        #Puts each stat into array as their own item
        for stat in game_stats:
            stats.append(stat.text)
    
        #Adds the stats array to the game_log array so each game is their own array
        game_logs.append(stats)
    
    return stat_ctgs, game_logs


#function to write stats from a given season to csv file
def write_csv(header, game_logs, year):
    
    with open(f'curry_games_{year}.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        #Adds header with format (rank, name, age, stat_categories)
        writer.writerow(header)
        #Adds each player's stats on their own row
        for game in game_logs:
            writer.writerow(game)

    return print(f"curry_games_{year}.csv updated")




######----------Main Section-----------------#####


#starting year to grab games
year = 2023

#URL for Steph Curry game logs
curry_url = "https://www.basketball-reference.com/players/c/curryst01/gamelog/"

#Number of previous years to grab
prev_yrs = 5

#Loop to grab games from multiple seasons
for i in range(prev_yrs):

    #GET request to grab website data
    r = requests.get(curry_url + str(year))

    #Grabs stat categories and game stats
    header, game_logs = get_game_stats(r)

    #Writes game stats to csv
    write_csv(header, game_logs, year)

    #decrements year for url
    year -= 1