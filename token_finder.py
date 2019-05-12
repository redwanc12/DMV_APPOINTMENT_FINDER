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

    def authenticateClient(self):
        # Validates driver. Returns default date.
        self.driver.get(self.url)
        try:
            self.driver.find_element_by_name('btnAcceptTop').click()
        except NoSuchElementException:
            pass

        return(self.driver.page_source) 

    def scrapeDate(self, date):
        # uses web driver to access a new page
        try:
            self.driver.find_element_by_xpath('//*[@title="{}"]'.format(date)).click()
        except NoSuchElementException:
            pass

        return(self.driver.page_source)

    def nextMonth(self):
        try:
            self.driver.find_element_by_xpath('//*[@title="Go to the next month"]').click()
        except NoSuchElementException:
            pass
        return(self.driver.page_source)

    def closeDriver(self):
        self.driver.close()

        


if __name__ == '__main__':
    scraper = tokenFinder()
    dateList = ["May 28", "May 29", "June 13"]
    scraper.authenticateClient()
    for each in dateList:
        if('May' not in each):
            scraper.nextMonth()
        file = open(each +'.html', 'w')
        file.write(scraper.scrapeDate(each))
        file.close()
    scraper.closeDriver()

