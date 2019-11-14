#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Define the Result model
"""


class Result(object):

    def __init__(self, message, details={}):
        self.message = message
        self.data = details
