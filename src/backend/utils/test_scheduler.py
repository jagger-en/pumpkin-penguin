#!/usr/bin/env python3

import unittest
from datetime import datetime as dt
from datetime import timedelta as td
from scheduler import get_available_slots


class TestGetAvailableSlots(unittest.TestCase):

    def test_various_inputs(self):

        test_data = [
            (dt(2023, 11, 25, 13, 00),
             dt(2023, 11, 25, 14, 00),
             [(dt(2023, 11, 25, 13, 0), dt(2023, 11, 25, 13, 28))],
             [(dt(2023, 11, 25, 13, 30), dt(2023, 11, 25, 13, 45)),
              (dt(2023, 11, 25, 13, 45), dt(2023, 11, 25, 14, 00))]),
            (dt(2023, 11, 25, 13, 00),
             dt(2023, 11, 25, 14, 00),
             [(dt(2023, 11, 25, 13, 00), dt(2023, 11, 25, 13, 31))],
             [(dt(2023, 11, 25, 13, 45), dt(2023, 11, 25, 14, 00))]),
        ]
        for start_time, end_time, intervals, expected_slots in test_data:
            available_slots = get_available_slots(
                start_time, end_time, intervals, td(minutes=15))
            self.assertEqual(available_slots, expected_slots)


if __name__ == '__main__':
    unittest.main()
