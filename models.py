"""Models to communciate my website to my rest API"""

class ExcludeList:
    """List object to handle dates to exclude"""
    def __init__(self):
        self.list = []

class User:
    """User model"""
    def __init__(self, email, number, excludeList):
        self.email = email
        self.number = number
        self.exclude = excludeList

class MonthList:
    """Class to get a list of the DMV days in the following month"""
    def __init__(self):
        self.list = []
    
    def fillMonth(self)




