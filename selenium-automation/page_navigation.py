import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

Driver = webdriver.Firefox()

Driver.maximize_window()
Driver.get("https://www.gsmarena.com/")
All_Brands = Driver.find_element(by=By.XPATH, value="//aside[@class='sidebar col left']/div/ul/li[1]/a")
All_Brands.click()
time.sleep(2)
Driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
next_page = Driver.find_element(by=By.XPATH, value="//a[@class='pages-next']")
while next_page:
    next_page.click()
    Driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    try:
        next_page = Driver.find_element(by=By.XPATH, value="//a[@class='pages-next']")
    except:
        next_page = None
    print(next_page)

Driver.close()
Driver.quit()
