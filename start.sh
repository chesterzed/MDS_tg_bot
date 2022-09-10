bot=$(ps -ef | grep bot/app.py | awk '{print $2}')
b_starter=$(ps -ef | grep start_bot.sh | awk '{print $2}')
crm=$(ps -ef | grep crm/manage.py | awk '{print $2}')
checker=$(ps -ef | grep crm/checker.py | awk '{print $2}')
kill -9 $bot
kill -9 $crm
kill -9 $checker
kill -9 $b_starter

git pull

python3 crm/manage.py runserver 109.68.213.180:1000 &
python3 crm/checker.py &
sh start_bot.sh &
