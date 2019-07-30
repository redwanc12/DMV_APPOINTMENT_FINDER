# DMV_DATE_FINDER
The DMV road test in hawaii takes on average 3 months to create an appointment. With this service, you can get notified, through text or email, when someone drops an appointment in a specified date range for the Hawaii DMV road test.

This project is now completed and live at roadtesthawaii.com

# How it works
This service uses a Web Driver to navigate the offical DMV ROAD TEST website. This is to bypass the bot checks and the fact that most functionalities on the website is in JavaScript. It scrapes each page within a given date range, and parses the Json returned to determine when and where the openings are. It then saves this information, and passes it to the REST API to be further handeled by the web app.

# Technologies used
Python3.6
Selenium Web Driver
Twilio
Requests Library

# Web
Note: No code for the Web app, nor the REST API, has been made public. This repository only contains the web scraping both that gathers the information.
