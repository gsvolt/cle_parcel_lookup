SHELL := /bin/bash

create_venv:
	python3 -m venv .venv

activate_venv:
	source .venv/bin/activate

deps:
	pip3 install -r requirements-dev.txt

run:
	FLASK_APP=cle_parcel_lookup FLASK_ENV=development flask run

freeze:
	pip3 freeze > requirements-dev.txt

lint:
	pylint cle_parcel_lookup
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude __pycache__,.coverage,.github,.git,.pytest_cache,.venv,.vscode,build,images,dist
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude __pycache__,.coverage,.github,.git,.pytest_cache,.venv,.vscode,build,images,dist

test:
	PYTHONPATH=. pytest -v

coverage:
	coverage run -m pytest
	coverage report

dist:
	python3 setup.py bdist_wheel

dist_deploy:
	pip3 install dist/cle_parcel_lookup-1.0.0-py3-none-any.whl

container_build:
	docker build --tag=cle_parcel_lookup_image .

container_run: container_build
	docker run -d --name cle_parcel_lookup -p 5000:5000 cle_parcel_lookup_image
