#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import config


class user_informer(object):

    auth = {
        'url': config.USER_INFORMER['AUTH']['URL'],
        'username': config.USER_INFORMER['AUTH']['USERNAME'],
        'password': config.USER_INFORMER['AUTH']['PASSWORD'],
        'token': '',
    }

    info_url = config.USER_INFORMER['INFO_URL']

    @staticmethod
    def login():
        login_data = {'username': user_informer.auth['username'],
                      'password': user_informer.auth['password'],
                      'rememberMe': 'true'}

        response = requests.post(user_informer.auth['url'],
                                 json=login_data)

        if not str(response.status_code).startswith('20'):
            raise ValueError('Cannot login on auth server')
        else:
            user_informer.auth['token'] = response.json()['id_token']

    @staticmethod
    def check_logged():
        if not user_informer.auth['token']:
            user_informer.login()

    @staticmethod
    def get_email(userId, first_time=True):
        user_informer.check_logged()

        headers = {'Authorization': 'Bearer '
                   + user_informer.auth['token']}

        response = requests.get(user_informer.info_url + userId,
                                headers=headers)

        if str(response.status_code).startswith('20'):
            return response.json()['email']

        if first_time:
            user_informer.auth['token'] = ''
            return user_informer.get_email(userId, False)
        else:
            raise ValueError('Cannot get email on auth server')
