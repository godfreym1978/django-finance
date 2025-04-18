# fin/routers.py
class FinanceRouter:
    """
    A router to control all database operations on models in the
    fin application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read fin models go to finance.
        """
        if model._meta.app_label == 'fin':
            return 'finance'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write fin models go to finance.
        """
        if model._meta.app_label == 'fin':
            return 'finance'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the fin app is involved.
        """
        if (
            obj1._meta.app_label == 'fin' or
            obj2._meta.app_label == 'fin'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the fin app only appears in the 'finance'
        database.
        """
        if app_label == 'fin':
            return db == 'finance'
        return None