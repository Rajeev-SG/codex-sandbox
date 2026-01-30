PYTHON ?= python3
export PYTHONPATH := src

.PHONY: setup lint format typecheck test coverage docs clean

setup:
	$(PYTHON) -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt
	. .venv/bin/activate && pre-commit install

lint:
	ruff check src tests scripts
	radon cc -n B -s src/codex_sandbox
	pylint src/codex_sandbox --disable=all --enable=R0801
	deptry .
	vulture src/codex_sandbox --min-confidence 80
	python scripts/check_todos.py
	python scripts/validate_agents_md.py
	python scripts/check_feature_flags.py

format:
	black src tests scripts
	ruff check --fix src tests scripts

typecheck:
	mypy src

coverage:
	pytest -n auto --durations=10 --cov=codex_sandbox --cov-report=term-missing --cov-report=xml --cov-fail-under=85

test:
	pytest -n auto

docs:
	mkdocs build --strict

clean:
	rm -rf .venv .pytest_cache .mypy_cache .ruff_cache .coverage dist site
