# Runbooks

## CI is failing
1. Run `make lint` locally to surface linting errors.
2. Run `make typecheck` and `make coverage` to verify typing and test coverage.
3. If docs fail, run `make docs` and review `mkdocs.yml` or the referenced docs.

## Updating tooling
1. Update pinned versions in `requirements.txt` and `requirements-dev.txt`.
2. Run `make setup` to refresh your environment.
3. Run `make lint` and `make coverage`.
