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


def update_user_last_in(user_tg_id):
    try:
        query = f"""UPDATE work_users SET last_in = "{date.today()}" WHERE tg_id = "{user_tg_id}" """
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except:
        pass
