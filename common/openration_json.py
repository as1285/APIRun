import json

class OperationJson:
    def __init__(self):
        pass
    def get_data(self):
        with open('') as f:
            data = json.load(f)
            return data
