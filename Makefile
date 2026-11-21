.PHONY: shell install run run-api run-web

API_DIR := apps/api

# Crée l'environnement virtuel et ouvre Fish avec celui-ci activé.
shell: .venv/bin/python
	fish -i -C 'source .venv/bin/activate.fish'

# Installe les dépendances Python et Angular.
install: .venv/bin/python
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r $(API_DIR)/requirements.txt
	npm --prefix apps/web install

# Lance l'API Django et le frontend Angular en parallèle.
run: .venv/bin/python
	@set -e; \
	.venv/bin/python $(API_DIR)/manage.py runserver --noreload 127.0.0.1:8000 & api_pid=$$!; \
	npm --prefix apps/web start & web_pid=$$!; \
	trap 'kill $$api_pid $$web_pid 2>/dev/null || true' INT TERM EXIT; \
	wait $$api_pid $$web_pid

# Lance uniquement l'API Django.
run-api: .venv/bin/python
	.venv/bin/python $(API_DIR)/manage.py runserver --noreload 127.0.0.1:8000

# Lance uniquement le frontend Angular.
run-web:
	npm --prefix apps/web start

# Crée l'environnement virtuel s'il n'existe pas encore.
.venv/bin/python:
	python3 -m venv .venv
