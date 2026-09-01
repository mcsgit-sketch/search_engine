import sqlite3 

database = "webpages.db"

def create_db():
    # initializing SQL database 
    con = sqlite3.connect(database)
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS 
                webpages(
                id INTEGER AUTOCREMENT PRIMARY KEY,
                url TEXT UNIQUE,
                title TEXT, 
                text TEXT)""")
    
    con.commit()
    con.close()

def store_page(url, title, text): 
    con = sqlite3.connect(database)
    cur = con.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO webpages
    (url, title, text)
    VALUES (?, ?, ?) 
    """, 
    (url, title, text)
                )
    
    con.commit()
    con.close()


