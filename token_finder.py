import re
import string
from urllib.parse import urlparse
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

LINK = "https://www12.honolulu.gov/csdarts/frmApptInt.aspx"


class tokenFinder(object):
    # token finder class
    def __init__(self):
        self.url = LINK
        self.driver = webdriver.Chrome(str(Path().absolute()) + '/chromedriver' )
        self.driver.set_window_size(1120, 550)

    def scrape(self):
        self.driver.get(self.url)

    
if __name__ == '__main__':
    scraper = tokenFinder()
    scraper.scrape()

