from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

# Artists
# UudGCx16EmBkuFPllvss

# Songs
# btE2c3IKaOXZ4VNAb8WQ

driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
driver.get('https://open.spotify.com/playlist/03BUWWy6N5FlYw2VqUWwqE')

driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# artists = soup.find_all('span', attrs={"class":"UudGCx16EmBkuFPllvss"})
songs = soup.find_all("div", class_="btE2c3IKaOXZ4VNAb8WQ")

file = open('songs.csv', 'w')
writer = csv.writer(file)

writer.writerow(['SONGS'])

for song in zip(songs):
    print(song.text)
    writer.writerow([song.text])
file.close()