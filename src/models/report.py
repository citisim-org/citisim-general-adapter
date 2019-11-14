#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Define the Report model
"""


class Report(object):

    def __init__(
        self,
        userId,
        photoDescription,
        date,
        id,
        latitude,
        longitude,
        altitude,
        photoPath,
        status,
        title,
        category
    ):

        self.userId = userId
        self.photoDescription = photoDescription
        self.date = date
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.photoPath = photoPath
        self.status = status
        self.title = title
        self.category = category

    def __repr__(self):
        return '<Report(userId={self.userId!r})>'.format(self=self)
