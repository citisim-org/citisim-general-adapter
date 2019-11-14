#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os

DEBUG = os.getenv('ENVIRONMENT') == 'DEV'
APPLICATION_ROOT = os.getenv('APPLICATION_ROOT', '')
HOST = os.getenv('APPLICATION_HOST')
PORT = int(os.getenv('APPLICATION_PORT', '9000'))

PUBLISHER = {
    'CONFIG_PATH': os.getenv(
        'PUBLISHER_CONFIG_PATH',
        './publisher.config'),
    'TRANSDUCER_TYPE': os.getenv(
        'PUBLISHER_TRANSDUCER_TYPE',
        'CitizenReporter'),
    'BROKER_SOURCE': os.getenv(
        'PUBLISHER_BROKER_SOURCEE',
        '0000000000000000')}

USER_INFORMER = {
    'AUTH': {
        'URL': os.getenv(
            'USER_INFORMER_AUTH_URL',
            'http://127.0.0.1:8080/api/authenticate'),
        'USERNAME': os.getenv(
            'USER_INFORMER_AUTH_USERNAME',
            'user'),
        'PASSWORD': os.getenv(
            'USER_INFORMER_AUTH_PASSWORD',
            'password')},
    'INFO_URL': os.getenv(
        'USER_INFORMER_INFO_URL',
        'http://127.0.0.1:8080/api/users/')}

logging.basicConfig(filename=os.getenv('SERVICE_LOG', 'server.log'),
                    level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s \
                            pid:%(process)s module:%(module)s %(message)s',
                    datefmt='%d/%m/%y %H:%M:%S')
