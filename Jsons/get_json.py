import json
from main_shared_variables import path_to_json


class GetJson:
    def get_json(self, file):
        with open(f"{path_to_json}{file}.json", 'r', encoding='utf-8') as data:
            json_data = json.load(data)
        return json_data

    def get_levels(self):
        return self.get_json('levels')

    def get_resources(self):
        return self.get_json('resources')


get_json = GetJson()
