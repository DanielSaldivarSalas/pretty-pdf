dev-dep:
	pip-compile --extra dev -o dev-requirements.txt pyproject.toml
	pip-sync requirements.txt dev-requirements.txt

install-prod-deps:
	pip-sync


.PHONY: test
test:
	python3 -m pytest
	
.PHONY: ci
ci:
	pre-commit
	make test
