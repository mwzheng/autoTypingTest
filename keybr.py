from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = 'https://www.keybr.com/'
driver =  webdriver.Chrome(ChromeDriverManager().install())

# Site where we want to do typing test
driver.get(URL)

# Open browser in full screen
driver.maximize_window()

# Close the pop-up when site first loads
driver.find_element_by_class_name("Tour-close").click()

# Turn on dark mode
driver.find_element_by_css_selector('#Nav > div > div:nth-child(2) > div > button:nth-child(1)').click()

# Click on area to start typing
driver.find_element_by_class_name("TextInput-label").click()

# Change to complete however many tests you want
testNumber = 1

# Keeps track of current test 
currTestNumber = 0

while currTestNumber != testNumber:
    print("Current Test number: " + str(currTestNumber + 1))

    # Initialize action chain 
    action = ActionChains(driver)
    
    # Find all of the letters in the typing test
    characters = driver.find_elements_by_class_name("TextInput-item")

    # Read each character & add it into the action chain w/ a delay after each input
    # Change pause time to go faster or slower when actual typing begins 
    for element in characters:
        char = element.text
        if (char != '␣'):
            action.pause(.1).send_keys(char)
        else:
            action.pause(.05).send_keys(Keys.SPACE)

    # Complete the current test
    action.perform()
    currTestNumber += 1

print("done")

# After test are complete wait 5 secs & close browser
time.sleep(5)
driver.quit()