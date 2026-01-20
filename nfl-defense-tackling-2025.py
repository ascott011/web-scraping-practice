import requests
from bs4 import BeautifulSoup
import pandas as pd 

# check the status code to start as a habit

# header to say I am a browser and not some generic script
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = 'https://www.nfl.com/stats/team-stats/defense/tackles/2025/reg/all'

def get_stats(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retreive stats")
        print("Status code:", response.status_code)
        exit()

    soup = BeautifulSoup(response.content, 'html.parser')

    column_headers = soup.find("thead").text.splitlines()[2:-1] 
    table_body = soup.find("tbody")
    rows = table_body.find_all("tr")

    all_team_stats = []

    for row in rows:
        cells = row.find_all("td")
        #accounts for any blank cells
        if not cells:
            continue
        
        #team name entered twice so just grabbing once
        teams_data = []
        team_name_cell = cells[0]
        short_team_name = team_name_cell.find("div", class_="d3-o-club-shortname")
        teams_data.append(short_team_name.get_text(strip=True))
        
        #loop through the rest of the stats
        for cell in cells[1:]:
            teams_data.append(cell.get_text(strip=True))
        all_team_stats.append(teams_data)

    return column_headers, all_team_stats

column_headers, all_team_stats = get_stats(url, headers)

def create_pandas_df(data, headers):
    df = pd.DataFrame(data=data, columns=headers)

print(create_pandas_df(all_team_stats, column_headers))
