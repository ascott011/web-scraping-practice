import requests
from bs4 import BeautifulSoup
import pandas as pd


# check the status code to start as a habit

# header to say I am a browser and not some generic script
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = 'https://www.nfl.com/stats/team-stats/'

def get_stats(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        print(response.status_code)
        exit()
    soup = BeautifulSoup(response.content, 'html.parser')

    column_headers = soup.find("thead").text.splitlines()[2:-1]
    table_body = soup.find("tbody")
    rows = table_body.find_all("tr")
    #this was checking the frist team's data to make sure it grabs everything in the correct format
    # cells = rows[1].find_all("td")

    all_team_stats = []
    
    for row in rows:
        cells = row.find_all("td")
        #if there was a blank for or seperator row, this would skip it
        if not cells:
            continue

        #special case because table has formal team name and shortened name. Only want shortened name
        team_data = []
        team_cell = cells[0]
        short_team_name = team_cell.find("div", class_="d3-o-club-fullname")
        team_data.append(short_team_name.get_text(strip=True))

        #grab the rest of the stats
        for cell in cells[1:]:
            team_data.append(cell.get_text(strip=True))
        
        all_team_stats.append(team_data)
    
    return column_headers, all_team_stats

print(get_stats(url, headers))

column_headers, team_stats = get_stats(url, headers)

def create_pandas_df(data, headers):
    df = pd.DataFrame(data=data, columns=headers)

create_pandas_df(team_stats, column_headers)

print(create_pandas_df(team_stats, column_headers))