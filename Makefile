.PHONY: test, lint, run

test:
	uv run pytest tests/ -vv --cov --cov-branch

lint:
	uv run ruff check .
	uv run ruff format --check --diff .

run:
	uv run scripts/sevens.py
