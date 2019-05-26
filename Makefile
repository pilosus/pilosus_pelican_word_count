.DEFAULT_GOAL := lint


.PHONY: install
install:
	pip install -U pip
	pip install -U -r requirements.txt

.PHONY: format
format:
	isort -rc -w 88 .
	black -S -l 88 --target-version py37 .

.PHONY: lint
lint:
	flake8 .
	black -S -l 88 --target-version py37 --check .
