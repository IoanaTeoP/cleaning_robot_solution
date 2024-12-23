# Robot cleaning solution

## Installation

### Local machine

`$ cd app`

Ideally with a python version manager, install Python distribution ^3.10

`$ pyenv install 3.13.1` [Pyenv installation](https://github.com/pyenv/pyenv#installation)

Activate python version

`$ pyenv local 3.13.1`

Install poetry

`$ pip install poetry`

Install project requirements

`$ poetry install`

You should see a similar output:

`Creating virtualenv app-***-**-py3.13.1 in **/Cache/pypoetry/virtualenvs`

Run server locally

`cd cleaning_robot`

`PYTHONPATH=..:$PYTHONPATH python app.py`

Should start application on http://0.0.0.0:5000

### Docker

Make sure you have docker and docker-compose installed.

`$ docker-compose build`

`$ docker-compose up postgres app`

Should start application on http://0.0.0.0:5000

## Play with the API

If both postgres and app are running, go to http://0.0.0.0:5000/api/ui/.
You can now call the API interactively with the Swagger UI, by clickig "try it now" or "execute" on resources.


### Algorithm
The algorithm uses a dictionary to store the unique points that the robot has visited.
The result is them calculated as the sum of the lengths of the values of this dictionary.

# Disclaimer
The structure and method are not the most efficient when it comes to memory. The structure
starts to have hash collisions and it does not perform well on large path
inputs.
