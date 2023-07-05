from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
import time


def chromeInteraction():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    return options


driver = webdriver.Chrome(options=chromeInteraction())
driver.get("https://github.com/")
time.sleep(5)
print(driver.title)
driver.find_element(By.XPATH , "//a[@class='HeaderMenu-link HeaderMenu-link--sign-in flex-shrink-0 no-underline d-block d-lg-inline-block border border-lg-0 rounded rounded-lg-0 p-2 p-lg-0']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='login_field']").send_keys("soumili31")
driver.find_element(By.XPATH, "//input[@id='login_field']//input[@id='login_field']//input[@id='login_field']").send_keys("Soumili@310705")
driver.find_element(By.XPATH , "//input[@name='commit']").click()
time.sleep(2)
driver.find_element(By.XPATH , "//a[contains(text(),'New')]").click()
time.sleep(2)
driver.find_element(By.XPATH , "//input[@id='react-aria-2']").send_keys("SeleniumTest")
time.sleep(2)
driver.find_element(By.XPATH , "//input[@id='react-aria-8']").click()
time.sleep(4)
driver.find_element(By.XPATH , "//span[contains(text(),'Create repository')]").click()
driver.find_element(By.XPATH , "//a[@aria-label='Edit this file']//*[name()='svg']").click()
driver.find_element(By.XPATH,"//div[@class='cm-line']").send_keys("This Readme file is updated via automation")
time.sleep(5)
driver.find_element(By.XPATH , "//span[contains(text(),'Commit changes...')]").click()
driver.quit()