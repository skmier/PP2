import psycopg2
from configsnake import host, user, password, db_name, port

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )

    with connection.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
);
        ''')

    

        connection.commit()
        print("[INFO] Tables created successfully")

except Exception as _ex:
    print("[ERROR] PostgreSQL error:", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed.")
