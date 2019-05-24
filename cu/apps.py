from django.apps import AppConfig


class CuConfig(AppConfig):
    name = 'cu'

    def ready(self):
        import cu.signals
