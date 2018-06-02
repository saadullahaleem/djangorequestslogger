=====
Request Logger
=====

Request Logger is a simple Django middleware to log all http requests to your django application. It logs
request data, response, HTTP methods, and requesting IP.

This model only runs with PostgreSQL as the database, since it stores request and response as JSON.

Quick start
-----------

1. Add "logger" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'logger',
    ]

2. Add requestlogger to the MIDDLEWARES in your settings:

    MIDDLEWARE = [
    ...
    'logger.middleware',
    ]

3. Run `python manage.py migrate` to create the RequestLogger models.