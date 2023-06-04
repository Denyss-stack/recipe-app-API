"""
Django command for wait the database is available
"""

from django.core.management.base import BaseCommand # noqa
import time
from psycopg2 import OperationalError as Psycopg2OpError # noqa
from django.db.utils import OperationalError # noqa


class Command(BaseCommand):
    """Django command for wait the database"""
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database is anavailable, wait for 1 second') 
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available!'))
