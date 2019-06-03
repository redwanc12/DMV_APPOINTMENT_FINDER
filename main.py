"""main class"""
import time
from check_avail import openFinder
from token_finder import tokenFinder
from models import User, Spots
from notif_sender import notif


#testing
sender = notif()
tf = tokenFinder()
parser = openFinder()
starttime = time.time()
tf.authenticateClient()

testUser = User('redwanc12@gmail.com', '')
next_spots = parser.findDates(tf.nextDayWithOpens())

while(True):
    for each in next_spots:
        spot = Spots(
            each['openings'],
            each['time'],
            each['location'],
            each['day']
        )
        if not spot in testUser.excludeList:
            sender.sendEmail(testUser.email, 'open', each['location']) 
            testUser.append_spot(spot)
    
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))


"""
while(True):
    r = requests.get('http://127.0.0.1:8000/polls/open')
    soup = BeautifulSoup(r.text, 'html.parser')
    emails = soup.find_all('h1')
    days = soup.find_all('p')
    emailList = []

    for each in range(len(emails)):
        emailList.append({
            'day': days[each].text,
            'email': emails[each].text
        })

    tf.refresh()
    for each in emailList:
        data = tf.scrapeDate(each['day'])
        dates = parser.findDates(data)
        if(dates != []):
            sender.sendEmail(each['email'], 'Open date', sender.dateToBody(dates))

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

tf.closeDriver()
"""
