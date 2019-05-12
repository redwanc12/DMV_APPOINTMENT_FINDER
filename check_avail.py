from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path

LINK = "https://www12.honolulu.gov/csdarts/frmApptInt.aspx"
driver = webdriver.Chrome(str(Path().absolute()) + '/chromedriver' )
driver.get(LINK)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

