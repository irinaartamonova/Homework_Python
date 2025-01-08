from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

time.sleep(5)

close_button = driver.find_element(By.CSS_SELECTOR, ".modal-close")

close_button.click()

driver.quit()
