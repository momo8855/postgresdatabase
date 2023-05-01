import psycopg2 as psy
from psycopg2.extras import RealDictCursor
from .config import settings

while True:
    try:
        conn = psy.connect(host=settings.database_hostname, database=settings.database_name, user=settings.database_username,
                           password=settings.database_password, port=settings.database_port, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection was Succesful")
        break
    except Exception as error:
        print("Connection to Database Field")
        print("Error: ", error)