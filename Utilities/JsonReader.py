import json


class JsonReader:

    @staticmethod
    def read_json(file_path, key):

        with open(file_path, "r") as file:
            data = json.load(file)

        return data[key]