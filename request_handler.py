"""class to handle requests to the API"""
import json
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

    def get_users_list(self):
        return json.loads(requests.get(
            url=f'{self.url}api/dmv/customers/',
            headers=self.header
        ).text)
    
    def append_exclude_list(self, user_id, spot_text):
        response = requests.get(f'{self.url}api/dmv/customers/{user_id}/', headers=self.header)
        current_spots = response.json()['excludeSpotList']

        requests.patch(
            f'{self.url}api/dmv/customers/{user_id}/',
            {"excludeSpotList":current_spots + spot_text},
            headers=self.header)
    
    def clear_exclude_list(self, user_id):
        requests.patch(
            f'{self.url}api/dmv/customers/{user_id}/',
            {"excludeSpotList":''},
            headers=self.header)
        
    def delete_from_exclude_list(self, user_id, spot_text):
        response = requests.get(f'{self.url}api/dmv/customers/{user_id}/', headers=self.header)
        current_spots = response.json()['excludeSpotList']
        if spot_text in current_spots:
            current_spots = current_spots.replace(spot_text, '')

        requests.patch(
            f'{self.url}api/dmv/customers/{user_id}/',
            {"excludeSpotList":current_spots},
            headers=self.header)
