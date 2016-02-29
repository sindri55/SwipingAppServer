# SwipingAppServer
Server for the Tapit application

Current Python version: 3.5.0 although > 3.4 is fine.

# Setup

## Python version > 3.4

Install for your OS

## Virtualenv (Virtual environment)

### Installing

> pip install virtualenv

### Creating a virtualenv

> virtualenv -p python3 {virtualenv name}

The name could be, for instance, .tapit

### Activating it

> source name_of_virtualenv/bin/activate

## Install project required

From the SwipingAppServer directory:

> pip install -r REQUIREMENTS

REQUIREMENTS is just a file containing information about the python packages and their versions used in the project.

# Running the server

With the virtualenv active:

> python manage.py runserver [IP:PORT]

The IP is usually either 127.0.0.1 to run purely locally or 0.0.0.0 to run broadcasted from the computer. Port up to you when in dev, the convention is 8000
