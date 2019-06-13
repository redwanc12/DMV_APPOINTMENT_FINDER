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
    
    def append_exclude_list(self, user_id, spot_id):
        response = requests.get(f'{self.url}api/dmv/customers/{user_id}/', headers=self.header)
        current_spots = response.json()['excludeSpotList']
        spot_list = []
        spot_list.append(current_spots)
        spot_list.append(spot_id)

        requests.patch(
            f'{self.url}api/dmv/customers/{user_id}/',
            {"excludeSpotList":spot_list},
            headers=self.header)
    
    def clear_exclude_list(self, user_id):
        requests.patch(
            f'{self.url}api/dmv/customers/{user_id}/',
            {"excludeSpotList":[]}, # this does not work.
            headers=self.header)
