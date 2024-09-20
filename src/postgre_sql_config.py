import os
import psycopg2
from psycopg2 import DatabaseError

def connect_to_db():
    
    connection_params = {
        "host": os.environ.get('ofac_host'),
        "database": os.environ.get('ofac_database'),
        "user":  os.environ.get('ofac_user'),
        "password": os.environ.get('ofac_password'),
        "port": os.environ.get('ofac_port')
    }
    
    try:
        connection = psycopg2.connect(**connection_params)
        return connection
    
    except DatabaseError as db_error:
        print(f"Database error: {db_error}")
        return None
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None