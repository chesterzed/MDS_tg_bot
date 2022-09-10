while true
do
  bot=$(ps -ef | grep bot/app.py | awk '{print $2}')
  kill -9 $bot
  echo $bot
  python3 bot/app.py &
  sleep 5
done
