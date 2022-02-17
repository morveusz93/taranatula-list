import psycopg2
import os


DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


def connect(query):
    conn = None
    rows = None
    try:
        params = {
            'host': DB_HOST, 
            'database': DB_NAME, 
            'user': DB_USER, 
            'password': DB_PASSWORD}

        print('PARAMS: ', params)
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
            return rows


if __name__ == '__main__':
    connect()
