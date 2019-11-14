#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import json
from unittest.mock import patch

from server import server


class TestReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    @patch('services.ReportService.publish')
    def test_publish_ok(self, mock_report_publish):
        """ The POST on `/report` should publish an report """

        mock_report_publish.return_value = True

        example_report = {
            'id': 'id',
            'userId': 'userId',
            'photoDescription': 'tag1,tag2,tag3,tag4',
            'date': '0',
            'latitude': '0',
            'longitude': '0',
            'altitude': '0',
            'photoPath': 'photoPath',
            'status': 'status',
            'title': 'title',
            'category': 'category'
        }

        response = self.client.post('/report/publish',
                                    content_type='application/json',
                                    data=json.dumps(example_report))

        self.assertEqual(response.status_code, 200)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json,
                         {'message': 'Report created successfully',
                          'details': example_report})

    @patch('services.ReportService.publish')
    def test_publish_missing_data(self, mock_report_publish):
        """ The POST on `/report` should not publish an report """
        """ if some data is missing """

        mock_report_publish.return_value = True

        example_report = {
            'userId': 'userId',
            'photoDescription': 'tag1,tag2,tag3,tag4',
            'date': '0',
            'latitude': '0',
            'longitude': '0',
            'altitude': '0',
            'photoPath': 'photoPath',
            'status': 'status',
            'title': 'title',
            'category': 'category'
        }

        response = self.client.post('/report/publish',
                                    content_type='application/json',
                                    data=json.dumps(example_report))

        self.assertEqual(response.status_code, 400)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json,
                         {'message': 'Invalid report received',
                          'details': {'id': ['Missing data for required field.'
                                             ]}})

    @patch('services.ReportService.publish')
    def test_publish_invalid_type(self, mock_report_publish):
        """ The POST on `/report` should not publish an report """
        """ if some data have a invalid type """

        mock_report_publish.return_value = True

        example_report = {
            'id': 'id',
            'userId': 'userId',
            'photoDescription': 'tag1,tag2,tag3,tag4',
            'date': 'invalid',
            'latitude': '0',
            'longitude': '0',
            'altitude': '0',
            'photoPath': 'photoPath',
            'status': 'status',
            'title': 'title',
            'category': 'category'
        }

        response = self.client.post('/report/publish',
                                    content_type='application/json',
                                    data=json.dumps(example_report))

        self.assertEqual(response.status_code, 400)

        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json,
                         {'message': 'Invalid report received',
                          'details': {'date': ['Not a valid integer.']}})

    @patch('services.ReportService.publish')
    def test_publish_exception(self, mock_report_publish):
        """ The POST on `/report` should not publish an report """
        """ if some exception is raised """

        exception = Exception('Exception')
        mock_report_publish.side_effect = exception

        example_report = {
            'id': 'id',
            'userId': 'userId',
            'photoDescription': 'tag1,tag2,tag3,tag4',
            'date': '0',
            'latitude': '0',
            'longitude': '0',
            'altitude': '0',
            'photoPath': 'photoPath',
            'status': 'status',
            'title': 'title',
            'category': 'category'
        }

        response = self.client.post('/report/publish',
                                    content_type='application/json',
                                    data=json.dumps(example_report))

        self.assertEqual(response.status_code, 500)

        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response_json,
                         {'message': 'Could not publish report',
                          'details': str(exception)})
