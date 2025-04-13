import psycopg2,csv
from config import host, user, password, db_name, port



try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")

    #Create Table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE phonebook(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
            );"""
        )
        print("[INFO] Table created successfuly")

    


except Exception as _ex:
    print("[INFO] Error while working with psql:", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed.")
