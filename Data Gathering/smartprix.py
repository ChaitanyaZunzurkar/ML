from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

s = Service("D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe.exe")

driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)

driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span').click()

time.sleep(1)

driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span').click()

old_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == old_height: 
        break

    old_height = new_height

html = driver.page_source

with open('smartprix.html' , 'w' , encoding='utf-8') as f:
    f.write(html)

input("Please enter to stop.")