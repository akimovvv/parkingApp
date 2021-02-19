import sqlite3

conn = sqlite3.connect("parking.db")
cursor = conn.cursor()

def start(start_time):
    cursor.execute("""INSERT INTO tickets(start, status_id) VALUES (?,?);""", (start_time, 1,))
    conn.commit()
    return cursor.lastrowid

def end(ticket_id, end_time):
    try:
        cursor.execute("""UPDATE tickets SET end = (?) WHERE id = (?);""", (end_time, ticket_id))
        conn.commit()
    except Exception as ex:
        print(ex)

def show_start(ticket_id):
    try:
        cursor.execute("""SELECT start FROM tickets WHERE id = (?);""", (ticket_id,))
        return cursor.fetchone()
    except Exception as ex:
        print(ex)


def show_end(ticket_id):
    try:
        cursor.execute("""SELECT end FROM tickets WHERE id = (?);""", (ticket_id,))
        return cursor.fetchone()
    except Exception as ex:
        print(ex)

def sum(ticket_id, sum):
    try:
        cursor.execute("""UPDATE tickets SET price = (?), status_id = (?) WHERE id = (?);""", (sum, 2, ticket_id,))
        conn.commit()
    except Exception as ex:
        print(ex)
def check_status(ticket_id):
    cursor.execute("""SELECT status_id FROM tickets WHERE id = (?);""", (ticket_id,))
    a = cursor.fetchone()
    return a[0]

def show_all(ticket_id):
    cursor.execute("""SELECT t.start, t.end, t.price, s.status_info FROM tickets t JOIN statuses s on t.status_id = s.id WHERE t.id = (?);""", (ticket_id,))
    return cursor.fetchall()
def close():
    conn.close()