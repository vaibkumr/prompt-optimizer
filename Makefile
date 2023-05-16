docs_build:
	cd docs && poetry run make html

docs_clean:
	cd docs && poetry run make clean


docs_linkcheck:
	poetry run linkchecker docs/_build/html/index.html	

lint lint_diff:
	poetry run isort prompt_optimizer/
	poetry run black prompt_optimizer/
	poetry run ruff prompt_optimizer/ --fix

test:
	poetry run pytest tests/unit_tests

help:
	@echo '----'
	@echo 'docs_build          - build the sphinx documentation'
	@echo 'docs_clean          - clean the documentation build artifacts'
	@echo 'test                - run unit tests'