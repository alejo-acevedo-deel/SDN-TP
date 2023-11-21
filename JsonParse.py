import json

class JsonParse:
    def __init__(self, json_file, json_data):
        self.json_data = json_data
        self.json_file = json_file

    def load_json(json_file):
        try:
            with open(json_file, 'r') as json_data:
                json_data = json.load(json_data)
                return JsonParse(json_file, json_data)
        except FileNotFoundError as e:
            print('No se encontro el archivo: ' + json_file)
            return None
        except json.decoder.JSONDecodeError as e:
            print('No se pudo decodificar el archivo: ' + json_file)
            return None

    def get_json_data(self):
        return self.json_data

