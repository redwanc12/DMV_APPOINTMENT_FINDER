import smtplib
from check_avail import openFinder
from token_finder import tokenFinder
from models import User, Spots
import time

import requests
from bs4 import BeautifulSoup

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



class notif(object):
    def __init__(self):
        self.email = 'dmvnotificationhi@gmail.com'
        self.password = 'DMVpass123!'
    
    def logIn(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(self.email, self.password)

    def sendEmail(self, email, subject, body):
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                msg = f'Subject: {subject}\n\n{body}'
                smtp.login(self.email, self.password)
                smtp.sendmail(self.email, email, msg)

    def dateToBody(self, dates):
        body = ''
        for each in dates:
            body += (each['openings'] + ' Opening at ' + each['time'] + ' at ' + each['location'] + ' on ' + each['day'] + '\n')
        return body


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
            sender.sendEmail(testUser.email, 'open', each['location']) # make this mmethod in spots model
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
