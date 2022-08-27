bot=$(ps -ef | grep bot/app.py | awk '{print $2}')
crm=$(ps -ef | grep crm/manage.py | awk '{print $2}')
echo $(ps -ef | grep bot/app.py | awk '{print $2}')
kill $bot
kill $crm

git pull

python3 bot/app.py &
python3 crm/manage.py runserver 109.68.213.180:1000 &
