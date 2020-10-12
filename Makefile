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

test:
	PYTHONPATH=. pytest -v

coverage:
	coverage run -m pytest
	coverage report

dist:
	python3 setup.py bdist_wheel

dist_deploy:
	pip3 install dist/cle_parcel_lookup-1.0.0-py3-none-any.whl