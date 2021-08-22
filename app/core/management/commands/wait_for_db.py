import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django Command to pause execution untill database is available"""

    def handle(self, *args, **options):
        self.stdout.write('waiting for DB')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 seond....')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
