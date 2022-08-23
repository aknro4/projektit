from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\computer\downloads\chromeDrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

date = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > time")
date_list = [event.text for event in date]

events = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > a")
event_list = [event.text for event in events]

dic = {}

for i in range(0, len(date_list)):
    dic[i] = {
        "time": date_list[i],
        "name": event_list[i]
    }

print(dic)

driver.quit()
