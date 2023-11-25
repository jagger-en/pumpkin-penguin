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



def add_genders_to_db(items):
    for item in items:
        payload = json.dumps(item, ensure_ascii=False)
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/gender",
            headers={"Content-type": "application/json"},
            data=payload
        )
        if response.status_code != 201:
            raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
        print(response.json())

add_genders_to_db([
    {'id': 1, 'name': 'male'},
    {'id': 2, 'name': 'female'},
])


def add_patients_to_db(patients):
    for patient in patients:
        payload = json.dumps(patient, ensure_ascii=False)
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/patient",
            headers={"Content-type": "application/json"},
            data=payload
        )
        if response.status_code != 201:
            raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
        print(response.json())




cleaned_patients = [{'id': '1',
  'first_name': 'Jase',
  'last_name': 'Manion',
  'gender_id': '1',
  'email': 'jmanion0@ovh.net',
  'weight': '99',
  'height': '150',
  'date_of_birth': '1990-12-03'},
 {'id': '2',
  'first_name': 'Gilles',
  'last_name': 'McGregor',
  'gender_id': '1',
  'email': 'gmcgregor1@hao123.com',
  'weight': '94',
  'height': '158',
  'date_of_birth': '1952-12-12'},
 {'id': '3',
  'first_name': 'Sibeal',
  'last_name': 'Askam',
  'gender_id': '2',
  'email': 'saskam2@nytimes.com',
  'weight': '160',
  'height': '164',
  'date_of_birth': '1977-12-06'},
 {'id': '4',
  'first_name': 'Horace',
  'last_name': 'Utley',
  'gender_id': '1',
  'email': 'hutley3@cdbaby.com',
  'weight': '136',
  'height': '174',
  'date_of_birth': '1975-12-07'},
 {'id': '5',
  'first_name': 'Leonid',
  'last_name': 'Tatham',
  'gender_id': '1',
  'email': 'ltatham4@ucsd.edu',
  'weight': '74',
  'height': '124',
  'date_of_birth': '1977-12-06'},
 {'id': '6',
  'first_name': 'Nap',
  'last_name': 'Spafford',
  'gender_id': '1',
  'email': 'nspafford5@imgur.com',
  'weight': '185',
  'height': '176',
  'date_of_birth': '1946-12-14'},
 {'id': '7',
  'first_name': 'Dimitri',
  'last_name': 'Monaghan',
  'gender_id': '1',
  'email': 'dmonaghan6@imageshack.us',
  'weight': '83',
  'height': '176',
  'date_of_birth': '2002-11-30'},
 {'id': '8',
  'first_name': 'Zia',
  'last_name': 'Brightling',
  'gender_id': '2',
  'email': 'zbrightling7@miitbeian.gov.cn',
  'weight': '122',
  'height': '155',
  'date_of_birth': '1948-12-13'},
 {'id': '9',
  'first_name': 'Anjela',
  'last_name': 'Smaile',
  'gender_id': '2',
  'email': 'asmaile8@samsung.com',
  'weight': '150',
  'height': '107',
  'date_of_birth': '1986-12-04'},
 {'id': '10',
  'first_name': 'Esteban',
  'last_name': 'Angelo',
  'gender_id': '1',
  'email': 'eangelo9@google.co.jp',
  'weight': '76',
  'height': '122',
  'date_of_birth': '1960-12-10'},
 {'id': '11',
  'first_name': 'Briny',
  'last_name': 'Bole',
  'gender_id': '2',
  'email': 'bbolea@usgs.gov',
  'weight': '186',
  'height': '135',
  'date_of_birth': '1951-12-13'},
 {'id': '12',
  'first_name': 'Tye',
  'last_name': 'Tookill',
  'gender_id': '1',
  'email': 'ttookillb@slate.com',
  'weight': '161',
  'height': '153',
  'date_of_birth': '1985-12-04'},
 {'id': '13',
  'first_name': 'Malissia',
  'last_name': 'Soldi',
  'gender_id': '2',
  'email': 'msoldic@wufoo.com',
  'weight': '127',
  'height': '195',
  'date_of_birth': '1965-12-09'},
 {'id': '14',
  'first_name': 'Fan',
  'last_name': 'Ironside',
  'gender_id': '2',
  'email': 'fironsided@shinystat.com',
  'weight': '108',
  'height': '123',
  'date_of_birth': '1943-12-15'},
 {'id': '15',
  'first_name': 'Liv',
  'last_name': 'Skowcraft',
  'gender_id': '2',
  'email': 'lskowcrafte@webnode.com',
  'weight': '93',
  'height': '149',
  'date_of_birth': '1952-12-12'},
 {'id': '16',
  'first_name': 'Nisse',
  'last_name': 'Pashenkov',
  'gender_id': '2',
  'email': 'npashenkovf@prweb.com',
  'weight': '82',
  'height': '184',
  'date_of_birth': '1981-12-05'},
 {'id': '17',
  'first_name': 'Dorothea',
  'last_name': 'Stidston',
  'gender_id': '2',
  'email': 'dstidstong@google.com.hk',
  'weight': '60',
  'height': '124',
  'date_of_birth': '1944-12-14'},
 {'id': '18',
  'first_name': 'Mame',
  'last_name': 'Hawken',
  'gender_id': '2',
  'email': 'mhawkenh@yellowpages.com',
  'weight': '131',
  'height': '125',
  'date_of_birth': '1946-12-14'},
 {'id': '19',
  'first_name': 'Sanson',
  'last_name': 'Brine',
  'gender_id': '1',
  'email': 'sbrinei@macromedia.com',
  'weight': '104',
  'height': '163',
  'date_of_birth': '1958-12-11'},
 {'id': '20',
  'first_name': 'Kort',
  'last_name': 'Feldbau',
  'gender_id': '1',
  'email': 'kfeldbauj@arstechnica.com',
  'weight': '196',
  'height': '184',
  'date_of_birth': '1982-12-05'},
 {'id': '21',
  'first_name': 'Marian',
  'last_name': 'McCawley',
  'gender_id': '2',
  'email': 'mmccawleyk@themeforest.net',
  'weight': '165',
  'height': '151',
  'date_of_birth': '1948-12-13'},
 {'id': '22',
  'first_name': 'Corrie',
  'last_name': 'Ugoletti',
  'gender_id': '1',
  'email': 'cugolettil@washington.edu',
  'weight': '92',
  'height': '175',
  'date_of_birth': '1980-12-05'},
 {'id': '23',
  'first_name': 'Muhammad',
  'last_name': 'Redwing',
  'gender_id': '1',
  'email': 'mredwingm@typepad.com',
  'weight': '162',
  'height': '106',
  'date_of_birth': '1950-12-13'},
 {'id': '24',
  'first_name': 'Alford',
  'last_name': 'Doutch',
  'gender_id': '1',
  'email': 'adoutchn@apple.com',
  'weight': '55',
  'height': '107',
  'date_of_birth': '1985-12-04'},
 {'id': '25',
  'first_name': 'Kimberley',
  'last_name': 'Duffield',
  'gender_id': '2',
  'email': 'kduffieldo@discovery.com',
  'weight': '71',
  'height': '157',
  'date_of_birth': '1979-12-06'},
 {'id': '26',
  'first_name': 'Danie',
  'last_name': 'Sheekey',
  'gender_id': '1',
  'email': 'dsheekeyp@unblog.fr',
  'weight': '147',
  'height': '139',
  'date_of_birth': '1958-12-11'},
 {'id': '27',
  'first_name': 'Andrea',
  'last_name': 'Boocock',
  'gender_id': '2',
  'email': 'aboocockq@netlog.com',
  'weight': '36',
  'height': '155',
  'date_of_birth': '1952-12-12'},
 {'id': '28',
  'first_name': 'Russell',
  'last_name': 'Brunsen',
  'gender_id': '1',
  'email': 'rbrunsenr@army.mil',
  'weight': '113',
  'height': '123',
  'date_of_birth': '1974-12-07'},
 {'id': '29',
  'first_name': 'Reginald',
  'last_name': 'Scotchbourouge',
  'gender_id': '1',
  'email': 'rscotchbourouges@nytimes.com',
  'weight': '188',
  'height': '193',
  'date_of_birth': '1964-12-09'},
 {'id': '30',
  'first_name': 'Izaak',
  'last_name': 'Mudge',
  'gender_id': '1',
  'email': 'imudget@tinyurl.com',
  'weight': '104',
  'height': '114',
  'date_of_birth': '1954-12-12'},
 {'id': '31',
  'first_name': 'Clotilda',
  'last_name': 'Parmiter',
  'gender_id': '2',
  'email': 'cparmiteru@eventbrite.com',
  'weight': '67',
  'height': '122',
  'date_of_birth': '1998-12-01'},
 {'id': '32',
  'first_name': 'Karisa',
  'last_name': 'Fratczak',
  'gender_id': '2',
  'email': 'kfratczakv@comcast.net',
  'weight': '192',
  'height': '119',
  'date_of_birth': '1993-12-02'},
 {'id': '33',
  'first_name': 'Leonore',
  'last_name': 'Quarlis',
  'gender_id': '2',
  'email': 'lquarlisw@ucsd.edu',
  'weight': '69',
  'height': '163',
  'date_of_birth': '1953-12-12'},
 {'id': '34',
  'first_name': 'Domeniga',
  'last_name': 'Prazer',
  'gender_id': '2',
  'email': 'dprazerx@sitemeter.com',
  'weight': '189',
  'height': '108',
  'date_of_birth': '1957-12-11'},
 {'id': '35',
  'first_name': 'Gregoire',
  'last_name': 'Petyakov',
  'gender_id': '1',
  'email': 'gpetyakovy@rakuten.co.jp',
  'weight': '194',
  'height': '150',
  'date_of_birth': '2004-11-29'},
 {'id': '36',
  'first_name': 'Tarrah',
  'last_name': 'Beaman',
  'gender_id': '2',
  'email': 'tbeamanz@virginia.edu',
  'weight': '50',
  'height': '162',
  'date_of_birth': '1951-12-13'},
 {'id': '37',
  'first_name': 'Lyndsey',
  'last_name': 'Garvin',
  'gender_id': '2',
  'email': 'lgarvin10@xinhuanet.com',
  'weight': '143',
  'height': '151',
  'date_of_birth': '1986-12-04'},
 {'id': '38',
  'first_name': 'Carlene',
  'last_name': 'Gladwell',
  'gender_id': '2',
  'email': 'cgladwell11@nsw.gov.au',
  'weight': '121',
  'height': '190',
  'date_of_birth': '2001-11-30'},
 {'id': '39',
  'first_name': 'Zilvia',
  'last_name': 'Assinder',
  'gender_id': '2',
  'email': 'zassinder12@smugmug.com',
  'weight': '49',
  'height': '139',
  'date_of_birth': '1983-12-05'},
 {'id': '40',
  'first_name': 'Allys',
  'last_name': 'Belmont',
  'gender_id': '2',
  'email': 'abelmont13@nba.com',
  'weight': '164',
  'height': '147',
  'date_of_birth': '1975-12-07'},
 {'id': '41',
  'first_name': 'Fredrick',
  'last_name': 'Sleigh',
  'gender_id': '1',
  'email': 'fsleigh14@jalbum.net',
  'weight': '166',
  'height': '168',
  'date_of_birth': '1990-12-03'},
 {'id': '42',
  'first_name': 'Chas',
  'last_name': 'Breckon',
  'gender_id': '1',
  'email': 'cbreckon15@ucoz.com',
  'weight': '62',
  'height': '120',
  'date_of_birth': '1960-12-10'},
 {'id': '43',
  'first_name': 'Jaymee',
  'last_name': 'Mariotte',
  'gender_id': '2',
  'email': 'jmariotte16@utexas.edu',
  'weight': '86',
  'height': '183',
  'date_of_birth': '1996-12-01'},
 {'id': '44',
  'first_name': 'Bondie',
  'last_name': 'Corbett',
  'gender_id': '1',
  'email': 'bcorbett17@ning.com',
  'weight': '124',
  'height': '118',
  'date_of_birth': '2005-11-29'},
 {'id': '45',
  'first_name': 'Hiram',
  'last_name': 'Domleo',
  'gender_id': '1',
  'email': 'hdomleo18@woothemes.com',
  'weight': '170',
  'height': '100',
  'date_of_birth': '1985-12-04'},
 {'id': '46',
  'first_name': 'Sheppard',
  'last_name': 'Girling',
  'gender_id': '1',
  'email': 'sgirling19@alexa.com',
  'weight': '49',
  'height': '162',
  'date_of_birth': '1984-12-04'},
 {'id': '47',
  'first_name': 'Germayne',
  'last_name': 'Francis',
  'gender_id': '1',
  'email': 'gfrancis1a@blogs.com',
  'weight': '108',
  'height': '192',
  'date_of_birth': '2002-11-30'},
 {'id': '48',
  'first_name': 'Neron',
  'last_name': 'Broek',
  'gender_id': '1',
  'email': 'nbroek1b@com.com',
  'weight': '44',
  'height': '181',
  'date_of_birth': '1972-12-07'},
 {'id': '49',
  'first_name': 'Melody',
  'last_name': 'Idell',
  'gender_id': '2',
  'email': 'midell1c@sbwire.com',
  'weight': '84',
  'height': '150',
  'date_of_birth': '1982-12-05'},
 {'id': '50',
  'first_name': 'Reuven',
  'last_name': 'Manilow',
  'gender_id': '1',
  'email': 'rmanilow1d@apple.com',
  'weight': '87',
  'height': '191',
  'date_of_birth': '1984-12-04'},
 {'id': '51',
  'first_name': 'Norma',
  'last_name': 'Purches',
  'gender_id': '2',
  'email': 'npurches1e@cbc.ca',
  'weight': '146',
  'height': '130',
  'date_of_birth': '2005-11-29'},
 {'id': '52',
  'first_name': 'Yancy',
  'last_name': 'McCaghan',
  'gender_id': '1',
  'email': 'ymccaghan1f@4shared.com',
  'weight': '161',
  'height': '120',
  'date_of_birth': '1999-12-01'},
 {'id': '53',
  'first_name': 'Fanechka',
  'last_name': 'Kellog',
  'gender_id': '2',
  'email': 'fkellog1g@google.ru',
  'weight': '68',
  'height': '120',
  'date_of_birth': '1970-12-08'},
 {'id': '54',
  'first_name': 'Cobby',
  'last_name': 'Middle',
  'gender_id': '1',
  'email': 'cmiddle1h@webs.com',
  'weight': '86',
  'height': '182',
  'date_of_birth': '1955-12-12'},
 {'id': '55',
  'first_name': 'Wally',
  'last_name': 'Baglan',
  'gender_id': '2',
  'email': 'wbaglan1i@amazon.co.uk',
  'weight': '41',
  'height': '190',
  'date_of_birth': '1991-12-03'},
 {'id': '56',
  'first_name': 'Arron',
  'last_name': 'Harpin',
  'gender_id': '1',
  'email': 'aharpin1j@mysql.com',
  'weight': '140',
  'height': '166',
  'date_of_birth': '1992-12-02'},
 {'id': '57',
  'first_name': 'Noam',
  'last_name': 'Peer',
  'gender_id': '1',
  'email': 'npeer1k@pagesperso-orange.fr',
  'weight': '69',
  'height': '193',
  'date_of_birth': '1996-12-01'},
 {'id': '58',
  'first_name': 'Aviva',
  'last_name': 'Riccione',
  'gender_id': '2',
  'email': 'ariccione1l@nydailynews.com',
  'weight': '62',
  'height': '191',
  'date_of_birth': '1994-12-02'},
 {'id': '59',
  'first_name': 'Erhart',
  'last_name': 'Massen',
  'gender_id': '1',
  'email': 'emassen1m@howstuffworks.com',
  'weight': '101',
  'height': '100',
  'date_of_birth': '1978-12-06'},
 {'id': '60',
  'first_name': 'Angelika',
  'last_name': 'Atack',
  'gender_id': '2',
  'email': 'aatack1n@arstechnica.com',
  'weight': '80',
  'height': '107',
  'date_of_birth': '1966-12-09'},
 {'id': '61',
  'first_name': 'Donavon',
  'last_name': 'Pristnor',
  'gender_id': '1',
  'email': 'dpristnor1o@nymag.com',
  'weight': '75',
  'height': '171',
  'date_of_birth': '1958-12-11'},
 {'id': '62',
  'first_name': 'Gaylord',
  'last_name': 'Creber',
  'gender_id': '1',
  'email': 'gcreber1p@cbsnews.com',
  'weight': '56',
  'height': '145',
  'date_of_birth': '1967-12-09'},
 {'id': '63',
  'first_name': 'Cece',
  'last_name': 'Dickinson',
  'gender_id': '1',
  'email': 'cdickinson1q@instagram.com',
  'weight': '100',
  'height': '186',
  'date_of_birth': '1991-12-03'},
 {'id': '64',
  'first_name': 'Reynolds',
  'last_name': 'Pill',
  'gender_id': '1',
  'email': 'rpill1r@japanpost.jp',
  'weight': '152',
  'height': '173',
  'date_of_birth': '1968-12-08'},
 {'id': '65',
  'first_name': 'Patten',
  'last_name': 'Symson',
  'gender_id': '1',
  'email': 'psymson1s@prlog.org',
  'weight': '196',
  'height': '174',
  'date_of_birth': '1978-12-06'},
 {'id': '66',
  'first_name': 'Rafferty',
  'last_name': 'Langstone',
  'gender_id': '1',
  'email': 'rlangstone1t@utexas.edu',
  'weight': '44',
  'height': '125',
  'date_of_birth': '2002-11-30'},
 {'id': '67',
  'first_name': 'Tressa',
  'last_name': 'Malpas',
  'gender_id': '2',
  'email': 'tmalpas1u@a8.net',
  'weight': '112',
  'height': '172',
  'date_of_birth': '1965-12-09'},
 {'id': '68',
  'first_name': 'Doug',
  'last_name': 'Balma',
  'gender_id': '1',
  'email': 'dbalma1v@storify.com',
  'weight': '192',
  'height': '150',
  'date_of_birth': '1969-12-08'},
 {'id': '69',
  'first_name': 'Gwyn',
  'last_name': 'Butland',
  'gender_id': '2',
  'email': 'gbutland1w@whitehouse.gov',
  'weight': '120',
  'height': '126',
  'date_of_birth': '1998-12-01'},
 {'id': '70',
  'first_name': 'Carr',
  'last_name': 'Whiteway',
  'gender_id': '1',
  'email': 'cwhiteway1x@dion.ne.jp',
  'weight': '42',
  'height': '185',
  'date_of_birth': '1977-12-06'},
 {'id': '71',
  'first_name': 'Clarke',
  'last_name': 'Yousef',
  'gender_id': '1',
  'email': 'cyousef1y@is.gd',
  'weight': '104',
  'height': '195',
  'date_of_birth': '2001-11-30'},
 {'id': '72',
  'first_name': 'Reeba',
  'last_name': 'Tschierasche',
  'gender_id': '2',
  'email': 'rtschierasche1z@desdev.cn',
  'weight': '162',
  'height': '143',
  'date_of_birth': '1943-12-15'},
 {'id': '73',
  'first_name': 'Danice',
  'last_name': 'Lipman',
  'gender_id': '2',
  'email': 'dlipman20@wsj.com',
  'weight': '200',
  'height': '189',
  'date_of_birth': '1972-12-07'},
 {'id': '74',
  'first_name': 'Hortensia',
  'last_name': 'Lemmens',
  'gender_id': '2',
  'email': 'hlemmens21@narod.ru',
  'weight': '160',
  'height': '173',
  'date_of_birth': '1984-12-04'},
 {'id': '75',
  'first_name': 'Jannelle',
  'last_name': 'Di Giacomo',
  'gender_id': '2',
  'email': 'jdigiacomo22@seattletimes.com',
  'weight': '67',
  'height': '175',
  'date_of_birth': '1995-12-02'},
 {'id': '76',
  'first_name': 'Layton',
  'last_name': 'Gripton',
  'gender_id': '1',
  'email': 'lgripton23@booking.com',
  'weight': '95',
  'height': '181',
  'date_of_birth': '1949-12-13'},
 {'id': '77',
  'first_name': 'Catherin',
  'last_name': 'Candy',
  'gender_id': '2',
  'email': 'ccandy24@ibm.com',
  'weight': '82',
  'height': '155',
  'date_of_birth': '1968-12-08'},
 {'id': '78',
  'first_name': 'Wilbur',
  'last_name': 'Surmeir',
  'gender_id': '1',
  'email': 'wsurmeir25@epa.gov',
  'weight': '143',
  'height': '143',
  'date_of_birth': '2008-11-28'},
 {'id': '79',
  'first_name': 'Luigi',
  'last_name': 'Dyas',
  'gender_id': '1',
  'email': 'ldyas26@rakuten.co.jp',
  'weight': '40',
  'height': '126',
  'date_of_birth': '2001-11-30'},
 {'id': '80',
  'first_name': 'Kendrick',
  'last_name': 'Newton',
  'gender_id': '1',
  'email': 'knewton27@chicagotribune.com',
  'weight': '138',
  'height': '163',
  'date_of_birth': '1973-12-07'},
 {'id': '81',
  'first_name': 'Tadio',
  'last_name': 'Tedahl',
  'gender_id': '1',
  'email': 'ttedahl28@house.gov',
  'weight': '46',
  'height': '163',
  'date_of_birth': '1985-12-04'},
 {'id': '82',
  'first_name': 'Una',
  'last_name': 'Dewdeny',
  'gender_id': '2',
  'email': 'udewdeny29@moonfruit.com',
  'weight': '132',
  'height': '145',
  'date_of_birth': '1997-12-01'},
 {'id': '83',
  'first_name': 'Preston',
  'last_name': 'Barraclough',
  'gender_id': '1',
  'email': 'pbarraclough2a@amazon.de',
  'weight': '88',
  'height': '192',
  'date_of_birth': '1946-12-14'},
 {'id': '84',
  'first_name': 'Howard',
  'last_name': 'Van Halen',
  'gender_id': '1',
  'email': 'hvanhalen2b@cargocollective.com',
  'weight': '167',
  'height': '123',
  'date_of_birth': '2006-11-29'},
 {'id': '85',
  'first_name': 'Ase',
  'last_name': 'Brandone',
  'gender_id': '1',
  'email': 'abrandone2c@people.com.cn',
  'weight': '95',
  'height': '139',
  'date_of_birth': '1951-12-13'},
 {'id': '86',
  'first_name': 'Stillmann',
  'last_name': 'Pollak',
  'gender_id': '1',
  'email': 'spollak2d@ibm.com',
  'weight': '147',
  'height': '130',
  'date_of_birth': '1975-12-07'},
 {'id': '87',
  'first_name': 'Latrina',
  'last_name': 'Cardnell',
  'gender_id': '2',
  'email': 'lcardnell2e@cargocollective.com',
  'weight': '137',
  'height': '160',
  'date_of_birth': '1960-12-10'},
 {'id': '88',
  'first_name': 'Brooks',
  'last_name': 'Forbes',
  'gender_id': '1',
  'email': 'bforbes2f@friendfeed.com',
  'weight': '172',
  'height': '171',
  'date_of_birth': '1955-12-12'},
 {'id': '89',
  'first_name': 'Doralin',
  'last_name': 'Ruoss',
  'gender_id': '2',
  'email': 'druoss2g@independent.co.uk',
  'weight': '150',
  'height': '112',
  'date_of_birth': '1985-12-04'},
 {'id': '90',
  'first_name': 'Alonzo',
  'last_name': 'Povah',
  'gender_id': '1',
  'email': 'apovah2h@accuweather.com',
  'weight': '198',
  'height': '104',
  'date_of_birth': '1998-12-01'},
 {'id': '91',
  'first_name': 'Garrett',
  'last_name': 'Medcalfe',
  'gender_id': '1',
  'email': 'gmedcalfe2i@paypal.com',
  'weight': '108',
  'height': '172',
  'date_of_birth': '1949-12-13'},
 {'id': '92',
  'first_name': 'Stephan',
  'last_name': 'Mackneis',
  'gender_id': '1',
  'email': 'smackneis2j@rediff.com',
  'weight': '118',
  'height': '158',
  'date_of_birth': '1982-12-05'},
 {'id': '93',
  'first_name': 'Alair',
  'last_name': 'Drayton',
  'gender_id': '1',
  'email': 'adrayton2k@google.ru',
  'weight': '198',
  'height': '170',
  'date_of_birth': '1960-12-10'},
 {'id': '94',
  'first_name': 'Hercules',
  'last_name': 'Ruggs',
  'gender_id': '1',
  'email': 'hruggs2l@wordpress.com',
  'weight': '35',
  'height': '110',
  'date_of_birth': '2002-11-30'},
 {'id': '95',
  'first_name': 'Dalia',
  'last_name': 'McSporrin',
  'gender_id': '2',
  'email': 'dmcsporrin2m@miitbeian.gov.cn',
  'weight': '162',
  'height': '100',
  'date_of_birth': '1960-12-10'},
 {'id': '96',
  'first_name': 'Thaine',
  'last_name': 'Horburgh',
  'gender_id': '1',
  'email': 'thorburgh2n@admin.ch',
  'weight': '62',
  'height': '130',
  'date_of_birth': '1971-12-08'},
 {'id': '97',
  'first_name': 'Benjamin',
  'last_name': 'Twyford',
  'gender_id': '1',
  'email': 'btwyford2o@usgs.gov',
  'weight': '147',
  'height': '101',
  'date_of_birth': '1957-12-11'},
 {'id': '98',
  'first_name': 'Tymon',
  'last_name': 'Whight',
  'gender_id': '1',
  'email': 'twhight2p@over-blog.com',
  'weight': '66',
  'height': '151',
  'date_of_birth': '1962-12-10'},
 {'id': '99',
  'first_name': 'Joachim',
  'last_name': 'Kunc',
  'gender_id': '1',
  'email': 'jkunc2q@comsenz.com',
  'weight': '136',
  'height': '114',
  'date_of_birth': '1993-12-02'},
 {'id': '100',
  'first_name': 'Lothario',
  'last_name': "O'Dare",
  'gender_id': '1',
  'email': 'lodare2r@clickbank.net',
  'weight': '81',
  'height': '172',
  'date_of_birth': '1961-12-10'}]


add_patients_to_db(cleaned_patients)










