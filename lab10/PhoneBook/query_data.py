import psycopg2,csv
from config import host, user, password, db_name, port

sellect_by_id = '''
    SELECT * FROM phonebook WHERE id = %s;
    '''
sellect_by_name = '''
    SELECT * FROM phonebook WHERE name = %s;
    '''
sellect_all = '''
    SELECT * FROM phonebook;
    '''

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
    port=port
)

cursor = connection.cursor()

com = input("What kind of query do u wnat to? ")

if com == "all":
    cursor.execute(sellect_all)
    print(cursor.fetchall())
elif com == "name":
    name = input()
    cursor.execute(sellect_by_name, (name,))
    print(cursor.fetchall())
elif com == "id":
    id = input()
    cursor.execute(sellect_by_id, (id,))
    print(cursor.fetchone())

connection.commit()

cursor.close()
connection.close()