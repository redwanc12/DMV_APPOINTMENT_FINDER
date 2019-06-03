import requests
from calendar import monthrange
from token_finder import tokenFinder

LINK = "https://www12.honolulu.gov/csdarts/frmApptInt.aspx"

headers = {
    'Origin':'https://www12.honolulu.gov',
    'Upgrade-Insecure-Requests':'1',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}


class httpRequester(object):
    #handles requests through HTTP. No driver needed

    tokenList = []
    
    def __init__(self):
        self.url = LINK
        self.headers = headers
    
    def appendTokenList(self, dateID, eventVal, viewState):
        # adds a new token to the list of saved tokens
        self.tokenList.append({
            'dateID': dateID,
            'eventVal': eventVal,
            'viewState':viewState
        })

    def getToken(self, dateID):
        # retrieves a token
        for each in self.tokenList:
            if(each['dateID'] == dateID):
                return each

    def date_id(self, month, day, year=2019):
    #Converts month and day to the day ID used by DMV
        b = 6939 #constant only works after 5/9
        for each in range(month-1): 
            b += monthrange(year, each+1)[1]
        b+=day
        return b

    def GetPage(self, dateID, eventVal, viewstate):
        #Gets page using dateID, eventVal, viewState

        self.data = {
        '__EVENTARGUMENT':dateID,
        '__EVENTTARGET':'Calendar1',
        '__EVENTVALIDATION': eventVal,
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEENCRYPTED':'',
        '__VIEWSTATEGENERATOR':'D050787D',
        'ddlLocation':'0'
        }

        page = requests.post(
            self.url,
            data=self.data,
            headers=self.headers,
        )
        return page.text
