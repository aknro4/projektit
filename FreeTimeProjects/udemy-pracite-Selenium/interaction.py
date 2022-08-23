from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\computer\downloads\chromeDrivers\chromedriver.exe"
website_path = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(website_path)

# articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# articles.click()

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("AODuhwpoauhid")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("döawhdoiö")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("wajöodijsklafnlk")

button = driver.find_element(by=By.CSS_SELECTOR, value="form button")
button.click()

# driver.quit()
