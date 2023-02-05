dev-dep:
	pip-compile --extra dev -o dev-requirements.txt pyproject.toml

install-prod-deps:
	pip-sync

install-dev-deps:
	pip-sync requirements.txt dev-requirements.txt
