import psycopg2, csv
from config import user, db_name, password, host, port

def inserting_from_csv(file):
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
            with open (file, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    name = row["name"]
                    phone_number = row['phone_number']
                    cursor.execute(
                        "INSERT INTO phonebook(name, phone_number) VALUES (%s,%s);",
                        (name, phone_number)
                    )
            print("[INFO] Data added successfuly")
    except Exception as _ex:
        print("[INFO] Error while working with psql:", _ex)
    finally:
        if connection:
            connection.close()

inserting_from_csv('lab10/PhoneBook/contacts.csv')
