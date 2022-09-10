while true
do
  bot=$(ps -ef | grep bot/app.py | awk '{print $2}')
  kill -9 $bot
  sleep 86400
done
