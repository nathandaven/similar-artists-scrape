import requests
import urllib.request
from bs4 import BeautifulSoup

print ("enter url from similar-artists.info: ")
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

artists = []

for artist in soup.findAll('div', attrs={'class':'discounted-item movie video-playlist'}):
    artists.append(artist.find('h1'))

print("length: ", len(artists))
for i in range(len(artists)):
    string = str(artists[i])
    print(string[4:len(string) - 5] + ", ", end="")
