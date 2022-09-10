bot=$(ps -ef | grep bot/app.py | awk '{print $2}')
crm=$(ps -ef | grep crm/manage.py | awk '{print $2}')
checker=$(ps -ef | grep crm/checker.py | awk '{print $2}')
kill -9 $bot
kill -9 $crm
kill -9 $checker

git pull

./start_bot.sh
python3 crm/manage.py runserver 109.68.213.180:1000 &
python3 crm/checker.py &
