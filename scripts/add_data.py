#!/usr/bin/env python3

import json
import requests

def add_machines_to_db(machines):
    for machine in machines:
        payload = json.dumps(machine, ensure_ascii=False)
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/machine",
            headers={"Content-type": "application/json"},
            data=payload
        )
        if response.status_code != 201:
            raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
        print(response.json())

machines_to_add = [
    {'machine_name': 'TrueBeam', 'id': 'TB1'},
    {'machine_name': 'TrueBeam', 'id': 'TB2'},
    {'machine_name': 'VitalBeam', 'id': 'VB1'},
    {'machine_name': 'VitalBeam', 'id': 'VB2'},
    {'machine_name': 'U', 'id': 'U1'},
]

add_machines_to_db(machines_to_add)

def add_regions_to_db(regions):
    for region in regions:
        payload = json.dumps(region, ensure_ascii=False)
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/region",
            headers={"Content-type": "application/json"}, data=payload)
        if response.status_code != 201:
            raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
        print(response.json())

regions_to_add = [
    {'name': 'Craniospinal', 'id': '1', 'avg_frac': '30'},
    {'name': 'Breast', 'id': '2', 'avg_frac': '12'},
    {'name': 'Breast special', 'id': '3', 'avg_frac': '20'},
    {'name': 'Head & neck', 'id': '4', 'avg_frac': '12'},
    {'name': 'Abdomen', 'id': '5', 'avg_frac': '12'},
    {'name': 'Pelvis', 'id': '6', 'avg_frac': '12'},
    {'name': 'Crane', 'id': '7', 'avg_frac': '10'},
    {'name': 'Lung', 'id': '8', 'avg_frac': '12'},
    {'name': 'Lung special', 'id': '9', 'avg_frac': '15'},
    {'name': 'Whole Brain', 'id': '10', 'avg_frac': '10'},
]

add_regions_to_db(regions_to_add)

def add_machine_and_region_to_db(machine_and_region_list):
    for mr in machine_and_region_list:
        payload = json.dumps(mr, ensure_ascii=False)
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/machineandregion",
            headers={"Content-type": "application/json"},
            data=payload
        )
        if response.status_code != 201:
            raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
        print(response.json())

machine_and_region = [{'region_id': '1', 'machine_id': 'TB1', 'id': '1'},
 {'region_id': '1', 'machine_id': 'TB2', 'id': '2'},
 {'region_id': '2', 'machine_id': 'TB1', 'id': '3'},
 {'region_id': '2', 'machine_id': 'TB2', 'id': '4'},
 {'region_id': '2', 'machine_id': 'VB1', 'id': '5'},
 {'region_id': '2', 'machine_id': 'VB2', 'id': '6'},
 {'region_id': '2', 'machine_id': 'U', 'id': '7'},
 {'region_id': '3', 'machine_id': 'TB1', 'id': '8'},
 {'region_id': '3', 'machine_id': 'TB2', 'id': '9'},
 {'region_id': '4', 'machine_id': 'TB1', 'id': '10'},
 {'region_id': '4', 'machine_id': 'TB2', 'id': '11'},
 {'region_id': '4', 'machine_id': 'VB1', 'id': '12'},
 {'region_id': '4', 'machine_id': 'VB2', 'id': '13'},
 {'region_id': '5', 'machine_id': 'TB1', 'id': '14'},
 {'region_id': '5', 'machine_id': 'TB2', 'id': '15'},
 {'region_id': '5', 'machine_id': 'VB1', 'id': '16'},
 {'region_id': '5', 'machine_id': 'VB2', 'id': '17'},
 {'region_id': '6', 'machine_id': 'TB1', 'id': '18'},
 {'region_id': '6', 'machine_id': 'TB2', 'id': '19'},
 {'region_id': '6', 'machine_id': 'VB1', 'id': '20'},
 {'region_id': '6', 'machine_id': 'VB2', 'id': '21'},
 {'region_id': '7', 'machine_id': 'TB1', 'id': '22'},
 {'region_id': '7', 'machine_id': 'TB2', 'id': '23'},
 {'region_id': '7', 'machine_id': 'VB1', 'id': '24'},
 {'region_id': '7', 'machine_id': 'VB2', 'id': '25'},
 {'region_id': '8', 'machine_id': 'TB1', 'id': '26'},
 {'region_id': '8', 'machine_id': 'TB2', 'id': '27'},
 {'region_id': '8', 'machine_id': 'VB1', 'id': '28'},
 {'region_id': '8', 'machine_id': 'VB2', 'id': '29'},
 {'region_id': '9', 'machine_id': 'TB1', 'id': '30'},
 {'region_id': '9', 'machine_id': 'TB2', 'id': '31'},
 {'region_id': '9', 'machine_id': 'VB1', 'id': '32'},
 {'region_id': '9', 'machine_id': 'VB2', 'id': '33'},
 {'region_id': '5', 'machine_id': 'VB1', 'id': '34'},
 {'region_id': '5', 'machine_id': 'VB2', 'id': '35'},
 {'region_id': '5', 'machine_id': 'U', 'id': '36'}]

add_machine_and_region_to_db(machine_and_region)
