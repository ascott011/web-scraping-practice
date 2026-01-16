import requests
from bs4 import BeautifulSoup


# check the status code to start as a habit

# header to say I am a browser and not some generic script
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = 'https://www.nfl.com/stats/team-stats/'

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    print(response.status_code)
    exit()
soup = BeautifulSoup(response.content, 'html.parser')

headers = soup.find("thead").text.splitlines()
table_body = soup.find("tbody")
rows = table_body.find_all("tr")
cells = rows[1].find_all("td")

print(list(headers)[2:])
print([cell.get_text(strip=True) for cell in cells])
