from django.apps import AppConfig


class LabelsConfig(AppConfig):
    name = 'labels'
    # Conserve l'identifiant historique des migrations et de la base SQLite.
    label = 'app'
