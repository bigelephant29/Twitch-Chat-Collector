#!/usr/bin/python3

def main():

  print ('Twitch-Chat-Collector author:bigelephant29')

  print ('Configuration-Setting Tool')
  
  config_file = open('config.ini', 'w')
  
  if not config_file:
    return print ('Fail to open config.ini')

  data = ''

  data += '[SERVER]\n'
  twitch_servername = input ('Please Enter Server Name : ')

  if len(twitch_servername) == 0:
    print ('Use default server name : irc.chat.twitch.tv')
    twitch_servername = 'irc.chat.twitch.tv'
  
  data += 'twitch_servername : ' + twitch_servername + '\n'

  twitch_serverport = input ('Please Enter Port : ')
  
  if len(twitch_serverport) == 0:
    print ('Use default port : 6667')
    twitch_serverport = 6667
  else:
    twitch_serverport = int(twitch_serverport) 
  
  data += 'twitch_serverport : ' + str(twitch_serverport) + '\n'

  data += '[USER_INFO]\n'
  while True:
    twitch_username = input ('Please Enter Twitch User Name : ')
    if len(twitch_username) == 0:
      print ('Error : user name should not be empty')
    else:
      break
  data += 'twitch_username : ' + twitch_username + '\n'
  
  while True:
    twitch_oauth_token = input ('Please Enter Twitch oAuth Token : ')
    if len(twitch_oauth_token) == 0:
      print ('Error : oauth token should not be empty')
    elif not twitch_oauth_token.startswith('oauth:'):
      print ('Error : oauth token should begins with \"oauth:\"')
    else:
      break
  data += 'twitch_oauth_token : ' + twitch_oauth_token + '\n'
  
  config_file.write(data)
  print ('All data is saved into config.ini')

if __name__ == '__main__':
  main()
