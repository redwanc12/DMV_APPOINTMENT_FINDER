from bs4 import BeautifulSoup

locationList = ['Kapalama', 'Kapolei', 'Koolau', 'Wahiawa', 'Waianae']

file = open('test2.html', 'r')
data = file.read()
file.close()

soup = BeautifulSoup(data, 'html.parser')
times = soup.find_all('tr', {'class':['TableItemLine','TableAltItemLine']})

for each in times:
    time = each.td.text
    spots = each.find_all(['input', 'span'])
    for index, spot in enumerate(spots):
        if('None' != spot.text):
            print('Opening at ' + time + ' at ' + locationList[index])

