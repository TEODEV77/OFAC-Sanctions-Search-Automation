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
    
def execute_query(query, params=(),action=None):
        connection = connect_to_db() 
        try:
            with connection.cursor() as cursor:
                if action == "select":
                    cursor.execute(query, params)
                    return cursor.fetchall()
                
                elif action == "insert":
                    cursor.execute(query, params)
                    connection.commit()
                
                elif action == "delete":
                    cursor.execute(query, params)
                    connection.commit()
                
                print("Query executed successfully.")
                
        except DatabaseError as db_error:
            print(f"Database error: {db_error}")
            connection.rollback()
            return None
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            connection.rollback()
            return None
        
def select(query, params=()):
    return execute_query(query,params,action="select")

def insert(query, params=()):
    execute_query(query,params,action="insert")
    
def delete(query, params=()):
    execute_query(query,params,action="delete")