create_venv:
	python3 -m venv .venv

run:
	FLASK_APP=flaskr FLASK_ENV=development flask run

test:
	pytest

coverage:
	coverage run -m pytest
	coverage report