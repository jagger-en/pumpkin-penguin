from datetime import datetime, timedelta
import random
from faker import Faker
from scheduler import create_non_office_intervals, get_available_slots

fake = Faker()
Faker.seed(0)

def generate_fake_appointment_data():
    fake_data = []

    date_start = datetime(2023, 11, 20)
    date_end = datetime(2023, 12, 10)

    intervals = create_non_office_intervals(date_start, date_end)


    for idx in range(100):
        slot_size = timedelta(minutes=random.randint(15, 30))
        slots = get_available_slots(date_start, date_end, intervals, slot_size)
        if slots:
            chosen_slot = random.choice(slots)
            intervals.append(chosen_slot)

            print(chosen_slot)
            fake_record = {
                'id': idx+1,
                'machine_id': random.choice(['TB1', 'TB2', 'VB1', 'VB2', 'U1']),
                'patient_id': random.randint(1, 100),
                'priority_id': random.choice(['A', 'B']),
                'start_time': chosen_slot[0].strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': chosen_slot[1].strftime('%Y-%m-%d %H:%M:%S')
            }
            fake_data.append(fake_record)

    return fake_data, intervals

generate_fake_appointment_data()
