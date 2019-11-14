#!/usr/bin/python
# -*- coding: utf-8 -*-

from schemas import ResultSchema
from http import HTTPStatus
from flask.json import jsonify


class response_generator(object):

    SCHEMA = ResultSchema()

    @staticmethod
    def generate(code, msg, details={}):
        (result, _) = response_generator.SCHEMA.load({'message': msg,
                                                      'details': details})
        response = jsonify(result)
        response.status_code = code
        return response

    @staticmethod
    def internal(msg, details={}):
        response = \
            response_generator.generate(HTTPStatus.INTERNAL_SERVER_ERROR,
                                        msg, details)
        return response

    @staticmethod
    def ok(msg, details={}):
        response = response_generator.generate(HTTPStatus.OK, msg,
                                               details)
        return response

    @staticmethod
    def bad(msg, details={}):
        response = response_generator.generate(HTTPStatus.BAD_REQUEST,
                                               msg, details)
        return response
