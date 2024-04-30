import requests
from PetrashchukV.Lesson28_HT22.create_new_table import CustomObject
from PetrashchukV.Lesson28_HT22.connection import SqlDatabase

class ApiSqlAdapter:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint
        self.db = SqlDatabase()

    def _get_from_api(self, endpoint):
        response = requests.get(endpoint)
        return response.json()

    def _post_to_api(self, endpoint, data):
        response = requests.post(endpoint, json=data)
        return response.json()

    def _put_to_api(self, endpoint, data):
        response = requests.put(endpoint, json=data)
        return response.json()

    def _insert_into_db(self, obj):
        self.db.add_object(obj)

    def _update_db(self, obj):
        self.db.add_object(obj)

    def get_object(self, obj_id):
        api_data = self._get_from_api(f"{self.api_endpoint}/{obj_id}")
        return api_data

    def post_object(self, data):
        api_response = self._post_to_api(self.api_endpoint, data)
        obj = CustomObject(**data)
        self._insert_into_db(obj)
        return obj.id

    def put_object(self, obj_id, data):
        api_response = self._put_to_api(f"{self.api_endpoint}/{obj_id}", data)
        obj = self.db.get_object_by_id(obj_id)
        for key, value in data.items():
            setattr(obj, key, value)
        self._update_db(obj)
        return obj

    def close_connection(self):
        self.db.close_connection()
