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
            
def delete_all_entries(c, conn, table_name):
    """
    Delete all rows in table
    :param conn: Connection to the SQLite database
    :param table_name: str name of table
    :return:
    """
    sql = 'DELETE FROM {}'.format(table_name)
    #c = conn.cursor()
    c.execute(sql)
    conn.commit()

def sql_fetch_tables(c, conn):
    c.execute('SELECT name from sqlite_master where type= "table"')
    tables = c.fetchall()
    conn.commit()
    return tables
            

if __name__ == '__main__':
    pass