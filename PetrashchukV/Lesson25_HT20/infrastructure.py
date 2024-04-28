import requests
import json


class Phone:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.headers = {'content-type':'application/json'}
        self.default_phone_data = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
        self.updated_data = {
    "name": "Apple MacBook Pro 17",
    "data": {
        "year": 2021,
        "price": 2055.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}
        self.created_phone_id = None

    def get_list_of_all_objets(self):
        return requests.get(self.base_url)

    def get_single_phone(self, device_id):
        return requests.get(f'{self.base_url}/{device_id}')

    def update_phone_new(self, device_id):
        return requests.put(f'{self.base_url}/{device_id}', headers=self.headers, data=json.dumps(self.updated_data))

    def create_single_default_object(self):
        response = requests.post(self.base_url, headers=self.headers, data=json.dumps(self.default_phone_data))
        if response.status_code == 200:
            self.created_phone_id = response.json().get('id')
        return response

    def update_phone_with_created_id(self):
        if not self.created_phone_id:
            print("Error: Phone ID is not available.")
            return None
        response = requests.put(f'{self.base_url}/{self.created_phone_id}', headers=self.headers, data=json.dumps(self.updated_data))
        return response


    def partial_update_phone(self, device_id):
        return requests.patch(f'{self.base_url}/{device_id}', headers=self.headers, data=json.dumps(self.updated_data))


    def delete_phone(self, device_id):
        return requests.delete(f'{self.base_url}/{device_id}')
