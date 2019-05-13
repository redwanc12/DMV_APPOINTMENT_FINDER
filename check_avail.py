from bs4 import BeautifulSoup

locationList = ['Kapalama', 'Kapolei', 'Koolau', 'Wahiawa', 'Waianae']

class openFinder(object):
    # class to find open dates
    def __init__(self):
        self.locationList = locationList
    
    def findDates(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        times = soup.find_all('tr', {'class':['TableItemLine','TableAltItemLine']})
        
        listOfDateDict = []

        for each in times:
            time = each.td.text
            spots = each.find_all(['input', 'span'])
            for index, spot in enumerate(spots):
                if('None' != spot.text):
                    dateDict = {
                        'openings': spot['value'],
                        'time': time,
                        'location': locationList[index]
                    }
                    listOfDateDict.append(dateDict)
        return listOfDateDict


file = open('test2.html', 'r')
data = file.read()
file.close()

if __name__ == "__main__":
    finder = openFinder()
    dateList = finder.findDates(data)
    for each in dateList:
        print(each['openings'] + ' Opening at ' + each['time'] + ' at ' + each['location'])



