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
chrome_options = Options()
chrome_options.add_argument("—disable-gpu")
chrome_options.add_argument("--headless")
Driver = uc.Chrome(Options=chrome_options)
Driver.maximize_window()
Driver.get('https://whatmobile.web.pk/')
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

mobile_images = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/div/a")
mobile_names = Driver.find_elements(by=By.XPATH, value="//div[@class='product-grid8']/b/a")
mobile_companies = Driver.find_elements(by=By.XPATH, value="//ul[@class='brb']/a")

for m in range(len(mobile_names)):
    images_data.append(mobile_images[m].get_attribute("href"))
    names_data.append(mobile_names[m].text)
    hrefs.append(mobile_companies[m].get_attribute("href"))

for i in range(len(hrefs)):
    Driver.get(hrefs[i])
    mobile_images = Driver.find_elements(by=By.XPATH, value="//a[@class='link-text']")
    mobile_names = Driver.find_elements(by=By.XPATH, value="//h6[@class='mt-3']/a")
    for j in range(len(mobile_names)):
        images_data.append(mobile_images[j].get_attribute("href"))
        names_data.append(mobile_names[j].text)

for i in range(50):
    Driver.get(images_data[i])
    Driver.execute_script("window.scrollTo(0, 800)")
    button = WebDriverWait(Driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, "//li/a[contains(text(),'View Full Specs')]")))

    button.click()
    Driver.implicitly_wait(3)
    # Driver.execute_script("window.scrollTo(0, 100)")
    Specs = Driver.find_elements(by=By.XPATH,
                                 value="//span[@class='mmml-5']")
    print(model_no.append(Specs[0].text))
    release_date.append(Specs[1].text)
    status.append(Specs[2].text)
    operating_system.append(Specs[3].text)
    technology.append(Specs[4].text)
    sim_info.append(Specs[5].text)
    # print(lock_security.append(Specs[6].text))
    # best_for.append(Specs[10].text)
    # price.append(Specs[11].text)
    # dimensions.append(Specs[12].text)
    # weight.append(Specs[13].text)
    # coulour_options.append(Specs[14].text)
    # build_material.append(Specs[15].text)
    # certification.append(Specs[16].text)
    # display_type.append(Specs[17].text)
    # screen_size.append(Specs[18].text)
    # resolution.append(Specs[19].text)
    # ppi.append(Specs[20].text)
    # refresh_rate.append(Specs[21].text)
    # chipest.append(Specs[22].text)
    # cpu.append(Specs[23].text)
    # gpu.append(Specs[24].text)
    # slot.append(Specs[25].text)
    # ram_rom.append(Specs[26].text)
    # rear_camera_setup.append(Specs[27].text)
    # main_sensor.append(Specs[28].text)
    # sensor_type.append(Specs[29].text)
    # rear_camera_aperture.append(Specs[30].text)
    # rear_camera_fatures.append(Specs[31].text)
    # video_rec.append(Specs[32].text)
    # front_camera_setup.append(Specs[33].text)
    # fron_sensor.append(Specs[34].text)
    # front_camera_sensor_type.append(Specs[35].text)
    # front_camera_features.append(Specs[36].text)
    # batery_type.append(Specs[37].text)
    # batery_capacity.append(Specs[38].text)
    # fast_charge.append(Specs[39].text)
    # wireless_charge.append(Specs[40].text)
    # blutooth.append(Specs[41].text)
    # wifi.append(Specs[42].text)
    # more.append(Specs[43].text)
    # g3_net.append(Specs[44].text)
    # g4_net.append(Specs[45].text)
    # g5_net.append(Specs[46].text)
    # net_speed.append(Specs[47].text)

data = {
    "Name": names_data,
    "Image": images_data,
    "Model No.": model_no,
    "Release Date": release_date,
    "Status": status,
    "Operating System": operating_system,
    "Technology": technology,
    "Sim Info": sim_info,
    "Lock Security": lock_security,
    # "Best For": best_for,
    # "Price": price,
    # "Dimensions": dimensions,
    # "Weight In Grams": weight,
    # "Colour Options": coulour_options,
    # "Build Material": build_material,
    # "Certification": certification,
    # "Protection":protection
    # "Display Type": display_type,
    # "Screen Size": screen_size,
    # "Resolution": resolution,
    # "PPI": ppi,
    # "Refresh Rate": refresh_rate,
    # "Chipest": chipest,
    # "CPU": cpu,
    # "GPU": gpu,
    # "Slot": slot,
    # "RAM and ROM": ram_rom,
    # "Rear Camera Setup": rear_camera_setup,
    # "Main Sensor": main_sensor,
    # "Rear Camera Sensor Type": sensor_type,
    # "Rear Camera Aperture": rear_camera_aperture,
    # "Rear Camera Features": rear_camera_fatures,
    # "Video Rec.": video_rec,
    # "Front Camera Setup": front_camera_setup,
    # "Front Sensor": fron_sensor,
    # "Front Camera Sensor Type": front_camera_sensor_type,
    # "Front Camera Mechanism": front_camera_mechanism
    # "Fron Camera Features": front_camera_features,
    # "Battery Type": batery_type,
    # "Capacity": batery_capacity,
    # "Fast Charge": fast_charge,
    # "Wireless Charge": wireless_charge,
    # "Blutooth": blutooth,
    # "WiFi": wifi,
    # "More": more,
    # "3G Net.": g3_net,
    # "4G Net.": g4_net,
    # "5G Net.": g5_net,
    # "Net. Speed": net_speed
}

df = pd.DataFrame(data=data)
df.to_excel("mb.xlsx")
print(Driver.title)
time.sleep(10)
