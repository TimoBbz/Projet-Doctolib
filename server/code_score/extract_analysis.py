import json

def extract_analysis(jsonfile):
    with open(jsonfile) as f:
        return json.load(f)

