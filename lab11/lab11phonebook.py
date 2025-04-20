import psycopg2 
from configlab11 import password, user, host, port, db_name

connection = psycopg2.connect(password=password, user=user, host=host, port=port, database=db_name)
connection.autocommit = True

# 1

def search_by_pattern(pattern):
    try:
        with connection.cursor() as cursor:
            like_pattern = f"%{pattern}%"
            cursor.execute(
                '''SELECT * FROM phonebooklb11 WHERE name ILIKE %s OR phone_number ILIKE %s;''',
                (like_pattern, like_pattern)
            )
            result = cursor.fetchall()
            print(result)
    except Exception as ex:
        print("error", ex)


# My proceduere in psql for second task
# CREATE OR REPLACE PROCEDURE insert_or_update4(p_name VARCHAR, p_phone VARCHAR)
# AS $$
# BEGIN 
#     IF EXISTS (SELECT 1 FROM phonebooklb11 WHERE name = p_name) THEN 
#         UPDATE phonebooklb11 SET phone_number = p_phone WHERE name = p_name;
#     ELSE 
#         INSERT INTO phonebooklb11 (name, phone_number) VALUES (p_name, p_phone);
#     END IF;
# END;
# $$ LANGUAGE plpgsql;

# 2

def insert_or_update4(name, phone):
    try:
        with connection.cursor() as cursor:
            cursor.execute("CALL insert_or_update4(%s, %s)", (name, phone))

            cursor.execute("SELECT * FROM phonebooklb11 WHERE name = %s;", (name,))
            res = cursor.fetchall()
            print("result:", res)

    except Exception as ex:
        print("ERRORRRRR:", ex)


# 3

def insert_many_users(names, phones):
    invalid_data = []
    try:
        with connection.cursor() as cursor:
            for name, phone in zip(names, phones):
                if phone.isdigit():
                    cursor.execute("INSERT INTO phonebooklb11 (name, phone_number) VALUES (%s, %s);", (name, phone))
                else:
                    invalid_data.append((name, phone))
        print("Table uploaded")

    except Exception as ex:
        print("ERRRROOOR", ex)

    print("Invalid data:", invalid_data)


# 4

def query_with_pagination(limit, offset):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM phonebooklb11 LIMIT %s OFFSET %s;", (limit, offset))
            res = cursor.fetchall()
            print(res)
    except Exception as ex:
        print("EROOOOR", ex)


# 5
# Удаление по имени или номеру

def delete_by_name_phone(something):
    command = input("IF U WANT TO DELETE BY NAME ENTER 1 ELSE 2: ")
    try:
        with connection.cursor() as cursor:
            if command == '1':
                cursor.execute("DELETE FROM phonebooklb11 WHERE name = %s;", (something,))
                print("Deleted by name.")
            elif command == '2':
                cursor.execute("DELETE FROM phonebooklb11 WHERE phone_number = %s;", (something,))
                print("Deleted by phone number.")
            else:
                print("Invalid command.")
        connection.commit()
    except Exception as ex:
        print("ERROR:", ex)



command = input("What do u want to do?\n" \
                "1 - Search by pattern\n" \
                "2 - Insert or update\n" \
                "3 - Insert many users\n " \
                "4 - Query with pagination\n" \
                "5 - Delete by name or phone\n   " \
                "Enter number: ")

if command == "1":
    pattern = input("Enter pattern: ")
    search_by_pattern(pattern)
elif command == "2":
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    insert_or_update4(name, phone)
elif command == "3":
    names = list(map(str, input("Enter names: ").split()))
    phones = list(map(str, input("Enter phones: ").split()))
    insert_many_users(names, phones)
elif command == "4":
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    query_with_pagination(limit, offset)
elif command == "5":
    something = input("Enter name or phone to delete: ")
    delete_by_name_phone(something)


if connection:
    connection.close()
    print("connection closed")



