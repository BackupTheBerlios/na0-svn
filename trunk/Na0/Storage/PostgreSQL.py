# Na0/Storage/PostgreSQL.py
# $Id$

"""PostgreSQL Storage Backend
"""

__all__ = []
__docformat__ = 'epytext'

from Na0.Storage.Generic import GenericStorage
import psycopg

class PostgreSQLStorage(GenericStorage):
    """PostgreSQL Storage Backend Implementation"""

    def __init__(self, dsn, prefix='na0_'):
        """Initializes new PostgreSQL driver instance.

        @param dsn: DSN to connect
        @type dsn: str
        @param prefix: table prefix. specify if you are willing to
                       install multiple instances in a database.
        @type prefix: str
        """
        self.dsn = dsn
        self.prefix = prefix
        self.connection = None
        self.connect()

    def connect(self):
        """Connects to PostgreSQL server"""
        self.conn = psycopg.connect(self.dsn)

    def runQuery(self, *args, **kw):
        """Runs a postgre query with the current connection.

        @return: result data
        """
        curs = self.conn.cursor()
        try:
            curs.execute(*args, **kw)
            result = curs.dictfetchall()
            curs.close()
            self.conn.commit()
            return result
        except:
            self.conn.rollback()
            raise

if __name__ == '__main__':
    pg = PostgreSQLStorage('host=127.0.0.1 dbname=mt user=mt password=mt')
    print pg.runQuery('select * from mt_author')
