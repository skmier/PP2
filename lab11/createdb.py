import psycopg2
from configlab11 import host, password, port, user

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE DATABASE LAB11PHONEBOOK"""
        )
        print("[INFO] DB created successfuly")
except Exception as _ex:
    print("[INFO] Error while working with psql:", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed.")



