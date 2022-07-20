import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

Driver = webdriver.Firefox()
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
Driver.maximize_window()
Driver.get("https://www.gsmarena.com/")
All_Brands = Driver.find_element(by=By.XPATH, value="//p[@class='pad']/a[@class='pad-multiple pad-allbrands']/span")
All_Brands.click()
time.sleep(5)

mobile_companies = []
mobiles = []
links = []
Spec = []
price = []
colors = []
memory = []
battery = []
o_s = []

Elements = Driver.find_elements(by=By.XPATH, value="//table/tbody/tr/td/a")
for element in Elements:
    mobile_companies.append(element.get_attribute("href"))

for mobile in mobile_companies:
    Driver.get(mobile)
    Driver.implicitly_wait(10)
    mobile_names = Driver.find_elements(by=By.XPATH, value="//div[@class='makers']/ul/li/a/strong/span")
    mobile_link = Driver.find_elements(by=By.XPATH, value="//div[@class='makers']/ul/li/a")
    Specs = Driver.find_elements(by=By.XPATH, value="//div[@class='makers']/ul/li/a/img")
    time.sleep(2)
    for i in range(len(mobile_names)):
        mobiles.append(mobile_names[i].text)
        links.append(mobile_link[i].get_attribute("href"))
        Spec.append(Specs[i].get_attribute("title"))
    Driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    try:
        next_page = Driver.find_element(by=By.XPATH, value="//a[@class='pages-next']")
    except:
        next_page = None
    while next_page:
        next_page.click()
        time.sleep(2)
        mobile_names = Driver.find_elements(by=By.XPATH, value="//div[@class='makers']/ul/li/a/strong/span")
        mobile_link = Driver.find_elements(by=By.XPATH, value="//div[@class='makers']/ul/li/a")
        Specs = Driver.find_elements(by=By.XPATH, value="//div[@class='makers']/ul/li/a/img")

        for i in range(len(mobile_names)):
            mobiles.append(mobile_names[i].text)
            links.append(mobile_link[i].get_attribute("href"))
            Spec.append(Specs[i].get_attribute("title"))

        Driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        try:
            next_page = Driver.find_element(by=By.XPATH, value="//a[@class='pages-next']")
        except:
            next_page = None
        print(next_page)

data = {
    "Name": mobiles,
    "Link": links,
    "Spec. Desc.": Spec,
}

df = pd.DataFrame(data=data)
df.to_excel("mobile.xlsx")
# for i in range(100):
#     Driver.get(links[i])
#     Driver.implicitly_wait(3)
#     try:
#         price.append((Driver.find_element(by=By.XPATH, value="//td[@data-spec='price']")).text)
#     except:
#         price.append("N/A")
#
#     print(price)
#
#     try:
#         memory.append((Driver.find_element(by=By.XPATH, value="//td[@data-spec='internalmemory']")).text)
#     except:
#         memory.append("N/A")
#
#     print(memory)
#
#     try:
#         o_s.append((Driver.find_element(by=By.XPATH, value="//td[@data-spec='os']")).text)
#     except:
#         o_s.append("N/A")
#
#     print(o_s)
#
#     try:
#         battery.append((Driver.find_element(by=By.XPATH, value="//td[@data-spec='batdescription1']")).text)
#     except:
#         battery.append("N/A")
#
#     print(battery)
#
#     try:
#         colors.append((Driver.find_element(by=By.XPATH, value="//td[@data-spec='colors']")).text)
#     except:
#         colors.append("N/A")
#
#     print(colors)
#
#
# Data = {
#     "Price": price,
#     "Color": colors,
#     "Memory": memory,
#     "OS": o_s,
#     "Battery": battery,
# }
#
#
# Df = pd.DataFrame(data=Data)
# Df.to_excel("spec.xlsx")

Driver.close()
Driver.quit()
