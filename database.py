import  sqlite3

conn = sqlite3.connect('journal.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        city TEXT,
        temperature REAL,
        mood TEXT,
        note TEXT
    )
''')

def add_entry(date, city, temperature, mood, note):

    cursor.execute('INSERT INTO entries (date, city, temperature, mood, note) VALUES (?,?,?,?,?)',
                   (date, city, temperature, mood, note))
    conn.commit()
    print('Entry Added')

def get_all_entries():
    cursor.execute('SELECT * FROM entries')
    for row in cursor.fetchall():
        print(row)

def get_some_entries_city():
    try:
        target = input('input your city want to see: ')
        cursor.execute('SELECT * FROM entries WHERE city = ?', (target,))
        result = cursor.fetchall()
        if len(result) == 0:
            print('No entries found')
        else:
            for row in result:
             print(row)

    except sqlite3.Error:
         print('city not found')

def get_some_entries_date():
    try:
        target = input('input your date want to see (YYYY-MM-DD): ')
        cursor.execute('SELECT * FROM entries WHERE date = ?', (target,))
        result = cursor.fetchall()
        if len(result) == 0:
            print('No entries found')
        else:
            for row in result:
             print(row)

    except sqlite3.Error:
         print('date not found')

def delete_entry_by_date():
    target = input('input your date want to delete (YYYY-MM-DD):')
    cursor.execute('DELETE FROM entries WHERE date = ?', (target,))
    conn.commit()
    print('Entry Deleted')

def delete_entry_by_city():
    target = input('input your city want to delete (BKK):')
    cursor.execute('DELETE FROM entries WHERE city = ?', (target,))
    conn.commit()
    print('Entry Deleted')

