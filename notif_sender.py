import smtplib
from check_avail import openFinder
from token_finder import tokenFinder
import time

emailList = [
    {
        'day':'July 01',
        'email':'redwanc12@gmail.com'
    },
    {
        'day':'August 02',
        'email':'mchowd13@asu.edu'
    }
]

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


sender = notif()
tf = tokenFinder()
parser = openFinder()
starttime = time.time()

tf.authenticateClient()
while(True):
    tf.refresh()
    for each in emailList:
        data = tf.scrapeDate(each['day'])
        dates = parser.findDates(data)
        if(dates != []):
            sender.sendEmail(each['email'], 'Open date', sender.dateToBody(dates))

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

tf.closeDriver()
