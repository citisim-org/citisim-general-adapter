#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Defines the blueprint for the users
"""

from flask import Blueprint
from flask_restful import Api

from resources import ReportResource

REPORT_BLUEPRINT = Blueprint('report', __name__)
Api(REPORT_BLUEPRINT).add_resource(ReportResource, '/report/publish')
