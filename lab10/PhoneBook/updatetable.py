import csv, psycopg2
from  config import host, user, password, db_name, port

def update_name( phone_number, new_name):
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
                "UPDATE phonebook SET name = %s WHERE phone_number = %s;",
                (new_name,phone_number)
            )
        if cursor.rowcount > 0:
            print("[INFO] Name updated successfuly")
        else:
            print("[INFO] User with such name doesn`t exist")
    except Exception as _ex:
        print("[INFO] Error while working with psql:", _ex)
    finally:
        if connection:
            connection.close()

def update_phone(name, new_phone):
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
                "UPDATE phonebook SET phone_number = %s WHERE name = %s;",
                (new_phone,name)
            )
        if cursor.rowcount > 0:
            print("[INFO] Phone updated successfuly")
        else:
            print("[INFO] Phone with such name doesn`t exist")
    except Exception as _ex:
        print("[INFO] Error while working with psql:", _ex)
    finally:
        if connection:
            connection.close()

choice = input("What do u want to change?")
if choice == "name":
    current_phone = input().strip()
    new_name = input().strip()
    update_name(current_phone,new_name)
elif choice == "phone":
    current_name = input().strip()
    new_phone = input().strip()
    update_phone(current_name, new_phone)

