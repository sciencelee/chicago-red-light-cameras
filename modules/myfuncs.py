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
            Parameters:
                c (cursor object): road segment list for intersection
                conn (connection object)
                table_name (str): name to use in db for TABLE    
    """
    sql = 'DELETE FROM {}'.format(table_name)
    #c = conn.cursor()
    c.execute(sql)
    conn.commit()
    

def sql_fetch_tables(c, conn):
    '''Return a list of all current tables in my db'''
    c.execute('SELECT name from sqlite_master where type= "table"')
    tables = c.fetchall()
    conn.commit()
    return tables



def make_table(df, table_name, c, conn):
    '''
    Create a new table in my db 
            Parameters:
                df (DataFrame): formatted df to create a table from
                table_name (str): name of table in db
                c : cursor object for sqlite3
                conn: connection object for sqlite3
    '''
    if table_name in sql_fetch_tables(c, conn):  # helper function in myfuncs
        delete_all_entries(c, conn, table_name) # in myfuncs
    
    df.to_sql(table_name, conn, if_exists='replace', index = False)    
    print(sql_fetch_tables(c, conn))  # print for verification
            

if __name__ == '__main__':
    pass