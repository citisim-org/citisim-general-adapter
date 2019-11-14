#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Defines the Report repository """

from models import Report
from libcitisim import Broker, Citizen
from util import user_informer
import config


class ReportService:

    broker_config_file = config.PUBLISHER['CONFIG_PATH']
    transducer_type = config.PUBLISHER['TRANSDUCER_TYPE']
    broker_source = config.PUBLISHER['BROKER_SOURCE']

    @staticmethod
    def publish(report):
        report = Report(**report)

        user_email = user_informer.get_email(report.userId)

        broker = Broker(ReportService.broker_config_file)

        publisher = broker.get_publisher(
            source=ReportService.broker_source,
            transducer_type=ReportService.transducer_type)

        report_to_publish = Citizen.CitizenReport(
            report.id, report.photoDescription.split(','), report.photoPath)

        report_properties = {
            'latitude': report.latitude,
            'longitude': report.longitude,
            'altitude': report.altitude,
            'timestamp': report.date,
            'category': report.category,
            'citizenemail': user_email
        }

        publisher.publish(report_to_publish, meta=report_properties)
