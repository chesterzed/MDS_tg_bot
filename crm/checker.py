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


def insert_to_stats(connection, i_month, i_year, i_reg_users, i_active_users, i_discard_users):
    table_query = f"""
    INSERT INTO work_statistic (month, year, reg_users, active_users, discard_users)
    VALUES ( %s, %s, %s, %s, %s, %s)"""

    cursor = connection.cursor()
    li = (str(i_month), str(i_year), str(i_reg_users), str(i_active_users), str(i_discard_users))
    cursor.execute(table_query, li)
    connection.commit()


def update_stats(connection, i_month, i_year, i_reg_users, i_active_users, i_discard_users):
    table_query = f"""
    UPDATE 
        work_statistic 
    SET
        reg_users = "%s", 
        active_users = "%s", 
        discard_users = "%s"
    WHERE 
        month = "%s" AND year = "%s";
    """ % (
        i_reg_users,
        i_active_users,
        i_discard_users,
        i_month,
        i_year
    )

    cursor = connection.cursor()
    li = (str(i_month), str(i_year), str(i_reg_users), str(i_active_users), str(i_discard_users))
    cursor.execute(table_query, li)
    connection.commit()


def user_leave_checker(connection, users):
    print("start checking...")

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


def reg_users(users, au_f):
    cm = 0
    au = 0
    today = date_to_float(date.today())
    for u in users:
        cm += 1
        if date_to_float(u[12]) and (today - date_to_float(u[12])) / 86400 < 3:
            au += 1
    if au_f > au:
        au = au_f

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
    usrs = get_table(con, "work_users")
    stats = get_table(con, "work_statistic")

    print(stats)

    for s in stats:
        if stats[-1][1] == s[1] and stats[-1][2] == s[2]:
            break
        reg_last_month += int(s.reg_users)

    act_last_month = int(stats[-2][3])
    act_current_month = int(stats[-1][4])
    reg_current_month = reg_last_month + int(stats[-1][3])

    user_leave_checker(con, usrs)
    if obj_months.get(date.today().strftime("%B")) != stats[-1][1]:  #  creating NEW
        reg_last_month = reg_current_month
        act_last_month = act_current_month
        act_current_month = 0
        insert_to_stats(
            con,
            obj_months.get(date.today().strftime("%B")),
            date.today().year,
            0,
            0,
            0
        )
        stats = get_table(con, "work_statistic")

    reg_current_month, act_current_month = reg_users(usrs, act_current_month)
    if obj_months.get(date.today().strftime("%B")) == stats[-1][1]:  #  daily update
        stats[-1][3] = reg_current_month
        stats[-1][4] = act_current_month
        update_stats(
            con,
            stats[-1][1],
            stats[-1][2],
            reg_current_month - reg_last_month,
            act_current_month,
            0
        )

    time.sleep(86400)  #  Ожидание 24 часа
