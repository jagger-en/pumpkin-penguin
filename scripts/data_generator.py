from datetime import datetime, timedelta
import random
from faker import Faker
import pytz

fake = Faker()
Faker.seed(0)

def generate_fake_appointment_data():
    fake_data = []

    for idx in range(500):
        start_date = fake.date_between_dates(date_start=datetime(2023, 11, 20), date_end=datetime(2023, 12, 25))
        start_datetime = datetime.strptime(str(start_date), '%Y-%m-%d').replace(hour=random.randint(8, 16), minute=random.randint(0, 59))
        end_datetime = start_datetime + timedelta(minutes=random.randint(1, 30))

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

