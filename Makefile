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

runns:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file1.json' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file2.json'

runfs:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/flat/file1.yml' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/flat/file2.yml'

runnp:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file1.json' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file2.json' --format plain
runnj:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file1.json' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file2.json' --format json

prc:
	git add .pre-commit-config.yaml
