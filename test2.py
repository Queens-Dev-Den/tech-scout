import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
driver.get('https://open.spotify.com/playlist/72D1vt56G2rUbIWLa0HC2R')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btE2c3IKaOXZ4VNAb8WQ"))
)

# Scroll down to load more songs using an interactable node
scroll_pause_time = 5  # Adjust the pause time if necessary
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.find_element(By.CLASS_NAME, 'btE2c3IKaOXZ4VNAb8WQ').send_keys(Keys.END)
    time.sleep(scroll_pause_time)  # Wait for the page to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # Check if the specified element is present
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    if soup.find("div", class_="yP3JLuwUNDIQHxRFilK3"):
        break
    
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