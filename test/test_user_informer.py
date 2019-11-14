#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from util import user_informer


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class TestAuthorInformer(unittest.TestCase):
    @patch("requests.get")
    @patch("requests.post")
    def test_get_email_no_token_ok(self, mock_post_login, mock_get_email):
        """ The get_email on `user_informer` without old token """
        """ should return an email """

        mock_post_login.return_value = MockResponse({"id_token": "0"}, 200)
        mock_get_email.return_value = MockResponse(
            {"email": "e@mail.com"}, 200)

        result = user_informer.get_email("admin")

        self.assertEqual(result, "e@mail.com")

    @patch("requests.get")
    def test_get_email_token_ok(self, mock_get_email):
        """ The get_email on `user_informer` with old token """
        """ should return an email """

        user_informer.auth["token"] = "0"
        mock_get_email.return_value = MockResponse(
            {"email": "e@mail.com"}, 200)

        result = user_informer.get_email("admin")

        self.assertEqual(result, "e@mail.com")

    @patch("requests.get")
    @patch("requests.post")
    def test_get_email_token_expired(self, mock_post_login, mock_get_email):
        """ The get_email on `user_informer` with token expired """
        """ should return an email """

        user_informer.auth["token"] = "0"

        mock_post_login.return_value = MockResponse({"id_token": "0"}, 200)
        mock_get_email.side_effect = [
            MockResponse({}, 401),
            MockResponse({"email": "e@mail.com"}, 200),
        ]

        result = user_informer.get_email("admin")

        self.assertEqual(result, "e@mail.com")

    @patch("requests.get")
    @patch("requests.post")
    def test_get_email_bad_credentails(self, mock_post_login, mock_get_email):
        """ The get_email on `user_informer` with bad credentails """
        """ should raise a exception """

        mock_post_login.return_value = MockResponse({}, 401)

        self.assertRaises(ValueError, user_informer.get_email, "admin")
