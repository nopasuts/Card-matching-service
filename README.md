# Card-matching-service
Card matching service using python FastAPI

## Features

- Create new board game
- Update clicks after each card opens
- Save each game best click counts into database
- Save global best click counts
- Save user best click counts

## Getting start
- Git clone `https://github.com/nopasuts/Card-matching-service.git`

Development
---------
Postgres database is run on docker for easier development purpose
First, start service and database using docker-compose: ::
``docker-compose up``
Then service and database will be started, and migrations will be executed

## ENV
Environment varaiables can be set in ``docker-compose.yml``

``DB_CONNECTION``: Specify database connection URL
``GAME_BOARD_SIZE``: Specify board size. Can not less than 3 otherwise it will use 3 as default. If not specify will use 4 as default.
[Example]
``GAME_BOARD_SIZE`` = 4
It will create game board of 4x3 cards
``GAME_BOARD_SIZE`` = 5
It will create game board of 5x4 cards

Run tests
---------

Tests for this project are defined in the ``tests/`` folder.

This project uses `pytest
<https://docs.pytest.org/>`_ to define tests because it allows you to use the ``assert`` keyword with good formatting for failed assertations.


To run all the tests of a project, simply run the ``pytest`` command: ::
Or run in poetry shell inorder to auto install dependencies:
``poetry install``
``poetry shell``
``pytest``


Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.

