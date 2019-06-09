"""Models to communciate my website to my rest API"""

class Spots:
    """Spot model"""
    def __init__(self, time, location, day):
        self.time = time
        self.location = location
        self.day = day

    def __str__(self):
        return f'opening on {self.day} at {self.time} in {self.location}'


class User:
    """User model"""
    def __init__(self, email, phone, excludeSpotList=[]):
        self.email = email
        self.phone = phone
        self.excludeSpotList = excludeSpotList

    def append_spot(self, spot):
        self.excludeSpotList.append(spot)

    def __str__(self):
        return f'email: {self.email} phone: {self.phone} excludeSpotList: {self.excludeSpotList}'

    def number(self):
        return self.phone
