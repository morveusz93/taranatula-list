import psycopg2
from db_config import config


def connect(query):
    """ Connect to the PostgreSQL database server """
    conn = None
    rows = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            return rows


if __name__ == '__main__':
    connect()
