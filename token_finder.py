
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
        # uses web driver to access a new page.
        try:
            self.driver.find_element_by_xpath('//*[@title="{}"]'.format(date)).click()
        except NoSuchElementException:
            pass

        return(self.driver.page_source)

    def nextMonth(self):
        # Mimicks the action of pressing the next month button.
        try:
            self.driver.find_element_by_xpath('//*[@title="Go to the next month"]').click()
        except NoSuchElementException:
            pass
        return(self.driver.page_source)

    def closeDriver(self):
        self.driver.close()

    def getEventVal(self, source):
        soup = BeautifulSoup(source, 'html.parser')
        eventVal = soup.find("input", {"id": "__EVENTVALIDATION"})['value']
        return eventVal


if __name__ == '__main__':
    scraper = tokenFinder()
    scraper.authenticateClient()
    data = scraper.scrapeDate('May 22')
    print(scraper.getEventVal(data))
    scraper.closeDriver()
