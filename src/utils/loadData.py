import json
def load_data(fileName):
    with open(fileName, 'r') as f:
        return json.load(f)