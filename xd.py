import sqlite3

conn = sqlite3.connect('SQlite')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS biblioteka(
        id int PRIMARY KEY,
        wypozyczona boolean NOT NULL,
        tytuł varchar(50) NOT NULL,
        imie_autora varchar(25) NOT NULL,
        nazwisko_autora varchar(50) NOT NULL
    )
''')

def bookManagerAdd(wypozyczona, tytuł, imie_autora, nazwisko_autora):
    try:
        cursor.execute('''INSERT INTO biblioteka (wypozyczona, tytuł, imie_autora, nazwisko_autora) VALUES (?, ?, ?)''', (wypozyczona, tytuł, imie_autora, nazwisko_autora))
    except sqlite3.Error as e:
        print(f" Bład przy operacji: {e}")
    finally:
        if conn:
            conn.close

def bookManagerRemove(id):
    try:
        row = cursor.execute('''
        DELETE FROM biblioteka WHERE ID = ?''', id)
    except sqlite3.Error as e:
        print(f" Bład przy operacji: {e}")
    finally:
        if conn:
            conn.close

def bookManagerShowById(id):
    try:
        cursor.execute('''
        SELECT * FROM biblioteka
    ''')
        row = cursor.fetchall()

        for line in row:
            print(line)
    except sqlite3.Error as e:
        print(f" Bład przy operacji: {e}")
    finally:
        if conn:
            conn.close

def bookManagerUpdate(action, arg, id):
    conn = sqlite3.connect('SQlite')
    cursor = conn.cursor()

    if action == "wypozyczona" or "rented":
        try:
            cursor.execute('''
            UPDATE biblioteka (
                SET wypozyczona = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Bład przy operacji: {e}")
        finally:
            if conn:
                conn.close

    if action == "tytul" or "tytuł" or "title":
        try:
            cursor.execute('''
            UPDATE biblioteka (
                SET tytul = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Bład przy operacji: {e}")
        finally:
            if conn:
                conn.close

    if action == "imie_autora" or "author_name" or "imie":
        try:
            cursor.execute('''
            UPDATE biblioteka (
                SET imie_autora = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Bład przy operacji: {e}")
        finally:
            if conn:
                conn.close

    if action == "nazwisko_autora" or "author_surname":
        try:
            cursor.execute('''
            UPDATE uzytkownicy (
                SET biblioteka autora = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Bład przy operacji: {e}")
        finally:
            if conn:
                conn.close
