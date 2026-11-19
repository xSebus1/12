import sqlite3

conn = sqlite3.connect('SQlite')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS uzytkownicy(
        id int PRIMARY KEY,
        imie varchar(20) NOT NULL,
        nazwisko varchar(50) NOT NULL,
        wiek int(2) NOT NULL
    )
''')

cursor.execute('''
INSERT INTO uzytkownicy (imie, nazwisko, wiek) VALUES (?, ?, ?)''', ('Jan', 'Kowalski', 12))

cursor.execute('''
    SELECT * FROM UZYTKOWNICY
''')
rows = cursor.fetchall();

for linia in rows:
    print(linia)

cursor.execute('''UPDATE uzytkownicy SET wiek = ? WHERE id = ?''', (10, 1))

cursor.execute('''
    DELETE FROM uzytkownicy WHERE id = ?
''', ('1'))

def managerAdd(name, surname, age):
    conn = sqlite3.connect('SQlite')
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO uzytkownicy (imie, nazwisko, wiek) VALUES (?, ?, ?)''', (name, surname, age))
    except sqlite3.Error as e:
        print(f" Bład przy operacji: {e}")
    finally:
        if conn:
            conn.close

def managerEdit(action, arg, id):
    conn = sqlite3.connect('SQlite')
    cursor = conn.cursor()

    if action == "wiek" or "age":
        try:
            cursor.execute('''
            UPDATE uzytkownicy (
                SET wiek = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Bład przy operacji: {e}")
        finally:
            if conn:
                conn.close

    if action == "imie" or "name":
        try:
            cursor.execute('''
            UPDATE uzytkownicy (
                SET imie = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Bład przy operacji: {e}")
        finally:
            if conn:
                conn.close

    if action == "nazwisko" or "nazwisko":
        try:
            cursor.execute('''
            UPDATE uzytkownicy (
                SET wiek = ? WHERE id = ?
            )''', (arg, id))
        except sqlite3.Error as e:
            print(f" Bład przy operacji: {e}")
        finally:
            if conn:
                conn.close

def managerShow(id):
    try:
        conn = sqlite3.connect('SQlite')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM uzytkownicy
    ''')
        row = cursor.fetchall()

        for line in row:
            print(line)
    except sqlite3.Error as e:
        print(f" Bład przy operacji: {e}")
    finally:
        if conn:
            conn.close

def managerDelete(id):
    try:
        conn = sqlite3.connect('SQlite')
        cursor = conn.cursor()

        row = cursor.execute('''
        DELETE FROM uzytkownicy WHERE ID = ?
    ''', id)
    except sqlite3.Error as e:
        print(f" Bład przy operacji: {e}")
    finally:
        if conn:
            conn.close

managerAdd('xxdxdd', 'grjgrigrgr', 12)
managerAdd('BDHHUB', 'hduyhAS', 76)
managerAdd('djihgdn', 'sut9uyg', 48)
managerAdd('kzsreghy8y', 'gusihg', 31)
managerShow(1)
managerShow(2)
managerShow(3)
managerShow(4)
