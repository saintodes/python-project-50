install:
	poetry install

lint:
	poetry run flake8 gendiff/

build:
	poetry build

publish: #--dry-run poetry publishing
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

force-reinstall:
	pip install --force-reinstall dist/*.whl

test:
	poetry run pytest

cov:
	poetry run pytest --cov=gendiff --cov-report xml

run:
	poetry run gendiff file1.json file2.json

prc:
	git add .pre-commit-config.yaml
