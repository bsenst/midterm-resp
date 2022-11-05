# Serving a model as described in mlbookcamp-code\chapter-05-deployment\test_service.py
# This script is for educational purpose only.

import requests
import json

patient = {
    'Age': 60,
    'Sex=female': 0, 
    'Sex=male': 1, 
    'Sex=not to say': 0,
    'Symptoms_encoded': 48,
}

url = 'http://172.17.0.2:9696/predict'
response = requests.post(url, json=patient)
result = response.json()

print(json.dumps(result, indent=2))

