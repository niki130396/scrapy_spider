

json_schema = {'birth_date', 'birth_place', 'profession', 'languages', 'political_party', 'email_address'}

class JsonValidator:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, json):
        pass