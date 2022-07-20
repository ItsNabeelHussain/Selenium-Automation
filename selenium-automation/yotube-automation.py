import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

Driver = uc.Chrome()
Driver.get("https://www.youtube.com/")
Driver.maximize_window()
wait = WebDriverWait(Driver, 10)

# use of XPATH to locate elements

search_box = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='search']")))
search_box.send_keys("Selenium crash course")

# use of ID to locate elements

search_button = wait.until(ec.visibility_of_element_located((By.ID, 'search-icon-legacy')))
search_button.click()
play_video = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@id='video-title'][1]")))
play_video.click()

# locating element by class name

play_button = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "ytp-play-button")))
play_button.click()
mini_play_button = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'ytp-next-button')))
mini_play_button.click()
print(Driver.title)
time.sleep(50)
