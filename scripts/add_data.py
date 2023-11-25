#!/usr/bin/env python3

import json
import requests


def add_patient_to_db(dictionary):
    payload = json.dumps(dictionary, ensure_ascii=False)
    response = requests.post(
        "http://127.0.0.1:8000/api/v1/patient", headers={"Content-type": "application/json"}, data=payload)
    if response.status_code != 201:
        raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
    print(response.json())


add_patient_to_db({
    'first_name': 'John',
    'last_name': 'Doe',
    'weight': 100.5,
})
