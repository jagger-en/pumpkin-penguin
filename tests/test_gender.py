#!/usr/bin/env python3
import unittest
from utils.base_class import BaseClass

class TestEndpoints(BaseClass):

    RESOURCE_PATH = '/api/v1/gender'

    def test_data_is_created(self):
        with self.flask_app.app_context():
            from backend.models.gender import Gender
            test_data = []
            test_data.append(Gender(id=1, name='male'))
            self.db.session.add_all(test_data)
            self.db.session.commit()

        result = self.endpoint_client.get(self.RESOURCE_PATH)
        self.assertEqual([{'id': '1', 'name': 'male'}],
                         result.json)

    def test_data_is_updated(self):
        with self.flask_app.app_context():
            from backend.models.gender import Gender
            test_data = []
            test_data.append(Gender(id=1, name='old-gender'))
            self.db.session.add_all(test_data)
            self.db.session.commit()

        result = self.endpoint_client.get(self.RESOURCE_PATH)
        self.assertEqual([{'id': '1', 'name': 'old-gender'}],
                         result.json)


        result = self.endpoint_client.put(self.RESOURCE_PATH, json={'id': '1', 'name': 'new-gender'})
        self.assertEqual(result.status_code, 201)

        result = self.endpoint_client.get(self.RESOURCE_PATH)
        self.assertEqual([{'id': '1', 'name': 'new-gender'}],
                         result.json)


    def test_deleting_resource(self):
        with self.flask_app.app_context():
            from backend.models.gender import Gender
            test_data = []
            test_data.append(Gender(id=1, name='female'))
            self.db.session.add_all(test_data)
            self.db.session.commit()

        record_id = 1

        response = self.delete_resource_by_id(record_id)
        self.assertEqual(response.status_code, 200)

        response = self.get_resource_by_id(record_id)
        self.assertEqual(response.status_code, 404)

    def test_delete_request_for_non_existing_resource(self):
        response = self.delete_resource_by_id('non-existing-123')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json, "Resource with id=non-existing-123 not found")

    def test_delete_request_without_id(self):
        response = self.endpoint_client.delete(self.RESOURCE_PATH, json={})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, "Resource id must be given")

    ##############
    # Helper Methods
    ###

    def get_resource_by_id(self, record_id, nested=False):
        param_string = '%s?id=%s'
        if nested:
            param_string = '%s?id=%s&nested=true'
        return self.endpoint_client.get(param_string % (self.RESOURCE_PATH, record_id))

    def delete_resource_by_id(self, record_id):
        return self.endpoint_client.delete("%s?id=%s" % (self.RESOURCE_PATH, record_id))

if __name__ == '__main__':
    unittest.main()
