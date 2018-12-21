import MySQLdb

def db_init():
    print("Connecting to database...")
    db = MySQLdb.connect("35.232.58.223","root","Darius23!","mysql" )
    print("Connected!")
    return db

def db_destroy(db):
    db.close()

def db_query(db,q):
    cursor = db.cursor()
    try:
        cursor.execute(q)
        db.commit()
    except:
        db.rollback()
    return cursor.fetchone()

Database = None
global Database
def db_query(q):
    return db_query(Database,q)

Database = db_init()

print("DB version is %s" % db_query(Database,"SELECT VERSION()"))

db_destroy(Database)
