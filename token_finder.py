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

    def scrapeDate(self, date):
        self.driver.get(self.url)
        try:
            self.driver.find_element_by_name('btnAcceptTop').click()
            self.driver.find_element_by_xpath('//*[@title="{}"]'.format(date)).click()
        except NoSuchElementException:
            pass
        
        file = open('nudes2.html', 'w')
        file.write(self.driver.page_source)
        file.close()

        self.driver.close()


if __name__ == '__main__':
    scraper = tokenFinder()
    scraper.scrapeDate("May 24")

