# This program is used for managing expenses
import sqlite3


def init():
    # this function helps to initialize the expense manager
    try:
        conn = sqlite3.connect("expense_manager.db")
        print('DB connection established')
    except ConnectionError:
        print('DB connection failed')
    cursor = conn.cursor()    
    query = '''create table if not exists expenses_table(amount real, category text, description text, date text)'''
    cursor.execute(query)
    conn.commit()
    conn.close()

def log(amount, category, description=None):
    # this function logs the user entries to DB
    try:
        conn = sqlite3.connect("expense_manager.db")
        print('DB connection established')
    except ConnectionError:
        print('DB connection failed')
    from datetime import datetime
    now = datetime.now()
    date = now.strftime('%d/%m/%Y %H:%M:%S')
    cursor = conn.cursor()
    query = '''insert into expenses_table values(:amt, :cat, :desc, :date)'''
    cursor.execute(query, {"amt":amount, "cat": category, "desc": description, "date":date})
    conn.commit()
    conn.close()

def view():
    # this program displays the expenses
    try:
        conn = sqlite3.connect("expense_manager.db")
        print('DB connection established')
    except ConnectionError:
        print('DB connection failed')
    cursor = conn.cursor()
    query = '''select * from expenses_table'''
    result = cursor.execute(query)
    print(result.fetchall())
    conn.close()

# init()
log(16500, 'Bills', 'house rent')
view()
