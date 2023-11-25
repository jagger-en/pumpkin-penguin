def add_appointment_to_db(appointment_list):
    payload = json.dumps(appointment_list, ensure_ascii=False)
    response = requests.post(
        "http://127.0.0.1:8000/api/v1/appointment",  
        headers={"Content-type": "application/json"},
        data=payload
    )
    if response.status_code != 201:
        raise Exception('Failed to send request: [%s] %s' % (response.status_code, response.json()))
    print(response.json())
  
appointment_data = [{'id': '66',
  'machine': 'TB2',
  'patient': '63',
  'priority': 'A',
  'start_time': '2023-12-07 09:37:31',
  'end_time': '2023-12-07 09:49:31'},
 {'id': '65',
  'machine': 'U',
  'patient': '18',
  'priority': 'B',
  'start_time': '2023-12-12 10:57:02',
  'end_time': '2023-12-12 11:14:02'},
 {'id': '80',
  'machine': 'U',
  'patient': '33',
  'priority': 'B',
  'start_time': '2023-12-03 13:31:51',
  'end_time': '2023-12-03 13:50:51'},
 {'id': '71',
  'machine': 'VB2',
  'patient': '62',
  'priority': 'A',
  'start_time': '2023-12-14 10:31:28',
  'end_time': '2023-12-14 10:53:28'},
 {'id': '8',
  'machine': 'VB2',
  'patient': '71',
  'priority': 'A',
  'start_time': '2023-12-08 15:59:53',
  'end_time': '2023-12-08 16:21:53'},
 {'id': '86',
  'machine': 'TB2',
  'patient': '81',
  'priority': 'A',
  'start_time': '2023-12-20 12:22:17',
  'end_time': '2023-12-20 12:43:17'},
 {'id': '31',
  'machine': 'VB2',
  'patient': '19',
  'priority': 'A',
  'start_time': '2023-11-30 10:06:57',
  'end_time': '2023-11-30 10:34:57'},
 {'id': '66',
  'machine': 'TB1',
  'patient': '63',
  'priority': 'B',
  'start_time': '2023-11-27 13:19:21',
  'end_time': '2023-11-27 13:42:21'},
 {'id': '91',
  'machine': 'VB2',
  'patient': '16',
  'priority': 'B',
  'start_time': '2023-11-28 10:50:58',
  'end_time': '2023-11-28 11:03:58'},
 {'id': '70',
  'machine': 'U',
  'patient': '27',
  'priority': 'B',
  'start_time': '2023-12-11 10:34:27',
  'end_time': '2023-12-11 10:45:27'},
 {'id': '25',
  'machine': 'VB1',
  'patient': '24',
  'priority': 'A',
  'start_time': '2023-12-12 15:39:37',
  'end_time': '2023-12-12 16:09:37'},
 {'id': '87',
  'machine': 'TB1',
  'patient': '97',
  'priority': 'B',
  'start_time': '2023-12-02 13:33:25',
  'end_time': '2023-12-02 13:51:25'},
 {'id': '5',
  'machine': 'TB1',
  'patient': '11',
  'priority': 'B',
  'start_time': '2023-11-28 15:30:19',
  'end_time': '2023-11-28 15:32:19'},
 {'id': '58',
  'machine': 'VB2',
  'patient': '64',
  'priority': 'B',
  'start_time': '2023-12-23 16:29:28',
  'end_time': '2023-12-23 16:39:28'},
 {'id': '11',
  'machine': 'U',
  'patient': '42',
  'priority': 'B',
  'start_time': '2023-12-22 14:39:24',
  'end_time': '2023-12-22 15:08:24'},
 {'id': '81',
  'machine': 'VB2',
  'patient': '43',
  'priority': 'A',
  'start_time': '2023-12-13 09:11:30',
  'end_time': '2023-12-13 09:39:30'},
 {'id': '29',
  'machine': 'VB1',
  'patient': '48',
  'priority': 'A',
  'start_time': '2023-12-16 11:35:00',
  'end_time': '2023-12-16 11:54:00'},
 {'id': '74',
  'machine': 'TB1',
  'patient': '16',
  'priority': 'B',
  'start_time': '2023-12-14 12:06:59',
  'end_time': '2023-12-14 12:11:59'},
 {'id': '3',
  'machine': 'TB2',
  'patient': '25',
  'priority': 'A',
  'start_time': '2023-12-24 12:07:47',
  'end_time': '2023-12-24 12:31:47'},
 {'id': '3',
  'machine': 'TB1',
  'patient': '70',
  'priority': 'A',
  'start_time': '2023-12-19 14:22:40',
  'end_time': '2023-12-19 14:40:40'},
 {'id': '34',
  'machine': 'VB1',
  'patient': '9',
  'priority': 'A',
  'start_time': '2023-12-07 10:52:03',
  'end_time': '2023-12-07 11:07:03'},
 {'id': '26',
  'machine': 'TB1',
  'patient': '34',
  'priority': 'A',
  'start_time': '2023-11-28 08:24:05',
  'end_time': '2023-11-28 08:35:05'},
 {'id': '99',
  'machine': 'TB2',
  'patient': '8',
  'priority': 'A',
  'start_time': '2023-11-30 15:18:40',
  'end_time': '2023-11-30 15:41:40'},
 {'id': '85',
  'machine': 'TB1',
  'patient': '33',
  'priority': 'B',
  'start_time': '2023-12-14 14:01:00',
  'end_time': '2023-12-14 14:23:00'},
 {'id': '82',
  'machine': 'VB1',
  'patient': '80',
  'priority': 'A',
  'start_time': '2023-12-15 14:27:23',
  'end_time': '2023-12-15 14:28:23'},
 {'id': '90',
  'machine': 'VB1',
  'patient': '43',
  'priority': 'B',
  'start_time': '2023-11-27 15:00:08',
  'end_time': '2023-11-27 15:24:08'},
 {'id': '5',
  'machine': 'VB2',
  'patient': '52',
  'priority': 'A',
  'start_time': '2023-12-15 12:19:22',
  'end_time': '2023-12-15 12:37:22'},
 {'id': '99',
  'machine': 'TB1',
  'patient': '85',
  'priority': 'B',
  'start_time': '2023-12-21 13:58:27',
  'end_time': '2023-12-21 14:18:27'},
 {'id': '58',
  'machine': 'VB1',
  'patient': '68',
  'priority': 'B',
  'start_time': '2023-11-26 10:48:25',
  'end_time': '2023-11-26 11:12:25'},
 {'id': '5',
  'machine': 'VB2',
  'patient': '64',
  'priority': 'A',
  'start_time': '2023-12-13 08:42:30',
  'end_time': '2023-12-13 08:59:30'},
 {'id': '97',
  'machine': 'VB2',
  'patient': '1',
  'priority': 'B',
  'start_time': '2023-11-25 08:28:27',
  'end_time': '2023-11-25 08:47:27'},
 {'id': '24',
  'machine': 'VB1',
  'patient': '13',
  'priority': 'B',
  'start_time': '2023-12-04 11:36:49',
  'end_time': '2023-12-04 11:52:49'},
 {'id': '81',
  'machine': 'TB2',
  'patient': '11',
  'priority': 'B',
  'start_time': '2023-12-09 11:40:25',
  'end_time': '2023-12-09 11:43:25'},
 {'id': '15',
  'machine': 'TB1',
  'patient': '33',
  'priority': 'A',
  'start_time': '2023-11-25 13:51:30',
  'end_time': '2023-11-25 14:15:30'}]

add_appointment_to_db(appointment_data)
