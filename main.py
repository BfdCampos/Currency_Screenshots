from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from playsound import playsound

print("Launching code...")

options = webdriver.ChromeOptions()
#options.headless = True

driver = webdriver.Chrome("chromedriver.exe")

print("Launching browser...")
time.sleep(0.5)
print("Getting all screenshots ready...")
time.sleep(0.5)
print("Approximate wait time 2 minutes 30 seconds")

""""Get's all pre-hard coded screenshots of currency pairs from XE.com"""

# CAD to IND

driver.get("https://www.xe.com/")


webdriver_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "amount")))

amount_box = driver.find_element_by_id("amount")
amount_box.clear()
amount_box.click()
amount_box.send_keys("1000")
amount_box.send_keys(Keys.RETURN)

send_country_box = driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[2]/section/div[2]/div/main/form/div[1]/div[3]"
)
send_country_box.click()
send_country_box_search = driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[2]/section/div[2]/div/main/form/div[1]/div[3]/div[2]/div/input"
)
send_country_box_search.click()
send_country_box.send_keys("Canada")
send_country_box.send_keys(Keys.RETURN)

receive_country_box = driver.find_element_by_id("midmarketToCurrency")
receive_country_box.click()
receive_country_box.send_keys("India")
receive_country_box.send_keys(Keys.RETURN)

convert_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/button")
convert_button.click()

driver.implicitly_wait(3)

view_full_chart_button = driver.find_element_by_link_text("View full chart")
view_full_chart_button.click()

driver.implicitly_wait(3)

one_month_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/section/div[2]/div/main/div/div[2]/div[2]/button[4]")
one_month_button.click()

time.sleep(5)
#except:
    #driver.set_window_size(width=1450, height=1370)
    #driver.get_screenshot_as_file('XE_CAD_to_INR_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

#else:
    #driver.set_window_size(width=1450, height=1370)
    #driver.get_screenshot_as_file('XE_CAD_to_INR_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

driver.quit()

print("Screenshots are ready")
playsound('Coin.mp3')

"""Zoom code: driver.execute_script("document.body.style.zoom='80%'")"""
"""Resolution code -  Large (default): driver.set_window_size(width=1877, height=1934)"""
