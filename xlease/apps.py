from django.apps import AppConfig


class XleaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'xlease'

    def ready(self) -> None:
        import xlease.signals