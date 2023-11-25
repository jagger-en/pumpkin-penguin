#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass

class TestEndpoints(BaseClass):

    RESOURCE_PATH = '/api/v1/patient'

    def test_data_is_created(self):
        with self.flask_app.app_context():
            from backend.models.patient import Patient
            test_data = []
            test_data.append(Patient(id=1, first_name='Foo',
                                     last_name='Bar', weight=76.5))
            self.db.session.add_all(test_data)
            self.db.session.commit()

        result = self.endpoint_client.get(self.RESOURCE_PATH)
        self.assertEqual([{'last_name': 'Bar', 'weight': 76.5, 'id': '1', 'first_name': 'Foo'}],
                         result.json)

if __name__ == '__main__':
    unittest.main()
