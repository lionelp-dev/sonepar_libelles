.PHONY: shell run

# Crée l'environnement virtuel et ouvre Fish avec celui-ci activé.
shell: .venv/bin/python
	fish -i -C 'source .venv/bin/activate.fish'

# Lance le serveur de développement Django sans rechargement automatique.
run: .venv/bin/python
	.venv/bin/python manage.py runserver --noreload 127.0.0.1:8000

# Crée l'environnement virtuel s'il n'existe pas encore.
.venv/bin/python:
	python3 -m venv .venv
