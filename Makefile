docs_build:
	cd docs && poetry run make html

docs_clean:
	cd docs && poetry run make clean


docs_linkcheck:
	poetry run linkchecker docs/_build/html/index.html	

PYTHON_FILES=.
lint: PYTHON_FILES=.
lint_diff: PYTHON_FILES=$(shell git diff --name-only --diff-filter=d master | grep -E '\.py$$')

lint lint_diff:
	poetry run black $(PYTHON_FILES) --check
	poetry run ruff .

format:
	poetry run black .
	poetry run ruff --select I --fix .	

test:
	poetry run pytest tests/unit_tests

help:
	@echo '----'
	@echo 'docs_build          - build the sphinx documentation'
	@echo 'docs_clean          - clean the documentation build artifacts'
	@echo 'format              - run code formatters, black and ruff'
	@echo 'test                - run unit tests'