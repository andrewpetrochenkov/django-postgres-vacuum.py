from django.core.management.base import BaseCommand
from django.db import connection

SQL = """
SELECT schemaname,relname
FROM pg_stat_all_tables
WHERE schemaname!='pg_catalog' AND schemaname!='pg_toast' AND n_dead_tup>0;
"""


class Command(BaseCommand):

    def handle(self, *args, **options):
        cursor = connection.cursor()
        cursor.execute(SQL)
        for r in cursor.fetchall():
            cursor.execute('VACUUM FULL "%s"."%s";' % (r[0], r[1]))
