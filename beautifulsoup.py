import requests
from bs4 import BeautifulSoup


# check the status code to start as a habit

# header to say I am a browser and not some generic script
headers = {
    "User-Agent": "Mozilla/5.0"
}

url = 'https://en.wikipedia.org/wiki/Green_Bay_Packers'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

h1 = soup.find("h1").get_text()

print(response.status_code)
print(h1)


# url = requests.get('https://www.wsj.com/').text
# soup = BeautifulSoup(url, 'html.parser')

# print(soup.find("h1").get_text())

