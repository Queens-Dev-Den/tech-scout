from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
driver.get('https://open.spotify.com/playlist/03BUWWy6N5FlYw2VqUWwqE')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btE2c3IKaOXZ4VNAb8WQ"))
)

# Scroll down to load more songs
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find song elements
songs = soup.find_all("div", class_="btE2c3IKaOXZ4VNAb8WQ")

# Check if songs are found
if not songs:
    print("No songs found. Please check the class name or the page structure.")
else:
    print(f"Found {len(songs)} songs.")

# Write to CSV
with open('songs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['SONGS'])
    for song in songs:
        song_text = song.get_text(strip=True)
        print(song_text)
        writer.writerow([song_text])

# Close the WebDriver
driver.quit()