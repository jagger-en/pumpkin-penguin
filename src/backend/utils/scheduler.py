#!/usr/bin/env python3

import datetime


def create_non_office_interval(given_date_time):
    year = given_date_time.year
    month = given_date_time.month
    day = given_date_time.day

    today = datetime.datetime(year, month, day)
    today = today.replace(hour=7, minute=0)
    yesterday = datetime.datetime(year, month, day) - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=16, minute=0)

    return (yesterday, today)

def create_days_list(start_time, end_time, tdelta):
    point_in_time = datetime.datetime(start_time.year, start_time.month, start_time.day)
    days_list = []
    days_list.append(point_in_time)
    while point_in_time < end_time:
        point_in_time = point_in_time + tdelta
        days_list.append(point_in_time)
    return days_list

def create_slots_list(start_time, end_time, slot_size):
    point_in_time = datetime.datetime(start_time.year, start_time.month, start_time.day)
    days_list = []
    while point_in_time < end_time:
        st_time = point_in_time
        point_in_time = point_in_time + slot_size
        days_list.append((st_time, point_in_time))
    return days_list

def create_non_office_intervals(start_time, end_time):
    intervals = []
    for date_time in create_days_list(start_time, end_time, datetime.timedelta(days=1)):
        intervals.append(create_non_office_interval(date_time))
    return intervals



def check_if_slot_is_available(slot, start_time, end_time, existing_slots):
    intervals = create_non_office_intervals(start_time, end_time)
    intervals.extend(existing_slots)

    for st, en in intervals:
        slot_st, slot_en = slot

        # HERE IT IS
        if slot_st >= st and slot_en <= en:
            return False
        # if slot_st >= st and slot_en >= en:
        #     return False
    return True


def get_available_slots(start_time, end_time, existing_slots, slot_size):
    available_slots = []
    for slot in create_slots_list(start_time, end_time, slot_size):
        status = check_if_slot_is_available(slot, start_time, end_time, existing_slots)
        if status:
            available_slots.append(slot)
    return available_slots



import pprint
start_time = datetime.datetime(2023, 11, 25, 13, 38)
end_time = datetime.datetime(2023, 11, 26, 17, 34)


existing_slots = [
    (datetime.datetime(2023, 11, 25, 7, 0), datetime.datetime(2023, 11, 25, 7, 50))
]

pprint.pprint(get_available_slots(start_time, end_time, existing_slots, datetime.timedelta(minutes=15)))
