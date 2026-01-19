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
    print(rows[1])
    # for row in rows:
    #     cells = row.find_all("td")
    #     print(cells[0:4])

get_stats(url, headers)