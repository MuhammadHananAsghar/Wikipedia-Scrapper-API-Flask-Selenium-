from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


CHROMEDRIVER_PATH = "/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/chromedriver"

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)


def search(USER_INPUT):
	driver.get("https://www.wikipedia.org/")
	search_input = driver.find_element_by_id("searchInput")
	search_button = driver.find_element_by_css_selector(".pure-button")
	search_input.send_keys(USER_INPUT)
	search_button.click()
	element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/head/title")))
	data_text = driver.find_elements_by_tag_name("p")
	collected_data = []
	for data in data_text:
		data = data.text
		pattern = r'\[.*?\]'
		refined_data = re.sub(pattern, '', data)
		collected_data.append(refined_data.strip())

	collected_data = '\n'.join(collected_data)
	return collected_data
