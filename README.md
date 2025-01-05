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


### To run the tests
`docker-compose run test_app`


## Interacting with the API

If both postgres and app are running, go to http://0.0.0.0:5000/ui/.
You can now call the API interactively with the Swagger UI, by clicking "try it now" or "execute" on resources.

## Implementation documentation

### Setup:
I chose an easy way to set up an API using flask and connexion.
The build in capabilities allow us to interact easily with the API
via the Swagger UI, and it is also easy to define the endpoints in the openapi schema.

### Algorithm:
You may find all code related to the algorithm inside the module `/path_calculation`

- The `robot_cleaning_simulator` class is the business layer of abstractization, it receives commands
and traverses the grid only. This class does not need to know the inner workings of PlacesStructure. Should
we decide to use a different structure, we need only refactor unique_places_structure module, not touching the business layer.

- The `unique_places_structure` holds in memory the input from the commands and can calculate the unique places count.

    I had tried in the beginning to use a simple set to hold unique points. This was
    not efficient in terms of memory

    I decided to use operations on segments instead. The structure holds
    horizontal and vertical segments as dictionaries. Each point on the axis
    is a key and the values are segments on that specific point or line.

To get the unique places, in method `compute_unique_places` of `PlacesStructure`,
the algorithm does as follows:
- Goes through elements of horizontal and vertical segments and merges the intervals. At the same
time it will calculate the number of unique points on the lines.
- Goes through the now merged and sorted segments and determines whether
they intersect on the different axes. Because the keys of dictionaries are also sorted, it will
not compare with all the segments in most cases.

## Complexities
We can define 'n' as being the number of commands.
- The first traversal of the commands is O(n) because we are inserting new segments in a dictionary and appending
to lists which are both O(1). Although, not always getting an element from a dictionary is O(1), at the sizes
of n <= 10k commands, collisions shouldn't pose an issue.
- Merging of the intervals *should be* O(nlog(n)) in the worst case when we would merge all input segments
 on the same line.
- The calculation of intersections will compare each segment with all the others in the worst case,
which results in O(n^2).
This leads to a total complexity of O(n) + O(nlog(n)) + O(n^2) => O(n^2)


