# Citisim Reports Adapter

This project is an example of a server with a endpoint to publish reports with libcitisim

## Table of Contents
1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Commands](#commands)
1. [Application Structure](#application-structure)
1. [Development](#development)
1. [Testing](#testing)
1. [Lint](#lint)
1. [Swagger](#swagger)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/citisim-org/citisim-elasticsearch-adapter.git <my-project-name>
$ cd <my-project-name>
```

Then install the example container and check that it works

```bash
$ make install      # Build container and install the pip dependencies
$ make start        # Run the container containing your local python server
```
If everything works, you should see the available routes [here](http://127.0.0.1:4000/swagger/apidocs).

The API runs locally on docker containers. You can easily change the python version you are willing to use on Dockerfile.

## Commands

While developing, you will probably rely mostly on `make start`; however, there are additional scripts at your disposal:

|`make <script>`|Description|
|------------------|-----------|
|`install`|Install or upgrade the pip dependencies and the server's container.|
|`start`|Run your local server in its own docker container.|
|`stop`|Stop your local server in its own docker container.|
|`daemon`|Run your local server in its own docker container as a daemon.|
|`tests`|Run unit tests with unittest in its own container.|
|`lint`|Run flake8 on the `src` directory.|


## Example Structure

The example structure presented in this boilerplate is grouped primarily by file type. Please note, however, that this structure is only meant to serve as a guide, it is by no means prescriptive.

```
.
├── src                           # Example source code
│   ├── models                    # Python classes modeling     
│   │   └── report.py             # Definition of the report model
│   │   └── result.py             # Definition of the result model
│   ├── schemas                   # Python classes scheming     
│   │   └── report.py             # Definition of the report model
│   │   └── result.py             # Definition of the report model
│   ├── services                  # Python classes allowing you to interact with the world
│   │   └── report.py             # Methods to easily handle report models
│   ├── resources                 # Python classes containing the HTTP verbs of your routes
│   │   └── report.py             # Rest verbs related to the report routes
│   ├── routes                    # Routes definitions and links to their associated resources
│   │   ├── __init__.py           # Contains every blueprint of your API
│   │   └── report.py             # The blueprint related to the report
│   ├── swagger                   # Resources documentation
│   │   └── report                # Documentation of the rest resource
│   │       └── POST.yml          # Documentation of the POST method on the report resource
│   ├── util                      # Some helpfull, non-business Python functions for your project
│   │   └── user_informer.py      # Wrapper for get user email
│   │   └── result_generator.py   # Wrapper for generate results of HTTP
│   │   └── reverse_proxied.py    # Wrapper for reverse proxied compatibility
│   ├── config.py                 # Project configuration settings
│   ├── publisher.config          # Libcitisim publisher configuration settings
│   └── server.py                 # Server configuration
└── test                          # Unit tests source code
```

## Development

To develop locally, here are your two options:

```bash
$ make start           # Create the containers containing your python server in your terminal
$ make daemon          # Create the containers containing your python server as a daemon
```

The containers will reload by themselves as your source code is changed.
You can check the logs in the `./server.log` file.

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./test/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly.
You can run your tests in their own container with the command:

```bash
$ make tests
```

## Lint

To lint your code using flake8, just run in your terminal:

```bash
$ make lint
```

It will run the flake8 commands on your project in your server container, and display any lint error you may have in your code.

## Swagger

Your API needs a description of it's routes and how to interact with them.
You can easily do that with the swagger package included in the starter kit.
Simply add a docstring to the resources of your API like in the `report`.
The API description will be available [here](http://127.0.0.1:4000/swagger/specs.json) and the SwaggerUi will be available [here](http://127.0.0.1:4000/swagger/apidocs)

