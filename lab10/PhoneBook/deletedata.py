import psycopg2
from  config import host, user, password, db_name, port

delete_name = """
    DELETE FROM phonebook WHERE id = %s;
"""

delete_phone = """
    DELETE FROM phonebook WHERE id = %s;
"""

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
    port=port
)

cursor = connection.cursor()

command = input("What information do u want to delete: ")
id = input("Enter the colume")

if command == "phone":
    cursor.execute(delete_phone,(id,))
if command == "name":
    cursor.execute(delete_name,(id,))

connection.commit()

cursor.close()
connection.close()