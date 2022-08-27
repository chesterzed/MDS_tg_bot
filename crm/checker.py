import os
import time
from work.models import User_tg, TaskConnect
from datetime import date


def user_leave_checker():
    print("start checking...")
    while True:
        users = User_tg.objects.all()
        today = date.today()
        for us in users:
            dat = us.last_in
            print(dat)
        time.sleep(86400)
