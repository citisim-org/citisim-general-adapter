#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Define the REST verbs relative to the reports
"""

from flasgger import swag_from
from flask_restful import Resource
from flask.json import request

from services import ReportService
from schemas import ReportSchema

from util import response_generator

import logging


class ReportResource(Resource):

    """ Verbs relative to the reports """

    @swag_from('../swagger/report/POST.yml')
    def post(self):
        """ Publish an report based on the sent information """

        report_json = request.get_json()

        response = response_generator.ok('Report created successfully',
                                         report_json)

        schema = ReportSchema()
        (report, error) = schema.load(report_json)

        if error:
            response = response_generator.bad('Invalid report received', error)
        else:
            try:
                ReportService.publish(report)
            except Exception as e:
                logging.exception('Could not publish report')
                response = \
                    response_generator.internal(
                        'Could not publish report', str(e).capitalize())
        return response
