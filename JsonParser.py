import json

class JsonParser:
    def __init__(self, json_file, json_data):
        self.json_data = json_data
        self.json_file = json_file
        
    @classmethod
    def load_json(self, json_file):
        try:
            with open(json_file, 'r') as json_data:
                json_data = json.load(json_data)
                return JsonParser(json_file, json_data)
        except FileNotFoundError as e:
            print('No se encontro el archivo: ' + json_file)
            return None
        except json.decoder.JSONDecodeError as e:
            print('No se pudo parsear el archivo: ' + json_file)
            print(e)
            return None

    def get_json_data(self):
        return self.json_data
    
    def parse_rule(self, rule):
        if not 'protocol' in rule or rule['protocol'] != 'TCP' or rule['protocol'] != 'UDP':
            return [
                {
                'nw_proto': 6,
                'nw_src' : rule['srcIp'] if 'srcIp' in rule else None,
                'nw_dst' : rule['destIp'] if 'destIp' in rule else None,
                'tp_src': rule['srcPort'] if 'srcPort' in rule else None,
                'tp_dst' : rule['destPort'] if 'destPort' in rule else None
                },
                {
                'nw_proto': 17,
                'nw_src' : rule['srcIp'] if 'srcIp' in rule else None,
                'nw_dst' : rule['destIp'] if 'destIp' in rule else None,
                'tp_src': rule['srcPort'] if 'srcPort' in rule else None,
                'tp_dst' : rule['destPort'] if 'destPort' in rule else None
                },
            ]
        elif rule['protocol'] == 'TCP' or rule['protocol'] == 'UDP':
            protocol_number = 6 if rule['protocol'] == 'TCP' else 17
            return [
                    {
                        'nw_proto': protocol_number,
                        'nw_src' : rule['srcIp'] if 'srcIp' in rule else None,
                        'nw_dst' : rule['destIp'] if 'destIp' in rule else None,
                        'tp_src': rule['srcPort'] if 'srcPort' in rule else None,
                        'tp_dst' : rule['destPort'] if 'destPort' in rule else None
                    }
                ]
        else:
            raise Exception('Regla invalida: ', rule)
    
    def get_rules(self):
        rules = []
        for rule in self.json_data['rules']:
            parsed_rules = self.parse_rule(rule)
            for parsed_rule in parsed_rules:
                rules.append(parsed_rule)
        return rules



