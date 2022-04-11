import sqlite3

def create_connection(db_file):

    db_connection = None
    
    try:
        db_connection = sqlite3.connect(db_file)
        return db_connection
    
    except sqlite3.Error as db_error:
        print(db_error)
    
    return db_connection


def create_table(db_connection, create_table_sql):
    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql)
    
    except sqlite3.Error as db_error:
        print(db_error)

def novi_ukucan(db_connection, ukucan):
    sq_query = ''' INSERT INTO Ukucani(ime, prezime, pin)
              VALUES(?, ?, ?) '''
    cursor = db_connection.cursor()
    cursor.execute(sq_query, ukucan)
    db_connection.commit()
    return cursor.lastrowid

def update_ukucana(db_connection, djelatnik):
    sql = ''' UPDATE Ukucani
              SET Ime = ? ,
                  Prezime = ?,
                  Pin = ?,
              WHERE id = ?'''
    cursor = db_connection.cursor()
    cursor.execute(sql, djelatnik)
    db_connection.commit()


# Metoda za brisanje zapisa o djelatniku u tabeli na osnovu ID broja retka
def obrisati_ukucana(db_connection, id):
    sql = 'DELETE FROM Ukucani WHERE id=?'
    cursor = db_connection.cursor()
    cursor.execute(sql, (id,))
    db_connection.commit()

def ocisti_tablicu(db_connection):
    sql = 'DELETE FROM Ukucani'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    db_connection.commit()


# Metoda za dohvat svih zapisa o djelatnicima
def select_all_employees(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Ukucani")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def select_employees_by_id(db_connection, id):

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Ukucani WHERE priority=?", (id,))


    rows = cursor.fetchall()

    for row in rows:
        print(row)