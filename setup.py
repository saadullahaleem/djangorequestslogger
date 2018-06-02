import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-request-logger",
    version="0.0.1",
    author="Saadullah Aleem",
    author_email="aleemsaadullah@gmail.com",
    description="Django middleware to log all requests to the system in the database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saadullahaleem/djangorequestslogger",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'django',
        'djangorestframework',
        'psycopg2',
        'django-ipware',
        'django-json-widget'
    ]
)