import json


class GetJson:
    def get_json(self, file):
        with open(f"E:\\python_projects\\AlbionOnlineTraderBot\\Jsons\\{file}.json", 'r', encoding='utf-8') as data:
            json_data = json.load(data)
        return json_data

    def get_levels(self):
        return self.get_json('levels')

    def get_resources(self):
        return self.get_json('resources')


get_json = GetJson()
