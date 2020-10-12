# Cleveland Parcel Lookup

## About

Cleveland Parcel Lookup is a web application that allows you to view details of five parcels in Cleveland. Data for this web application is sourced from [Northeast Ohio Community and Neighborhood Data for Organizing (NEOCANDO) at the Center on Urban Property and Community Development](https://neocando.case.edu/) located at [Case Western Reserve University](https://www.case.edu).

Here's what it looks like:

![Cleveland Parcel Lookup](/images/cle_parcel_lookup_light.png)

## Features

- Provides parcel details (image of property, location of the property on a map, and other related information about the parcel) for five parcel numbers located in Cleveland.
- Exposes a web-api endpoint (/parcel/NNN-NN-NNN) for ease of access that interfaces with NEOCANDO's webapi here: http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=NNN-NN-NNN (where N is assumed to be a number).
- Uses Python, Flask, Google Maps Embed API to deliver all these features (among other Python packages).

## Installation - Linux (Or similar Operating Systems)

To aid runtime of this application, a Makefile contains commands that simplifies the process. For each step below the make directives as well as the corresponding commands in bash will be described in an attempt to get the project to run locally.

- Setup virtual environment

Its best to install a virtual environment first to protect your host operating system from any modifications this program may make.

Make directive:

```bash
make create_venv
make activate_venv
```

OR 

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install project dependencies

There are a few dependencies used (as described in requirements-dev.txt), so before we run the program, lets install these dependencies.

Make directive:

```bash
make deps
```

OR 

```bash
pip3 install -r requirements-dev.txt
```

- Run the program in development mode

Since this is a web application developed using Python and Flask, in this step we use the flask binary to host a web server locally.

Make Directive:

```bash
make run
```

OR 

```bash
FLASK_APP=cle_parcel_lookup FLASK_ENV=development flask run
```

- At this point, please open your browser and visit `http://localhost:5000` to access the application.

- To cleanup after viewing the application, do make sure to press `CTRL-C` to
end the flask session.

## Alternative Installation using Wheel

In the off chance that none of the instructions above help with running of the application, do consider building a wheel package for it.

Make directive:

```bash
make dist
```

OR 

```bash
python3 setup.py bdist_wheel
```

This will create a file in the `dist` folder titled `cle_parcel_lookup-1.0.0-py3-none-any.whl`.

This file can then be installed on your system.

Make directive:

```bash
make dist_deploy
```

OR 

```bash
pip3 install dist/cle_parcel_lookup-1.0.0-py3-none-any.whl
```

## Other Directives

This project uses `pylint` as its linter - with its default settings. Here's how you can lint the project:

Make directive:

```bash
make lint
```

OR 

```bash
pylint cle_parcel_lookup
```

In addition to linting, the project uses `pytest` to run unit tests. Here's how you run pytest on the project:

Make directive:

```bash
make test
```

OR 

```bash
PYTHONPATH=. pytest -v
```

Sometimes running unit tests isn't enough and you'd like to know which specific lines in the project lack coverage. Here's how you can run `coverage` tool to discover lines that need unit tested:

Make directive:

```bash
make coverage
```

OR 

```bash
coverage run -m pytest
coverage report
```

