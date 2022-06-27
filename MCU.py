from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

user_input = input("character: ")
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://www.marvel.com/search")

search_input_xpath = "//input[@placeholder='Search']"
search_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, search_input_xpath)))
search_input.send_keys(user_input)

first_item_in_auto_suggest_area_xpath = "//div[contains(@id,'react-autowhatever')]/ul"
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, first_item_in_auto_suggest_area_xpath)))
search_input.send_keys(Keys.ENTER)

section = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".search-list p.card-body__headline a")))

character = driver.find_elements(By.CSS_SELECTOR, ".search-list p.card-body__headline a")
for character_tag in character:
    print(character_tag.text)
    print(character_tag.get_attribute("href"))

driver.close()
