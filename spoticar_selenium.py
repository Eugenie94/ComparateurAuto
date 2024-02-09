from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import json

# On récupère les liens des voitures avec selenium pour ensuite les importer dans scrapy

driver = webdriver.Chrome()

driver.get("https://www.spoticar.fr/")

#page de consentement
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#_psaihm_button_param_accept"))
).click()

#bouton acheter
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#navbar-toggle"))
).click()

time.sleep(1)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#navbar > ul > li:nth-child(2) > a"))
).click()


url_list = []                                

#on récupère les liens de toute les voitures
for i in range(1, 833):
    driver.get(f"https://www.spoticar.fr/voitures-occasion?page={i}")
    links = driver.find_elements(By.CSS_SELECTOR, '.card-wrapper a')

    for link in links:
                url_list.append(link.get_attribute('href'))

driver.quit()


# enregistrer liens dans un json
json_file = "spoticar.json"
with open(json_file, 'w') as f:
    json.dump(url_list, f, indent=4)