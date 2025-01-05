# Robot cleaning solution

## Installation

### Local machine

`cd app`

Ideally with a python version manager, install Python distribution ^3.10

`pyenv install 3.13.1` [Pyenv installation](https://github.com/pyenv/pyenv#installation)

Activate python version

`pyenv local 3.13.1`

Install poetry

`pip install poetry`

Install project requirements

`poetry install`

You should see a similar output:

`Creating virtualenv app-***-**-py3.13.1 in **/Cache/pypoetry/virtualenvs`

Run server locally

`poetry shell`

`PYTHONPATH=..:$PYTHONPATH python cleaning_robot/main.py`

Should start application on http://0.0.0.0:5000

### Docker

Make sure you have docker and docker-compose installed.

`docker-compose build`

Start the database

`docker-compose up postgres`

Start the application

`docker-compose up app`

Should start application on http://0.0.0.0:5000

## Interacting with the API

If both postgres and app are running, go to http://0.0.0.0:5000/api/ui/.
You can now call the API interactively with the Swagger UI, by clicking "try it now" or "execute" on resources.

## To run the tests
`docker-compose run test_app`
