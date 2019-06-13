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
    
headers = {'Authorization':'token 3ab74d348c070ece89b88ea3728f9ed8b22e44b8 '}
api_test = API('http://127.0.0.1:8000/', headers)


api_test.append_exclude_list(8, 23)