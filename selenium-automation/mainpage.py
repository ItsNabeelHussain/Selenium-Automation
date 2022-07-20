import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

model_no = []
release_date = []
status = []
operating_system = []
technology = []
sim_info = []
lock_security = []
price = []
hrefs = []
images_data = []
names_data = []
chrome_options = Options()
chrome_options.add_argument("—disable-gpu")
chrome_options.add_argument("--headless")
Driver = uc.Chrome(Options=chrome_options)
Driver.maximize_window()
Driver.get('https://whatmobile.web.pk/')
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

mobile_images = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/div/a")
mobile_names = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/b/a")
mobile_prices = Driver.find_elements(by=By.XPATH, value="//div[@class ='price small']")
mobile_companies = Driver.find_elements(by=By.XPATH, value="//ul[@class='brb']/a")

for m in range(len(mobile_names)):
    images_data.append(mobile_images[m].get_attribute("href"))
    names_data.append(mobile_names[m].text)
    price.append(mobile_prices[m].text)
    hrefs.append(mobile_companies[m].get_attribute("href"))

for i in range(len(hrefs)):
    Driver.get(hrefs[i])
    mobile_images = Driver.find_elements(by=By.XPATH, value="//a[@class='link-text']")
    mobile_names = Driver.find_elements(by=By.XPATH, value="//h6[@class='mt-3']/a")
    mobile_prices = Driver.find_elements(by=By.XPATH, value="//div[@class ='price small']")
    for j in range(len(mobile_names)):
        images_data.append(mobile_images[j].get_attribute("href"))
        names_data.append(mobile_names[j].text)
        price.append(mobile_prices[j].text)

for image in images_data:
    Driver.get(image)
    Driver.execute_script("window.scrollTo(0, 800)")
    try:
        button = WebDriverWait(Driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, "//li/a[contains(text(),'View Full Specs')]")))
        button.click()
        Driver.implicitly_wait(30)
    except:
        pass

    time.sleep(2)
    try:
        Elements = WebDriverWait(Driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mmml-5']")))
        Driver.implicitly_wait(3)
        time.sleep(1)
        print(Elements[0].text)
    except:
        pass

data = {
    "Name": names_data,
    "Image": images_data,
    "Price": price,
    # "Model No.": model_no,
    # "Release Date": release_date,
    # "Status": status,
    # "Operating System": operating_system,
    # "Technology": technology,
    # "Sim Info": sim_info,
    # "Lock Security": lock_security
}

df = pd.DataFrame(data=data)
df.to_excel("mb.xlsx")
print(Driver.title)
time.sleep(10)
