# Cleveland Parcel Lookup

## About

Cleveland Parcel Lookup is a web application that allows you to view details of five parcels in Cleveland. Data for this web application is sourced from [Northeast Ohio Community and Neighborhood Data for Organizing (NEOCANDO) at the Center on Urban Property and Community Development](https://neocando.case.edu/) located at [Case Western Reserve University](https://www.case.edu).

Here's what it looks like:

![Cleveland Parcel Lookup](/images/cle_parcel_lookup_light.png)

## Features

- Provides parcel details (image of property, location of the property on a map, approximate street addresses and other related information about the parcel) for five parcel numbers located in Cleveland.
- Exposes a web-api endpoint (/parcel/NNN-NN-NNN) for ease of access that interfaces with NEOCANDO's webapi here: http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=NNN-NN-NNN (where N is assumed to be a number).
- Uses Python, Flask, Google Maps Embed API and Reverse Geocoding API to deliver all these features (among other Python packages).

## Installation - Linux (Or similar Operating Systems)

To aid runtime of this application, a Makefile contains commands that simplifies the process. For each step below the make directives as well as the corresponding commands in bash will be described in an attempt to get the project to run locally.

- Clone this repo using Git

Easiest way to get this project on your system is to download it using git client in your terminal and change your working folder to the project root:

```bash
git clone https://github.com/gsvolt/cle_parcel_lookup
cd cle_parcel_lookup
```

- Setup virtual environment

Its best to install a virtual environment first to protect your host operating system from any modifications this program may make.

Make directive:

```bash
make create_venv
```

OR 

```bash
python3 -m venv .venv
```

- Activate Virtual Environment 

```bash
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

- Edit the file `cle_parcel_lookup\static\parcel.js` and update `apiKey` variable with a proper API Key from Google.

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

## Installation on Windows

Note: Pre-requisite: You have already installed Python 3.6 or higher

- Open command prompt and clone the project:

```bash
git clone https://github.com/gsvolt/cle_parcel_lookup.git
cd cle_parcel_lookup
```

- Setup a virtual environment

```bash
python -m venv venv
```

- Activate the virtual environment

```bash
venv\Scripts\activate
```
 
- Install dependencies

```
pip install -r requirements-dev.txt
```

- Edit the file `cle_parcel_lookup\static\parcel.js` and update `apiKey` variable with a proper API Key from Google.

- Run the program in development mode

```
set "FLASK_APP=cle_parcel_lookup" & set "FLASK_ENV=development" & flask run
```

- At this point, please open your browser and visit `http://localhost:5000` to access the application.

- To cleanup after viewing the application, do make sure to press `CTRL-C` to
end the flask session.


## Development Features

This project uses `pylint` (with its default settings) as well as `flake8` as its linter (to conform with github's python action). 
Here's how you can lint the project:

Make directive:

```bash
make lint
```

OR 

```bash
pylint cle_parcel_lookup
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude __pycache__,.coverage,.github,.git,.pytest_cache,.venv,.vscode,build,images,dist
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude __pycache__,.coverage,.github,.git,.pytest_cache,.venv,.vscode,build,images,dist
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

