dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager:app

lint:
	poetry run flake8 page_analyzer

build-app:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

install:
	poetry install

build:
	./build.sh
