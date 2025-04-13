import psycopg2, csv
from config import host, user, password, db_name, port

def insert_data(name, phone_number):
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
            cursor.execute(
                "INSERT INTO PhoneBook (name, phone_number) VALUES (%s, %s);",
                (name, phone_number)
            )
            print("[INFO] Data added successfuly")
    except Exception as _ex:
        print("[INFO] Error while working with psql:", _ex)
    finally:
        if connection:
            connection.close()
user_name = input()
user_phone = input()

insert_data(user_name, user_phone)