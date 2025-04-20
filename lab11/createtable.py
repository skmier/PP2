import psycopg2
from configlab11 import host, password, port, user, db_name


connection = None

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database = db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE phonebooklb11(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
            );
            """
        )
        print("[INFO] Table created successfuly")
except Exception as ex:
    print("[INFO] Error while working with psql:", ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed.")
