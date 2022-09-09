# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#
from selenium.webdriver.common.by import By

s = Service(r"/Browsers/chromedriver.exe")
browser = webdriver.Chrome(service=s)
url = 'https://www.saucedemo.com/'
browser.get(url)

username_text = browser.find_element(by=By.XPATH, value="//input[@id='user-name']")
username_text.send_keys("test123")
username_text = browser.find_element(by=By.XPATH, value="//input[@id='password']")
username_text.send_keys("password")
browser.find_element(by=By.XPATH, value="//input[@type='submit']").click()
error_text = browser.find_element(by=By.XPATH, value="//h3[@data-test='error']").text
print('\nERROR TEXT PRINTED HERE '+str(error_text))


