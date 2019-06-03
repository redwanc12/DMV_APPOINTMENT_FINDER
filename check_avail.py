from bs4 import BeautifulSoup
from calendar import monthrange

locationList = ['Kapalama', 'Kapolei', 'Koolau', 'Wahiawa', 'Waianae']

class openFinder(object):
    # class to find open dates
    def __init__(self):
        self.locationList = locationList
    
    def findDates(self, data):
        """Returns a list of open dates from a specific day"""
        soup = BeautifulSoup(data, 'html.parser')
        times = soup.find_all('tr', {'class':['TableItemLine', 'TableAltItemLine']})
        day = soup.find("span", {"id": "lblDate"}).text
        
        listOfDateDict = []

        for each in times:
            time = each.td.text
            spots = each.find_all(['input', 'span'])
            for index, spot in enumerate(spots):
                if('None' != spot.text):
                    dateDict = {
                        'openings': spot['value'],
                        'time': time,
                        'location': locationList[index],
                        'day': day
                    }
                    listOfDateDict.append(dateDict)
        return listOfDateDict

    def date_id(self, month, day, year=2019):
        #Converts month and day to the day ID used by DMV
        month = int(month)
        day = int(day)
        year = int(year)
        b = 6939 #constant only works after 5/9
        for each in range(month-1):
            b += monthrange(year, each+1)[1]
        b += day
        return b

    def compare_date_differece(self, old_source, new_source):
        """Compares how many days away from the current day a new date is"""
        soup = BeautifulSoup(old_source, 'html.parser')
        old_day = soup.find("span", {"id": "lblDate"}).text
        old_day_attrs = old_day.split('/')
        old_id = (self.date_id(old_day_attrs[0], old_day_attrs[1], old_day_attrs[2]))

        soup = BeautifulSoup(new_source, 'html.parser')
        new_day = soup.find("span", {"id": "lblDate"}).text
        new_day_attrs = new_day.split('/')
        new_id = (self.date_id(new_day_attrs[0], new_day_attrs[1], new_day_attrs[2]))

        return new_id - old_id

    