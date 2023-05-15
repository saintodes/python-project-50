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

runnj:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file1.json' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file2.json'
runny:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file1.yml' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/nested/file2.yml'
runpj:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/plain/file1.json' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/plain/file2.json'
runpy:
	poetry run gendiff '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/plain/file1.yml' '/home/sainttu/Projects/hexlet/python-project-50/tests/fixtures/plain/file2.yml'

prc:
	git add .pre-commit-config.yaml
