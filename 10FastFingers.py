from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Website of typing test
URL = 'https://10fastfingers.com/typing-test/english'

# Open chrome webdriver to full screen
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

wait = WebDriverWait(driver, 10)

# # Close the cookie notification at top 
closeCookie = wait.until(EC.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonAccept')))
closeCookie.click()

# Wait for the words to appear on the page
wordlist = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'highlight')))

# Find the input box
input = driver.find_element_by_id("inputfield")

# Type each word out 
for i in range(345):
    # Find the current word to type
    word = driver.find_element_by_class_name("highlight").text

    # Test is over
    if word == ' ':
        break

    # Type each word 1 character at a time w/ slight delay to look more humanlike 
    for aChar in word:
        input.send_keys(aChar)
        time.sleep(.04)

    # Enter space after each word to move on
    input.send_keys(Keys.SPACE)

# Pause for 5 seconds after test is done then close browser
time.sleep(5)
driver.close()