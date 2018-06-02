Request Logger
=====

This is a simple Django middleware to log all http requests to your django application. It logs
request data, response, HTTP methods, and requesting IP.

This model only runs with PostgreSQL as the database for now.

# Requirements

* Python (3.4, 3.5, 3.6)
* Django (1.11, 2.0)

# Installation

Install using `pip`...

    pip install django-request-logger

Add `'logger'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'logger',
    )

Add `'logger.middleware'` to the `'MIDDLEWARES'` in your settings:

    MIDDLEWARE = [
    ...
    'logger.middleware',
    ]

Run `python manage.py migrate` to create the `'RequestLog'` models.