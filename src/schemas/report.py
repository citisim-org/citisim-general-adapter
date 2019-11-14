#!/usr/bin/python
# -*- coding: utf-8 -*-

from marshmallow import Schema, fields


class ReportSchema(Schema):

    userId = fields.Str(required=True)
    photoDescription = fields.Str(required=True)
    date = fields.Int(required=True)
    id = fields.Str(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    altitude = fields.Float(required=True)
    photoPath = fields.Str(required=True)
    status = fields.Str(required=True)
    title = fields.Str(required=True)
    category = fields.Str(required=True)
