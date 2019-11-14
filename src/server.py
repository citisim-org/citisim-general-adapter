#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.blueprints import Blueprint
from flask.json import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from util import reverse_proxied

import config
import routes

# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

server = Flask(__name__)
server.wsgi_app = reverse_proxied(server.wsgi_app)
server.json_encoder = LazyJSONEncoder

template = dict(swaggerUiPrefix=LazyString(
    lambda: request.environ.get('HTTP_X_SCRIPT_NAME', '')))

server.config['SWAGGER'] = {  # all in
    'swagger_version': '2.0',
    'title': 'Citisim Reports Connector',
    'specs': [{
        'version': '0.0.1',
        'title': 'Citisim Reports Connector',
        'endpoint': 'specs',
        'route': '/swagger/specs.json',
        'rule_filter': lambda rule: True,
    }],
    'static_url_path': '/swagger/static',
    'specs_route': '/swagger/apidocs'
}

swagger = Swagger(server, template=template)

server.debug = config.DEBUG

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint,
                                  url_prefix=config.APPLICATION_ROOT)

if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT)
