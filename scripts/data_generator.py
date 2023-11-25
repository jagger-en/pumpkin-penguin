from datetime import datetime, timedelta
import random
from faker import Faker
import pytz

fake = Faker()
Faker.seed(0)

def generate_fake_appointment_data():
    fake_data = []

    for idx in range(100):
        start_date = fake.date_between_dates(date_start=datetime(2023, 11, 25), date_end=datetime(2023, 12, 25))
        start_time = fake.time_object(end_datetime=datetime.combine(start_date, datetime.max.time()))

        start_datetime = datetime.combine(start_date, start_time).replace(tzinfo=pytz.UTC)
        end_datetime = start_datetime + timedelta(minutes=random.randint(1, 30))

        if 8 <= start_datetime.hour <= 16 and 8 <= end_datetime.hour <= 16:
            fake_record = {
                'id': idx+1,
                'machine_id': random.choice(['TB1', 'TB2', 'VB1', 'VB2', 'U1']),
                'patient_id': 5,
                'priority_id': random.choice(['A', 'B']),
                'start_time': start_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': end_datetime.strftime('%Y-%m-%d %H:%M:%S')
            }
            fake_data.append(fake_record)

    return fake_data

