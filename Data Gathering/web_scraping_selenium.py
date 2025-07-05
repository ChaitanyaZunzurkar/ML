from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service("D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe.exe")

driver = webdriver.Chrome(service = s)

driver.get('https://www.ajio.com/men-caps-hats/c/830202001')
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')

counter = 1
while True:
    driver.execute_script('window.scrollTo(0 , document.body.scrollHeight)')
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(counter)
    counter += 1
    print(old_height , " " , new_height)

    if new_height == old_height:
        break

    old_height = new_height


html = driver.page_source

with open('ajio.html' , 'w' , encoding='utf-8') as f:
    f.write(html)



