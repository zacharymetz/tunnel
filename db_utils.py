import sqlite3

def check_db_integrety():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create the tables if they arent there 
    c.execute("""
    CREATE TABLE IF NOT EXISTS endpoints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text not null,
        user text not null,
        host text not null,
        port int nul null,
        keyfile text not null
    );

    
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS ports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        endpoint int references endpoints(id) not null,
        name text not null,
        local int not null,
        remote int not null,
        target text not null,
        update_required boolean default true

    );
    """)
    conn.close()
    pass


def insert_data(sql,params):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create table
    c.execute(sql,params)
    conn.commit()
    conn.close()
    pass 

def get_data(sql,params):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(sql, params)
    result = c.fetchall()
    return result

