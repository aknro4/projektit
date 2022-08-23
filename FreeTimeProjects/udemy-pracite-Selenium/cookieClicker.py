from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\computer\downloads\chromeDrivers\chromedriver.exe"
cookie_page = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(chrome_driver_path)
driver.get(cookie_page)

store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
store_items = [item.get_attribute("id") for item in store]

click_cookie = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    click_cookie.click()

    if time.time() > timeout:
        item = driver.find_elements(By.CSS_SELECTOR, value=f"#store b")
        item_prices = []

        for price in item:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        money = driver.find_element(By.ID, value="money").text

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = store_items[n]

        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        can_afforod = True

        while can_afforod:

            print(affordable_upgrades)
            try:
                highest_price_affordable_upgrade = max(affordable_upgrades)
                to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
                driver.find_element(By.ID, to_purchase_id).click()

            except ValueError:
                can_afforod = False

            try:
                affordable_upgrades.pop(max(affordable_upgrades))
            except ValueError:
                can_afforod = False

            print(affordable_upgrades)

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
