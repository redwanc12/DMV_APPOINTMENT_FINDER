"""Class to use webDriver to scrape data"""
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

LINK = "https://www12.honolulu.gov/csdarts/frmApptInt.aspx"


class tokenFinder(object):
    # token finder class, uses web driver
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
            self.nextMonth()
            return self.scrapeDate(date)

        return(self.driver.page_source)

    def nextMonth(self):
        # Mimicks the action of pressing the next month button.
        try:
            self.driver.find_element_by_xpath('//*[@title="Go to the next month"]').click()
        except NoSuchElementException:
            pass
        return(self.driver.page_source)

    def prevMonth(self):
        # Mimicks the action of pressing the next month button.
        try:
            self.driver.find_element_by_xpath('//*[@title="Go to the previous month"]').click()
        except NoSuchElementException:
            pass
        return(self.driver.page_source)

    def nextDayWithOpens(self):
        # Mimicks the action of pressing the go again button.
        try:
            self.driver.find_element_by_xpath('//*[@title="Click to find the next available appointment from the current selected date on the calendar."]').click()
        except NoSuchElementException:
            pass
        return(self.driver.page_source)

    def getDayList(self, ammount):
        """Gets the list of days that are not weekends or holidays"""
        self.refresh()
        dateList = []
        pageList = self.getDayListOnPage(self.driver.page_source)
        for each in pageList:
            if len(dateList) < ammount:
                dateList.append(each)
        while(len(dateList) < ammount):
            self.nextMonth()
            pageList = self.getDayListOnPage(self.driver.page_source)
            for each in pageList:
                if len(dateList) < ammount and not each in dateList:
                    dateList.append(each)
        return dateList

    def getDayListOnPage(self, source):
        """Finds a list of all clickable days on 1 page"""
        dateList = []
        soup = BeautifulSoup(source, 'html.parser')
        parser = soup.find_all('a')
        for each in parser:
            try:
                if 'javascript:__doPostBack' in each['href']:
                    dateList.append(each['title'])
            except Exception:
                pass

        dateList.remove('Go to the previous month')
        dateList.remove('Go to the next month')
        return dateList


    def closeDriver(self):
        self.driver.close()

    def getEventVal(self, source):
        #Returns the Event Validation of a given HTML source
        soup = BeautifulSoup(source, 'html.parser')
        eventVal = soup.find("input", {"id": "__EVENTVALIDATION"})['value']
        return eventVal

    def getViewState(self, source):
        # Returns the viewState of a given HTML source
        soup = BeautifulSoup(source, 'html.parser')
        vs = soup.find("input", {"id": "__VIEWSTATE"})['value']
        return vs

    def refresh(self):
        """goes to the current date page"""
        self.driver.get(self.url)
        return(self.driver.page_source)
