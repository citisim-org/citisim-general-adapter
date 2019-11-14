#!/usr/bin/python
# -*- coding: utf-8 -*-

from marshmallow import Schema, fields


class ResultSchema(Schema):

    message = fields.Str(required=True)
    details = fields.Raw(required=True)
