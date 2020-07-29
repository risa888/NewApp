from django.apps import AppConfig


class OriginalConfig(AppConfig):
    name = 'original'

    def ready(self):
        import original.signals
