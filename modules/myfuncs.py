from sqlite3 import Error
import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('sqlite3 version:', sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print('connected to', db_file)
            return conn
        else:
            print("Failed")
            

if __name__ == '__main__':
    pass