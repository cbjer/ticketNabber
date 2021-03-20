from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = '/Users/chris/Coding/Shell/chromeDriver/chromedriver'

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get("https://www.google.com")
driver.get("https://www.ra.co")
time.sleep(100)
driver.close()

def getChromeDriver():
    """
    Logs us into resident advisor and returns the drver object
    """
    pass

def addTicketToBasket(driver, ticketName):
    pass



