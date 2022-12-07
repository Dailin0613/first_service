import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    try:
        return psycopg2.connect(
            database = "postgres",
            user = "postgres",
            password = "root",
            host = "localhost",
            port = "5432"
        )
    except DatabaseError as ex:
        raise ex