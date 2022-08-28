from mysql.connector import connect
import time
from datetime import date


def db_connect():
    try:
        return connect(  # DB connection
            host="5.23.53.158",
            user="gen_user",
            password="mgx37gvw66",
            db="default_db",
            port=3306
        )
    except:
        return False


def date_to_float(current_date):
    if type(current_date) == type(date.today()):
        return time.mktime(current_date.timetuple())
    else:
        return False


def get_table(connection, table):
    table_query = f"SELECT * FROM {table}"
    cursor = connection.cursor()
    cursor.execute(table_query)
    return cursor.fetchall()


def insert_to_tasks(connection, i_user_from, i_user, i_about, i_photo_path):
    table_query = f"""
    INSERT INTO work_taskconnect (user_from, user_to, about, photo_path) 
    VALUES ( %s, %s, %s, %s)"""

    cursor = connection.cursor()
    li = (i_user_from, i_user, str(i_about), str(i_photo_path))
    cursor.execute(table_query, li)
    connection.commit()


def user_leave_checker():
    print("start checking...")

    connection1 = db_connect()
    users = get_table(connection1, "work_users")
    today = date_to_float(date.today())  # how many day user left
    for row in users:
        print(row[1])
        if date_to_float(row[12]):
            days_passed = (today - date_to_float(row[12])) / 86400  # 86400 - 1 day in seconds
            print(days_passed)
        else:
            days_passed = 0

        if days_passed >= 3:
            insert_to_tasks(connection1, row[1], 0, "Бро, человек то с гнильцой оказался", '')

    connection1.commit()

    time.sleep(86400)  #  Ожидание 24 часа


user_leave_checker()
