Twitch-Chat-Collector
====

This is a short project for collecting online chatroom message on Twitch channels.

+  First, you need an oAuth token from twitch. Please visit http://www.twitchapps.com/tmi/ to get one.

+  Second, run config.py and setup basic settings. This python script will create a new file 'config.ini' and save settings into it.

+  Finally, run listen.py with the following command format:
```
python3 listen.py <channel name>
```
The collected data will be stored in data/listen_result.txt

The current version supports only collecting messages. I'll try to add more features in the future.
