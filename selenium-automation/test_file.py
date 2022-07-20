import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

model_no = []
release_date = []
status = []
operating_system = []
technology = []
sim_info = []
lock_security = []
best_for = []
price = []
dimensions = []
weight = []
coulour_options = []
build_material = []
certification = []
protection = []
display_type = []
screen_size = []
resolution = []
ppi = []
refresh_rate = []
chipest = []
cpu = []
gpu = []
slot = []
ram_rom = []
rear_camera_setup = []
main_sensor = []
sensor_type = []
rear_camera_aperture = []
rear_camera_fatures = []
video_rec = []
front_camera_setup = []
fron_sensor = []
front_camera_sensor_type = []
front_camera_mechanism = []
front_camera_features = []
batery_type = []
batery_capacity = []
fast_charge = []
wireless_charge = []
blutooth = []
wifi = []
more = []
g3_net = []
g4_net = []
g5_net = []
net_speed = []
hrefs = []
images_data = []
spec_data = []
names_data = []

Driver = webdriver.Firefox()
Driver.maximize_window()
Driver.get('https://whatmobile.web.pk/')

# mobile_images = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/div/a")
# mobile_names = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/b/a")
# mobile_companies = Driver.find_elements(by=By.XPATH, value="//ul[@class='brb']/a")
#
# for m in range(len(mobile_names)):
#     images_data.append(mobile_images[m].get_attribute("href"))
#     names_data.append(mobile_names[m].text)
#     # hrefs.append(mobile_companies[m].get_attribute("href"))
#
# for i in range(len(hrefs)):
#     Driver.get(hrefs[i])
#     mobile_images = Driver.find_elements(by=By.XPATH, value="//a[@class='link-text']")
#     mobile_names = Driver.find_elements(by=By.XPATH, value="//h6[@class='mt-3']/a")
#     for j in range(len(mobile_names)):
#         images_data.append(mobile_images[j].get_attribute("href"))
#         names_data.append(mobile_names[j].text)
#
# for i in range(len(images_data)):
#     Driver.get(images_data[i])
#     Driver.execute_script("window.scrollTo(0, 800)")
#     button = WebDriverWait(Driver, 20).until(
#         ec.element_to_be_clickable((By.XPATH, "//li/a[contains(text(),'View Full Specs')]")))
#     Driver.implicitly_wait(2)
#     button.click()
#     Driver.implicitly_wait(1)
#     # Driver.execute_script("window.scrollTo(0, 100)")
#     Specs = Driver.find_elements(by=By.XPATH,
#                                  value="//span[@class='mmml-5']")
#     Driver.implicitly_wait(2)
#     model = model_no.append(Specs[0].text)
#     Driver.implicitly_wait(2)
#     release_date.append(Specs[1].text)
#     Driver.implicitly_wait(4)
#     status.append(Specs[2].text)
#     Driver.implicitly_wait(4)
#     operating_system.append(Specs[3].text)
#     Driver.implicitly_wait(4)
#     technology.append(Specs[4].text)
#     Driver.implicitly_wait(4)
#     sim_info.append(Specs[5].text)
#     Driver.implicitly_wait(4)
#     print(lock_security.append(Specs[6].text))
#
# data = {
#     "Name": names_data,
#     "Image": images_data,
#     "Model No.": model_no,
#     "Release Date": release_date,
#     "Status": status,
#     "Operating System": operating_system,
#     "Technology": technology,
#     "Sim Info": sim_info,
#     "Lock Security": lock_security,
#
# }
#
# df = pd.DataFrame(data=data)
# df.to_excel("mbs.xlsx")
# print(Driver.title)
# time.sleep(10)
# Driver.close()
# Driver.quit()
Driver.get("https://www.tutorialspoint.com/index.htm");
# open file in write and binary mode
with open('images/Logo.png', 'wb') as file:
    # identify image to be captured
    l = Driver.find_element_by_xpath('//*[@alt="Tutorialspoint"]')
    # write file
    file.write(l.screenshot_as_png)
# close browser
Driver.quit()
