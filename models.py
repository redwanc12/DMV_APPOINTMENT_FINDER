"""Models to communciate my website to my rest API"""

class Spots:
    """Spot model"""
    def __init__(self, openings, time, location, day):
        self.openings = openings
        self.time = time
        self.location = location
        self.day = day

    def __str__(self):
        pass


class User:
    """User model"""
    def __init__(self, email, number, excludeList=[]):
        self.email = email
        self.number = number
        self.excludeList = excludeList

    def append_spot(self, spot):
        self.excludeList.append(spot)
