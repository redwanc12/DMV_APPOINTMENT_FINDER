"""class to handle requests to the API"""
import requests


class API:
    """class to handle requests to the API"""
    def __init__(self, url, header):
        self.url = url
        self.header = header

    def delete_all(self, model):
        response = requests.get(
            f'{self.url}api/dmv/{model}/',
            headers=self.header
        )
        for each in response.json():
            requests.delete(
                url=f'{self.url}api/dmv/{model}/{each["id"]}',
                headers=self.header
            )
    
    def add_spot_list(self, data):
        requests.post(
            url=f'{self.url}api/dmv/spots/',
            data=data,
            headers=self.header
        )
    