bot=$(ps -ef | grep bot/app.py | awk '{print $2}')
crm=$(ps -ef | grep crm/manage.py | awk '{print $2}')
che=$(ps -ef | grep crm/checker.py | awk '{print $2}')
kill -9 $bot
kill -9 $crm
kill -9 $che
