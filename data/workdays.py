import numpy as np
import pandas as pd
from datetime import datetime, timedelta

import http.client
import json
import csv

conn = http.client.HTTPSConnection("date.nager.at")

year = 2024
# headers = {
#     'x-api-key': "059da98dc24f4e655f3d09c6cc7c5e8c0120f3acc1121c9f877056c95a8f6dd3",
#     'Content-type': "application/json"
#     }

conn.request("GET", f"/api/v3/publicholidays/{year}/HU") 

res = conn.getresponse()
data = res.read()
holidays = json.loads(data)
dates = [holiday["date"] for holiday in holidays]

def generate_workdays(year, holidayss):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    # Generate an array of dates from start_date to end_date
    date_range = pd.date_range(start_date, end_date)

    # Filter out weekends and holidays
    workdays = [date for date in date_range if date.weekday() < 5 and date not in holidayss]

    return workdays

# Example usage

# hungary_public_holidays = [
#     datetime(year, 1, 1),  # New Year's Day
#     datetime(year, 3, 15), # National Day
#     datetime(year, 5, 1),  # Labor Day
#     datetime(year, 8, 20), # St. Stephen's Day
#     datetime(year, 10, 23),# National Day
#     datetime(year, 12, 25),# Christmas
#     datetime(year, 12, 26),# Second Christmas Day
# ]

hungary_public_holidays = [datetime.strptime(date_string, "%Y-%m-%d") for date_string in dates]

workdays = generate_workdays(year, hungary_public_holidays)

# Define the CSV file path
csv_file_path = 'workdays.csv'

# Write workdays to CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Workday']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the workdays
    for workday in workdays:
        writer.writerow({'Workday': workday.strftime("%Y-%m-%d")})

print(f'Workdays saved to {csv_file_path}')

# Print the workdays
# for workday in workdays:
#     print(workday.strftime("%Y-%m-%d"))
