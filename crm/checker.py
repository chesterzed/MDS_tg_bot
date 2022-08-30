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


def user_leave_checker(connection):
    print("start checking...")

    users = get_table(connection, "work_users")
    today = date_to_float(date.today())  # how many day user left
    for row in users:
        print(row[1])
        if date_to_float(row[12]):
            days_passed = (today - date_to_float(row[12])) / 86400  # 86400 - 1 day in seconds
            print(days_passed)
        else:
            days_passed = 0

        if days_passed >= 3:
            print(row)
            insert_to_tasks(connection, row[1], -1, f"Не заходил в бота {days_passed} дней", '')

    connection.commit()


def reg_users(connection):
    cm = 0
    au = 0
    users = get_table(connection, "work_users")
    stats = get_table(connection, "work_statistic")
    today = date_to_float(date.today())
    for u in users:
        cm += 1
        if date_to_float(u[12]) and (today - date_to_float(u[12])) / 86400 < 3:
            au += 1

    return cm, au


obj_months = {'January': 'Январь', 'February': 'Февраль', 'March': 'Март', 'April ': 'Апрель',
              'May': 'Май', 'June': 'Июнь', 'July': 'Июль', 'August': 'Август', 'September': 'Сентябрь',
              'October': 'Октябрь', 'November': 'Ноябрь', 'December': 'Декабрь'}

reg_last_month = 0
reg_current_month = 0
act_last_month = 0
act_current_month = 0

while True:
    con = db_connect()
    user_leave_checker(con)
    reg_current_month, act_current_month = reg_users(con)
    if reg_current_month == 1:
        pass
    # obj_months.get(date.today().strftime("%B"))

    time.sleep(86400)  #  Ожидание 24 часа
