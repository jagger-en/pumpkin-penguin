#!/usr/bin/env python3
import datetime


def create_non_office_intervals(start_time, end_time):
    intervals = []
    for date_time in create_days_list(start_time, end_time, datetime.timedelta(days=1)):
        intervals.append(create_non_office_interval(date_time))
    return intervals


def create_non_office_interval(given_date_time):
    year = given_date_time.year
    month = given_date_time.month
    day = given_date_time.day

    today = datetime.datetime(year, month, day)
    today = today.replace(hour=7, minute=0)
    yesterday = datetime.datetime(
        year, month, day) - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=16, minute=0)

    return (yesterday, today)


def create_days_list(start_time, end_time, tdelta):
    point_in_time = datetime.datetime(
        start_time.year, start_time.month, start_time.day)
    days_list = []
    days_list.append(point_in_time)
    while point_in_time < end_time:
        point_in_time = point_in_time + tdelta
        days_list.append(point_in_time)
    return days_list


def get_available_slots(start_time, end_time, intervals, slot_size):
    available_slots = []
    for slot in create_slots_list(start_time, end_time, slot_size):
        status = check_if_slot_is_available(slot, intervals)
        if status:
            available_slots.append(slot)
    return available_slots


def create_slots_list(start_time, end_time, slot_size):
    point_in_time = start_time
    days_list = []
    while point_in_time < end_time:
        st_time = point_in_time
        point_in_time = point_in_time + slot_size
        days_list.append((st_time, point_in_time))
    return days_list


def check_if_slot_is_available(slot, intervals):
    for a1, a2 in intervals:
        b1, b2 = slot

        if b1 >= a1 and b1 <= a2 and b2 >= a2:
            return False
        elif b2 >= a1 and b2 <= a2 and b1 <= a1:
            return False
        elif b1 >= a1 and b2 <= a2:
            return False
        elif b1 <= a1 and b2 >= a2:
            return False
    return True
