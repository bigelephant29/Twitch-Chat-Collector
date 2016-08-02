#!/usr/bin/python3

import sys
import socket
import configparser
import re
import os

def main():
  
  print('Twitch-Chat-Collector author:bigelephant29')

  if len(sys.argv) != 2:
    return print('Usage: python3 listen.py <channel>')

  config = configparser.ConfigParser()
  config.read('config.ini')
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(30)

  servername = config['SERVER']['twitch_servername']
  port = int(config['SERVER']['twitch_serverport'])
  username = config['USER_INFO']['twitch_username']
  token = config['USER_INFO']['twitch_oauth_token']
  
  try:
    sock.connect((servername, port))
  except:
    return print('Connection Error')

  sock.settimeout(None)
  
  sock.send(('PASS %s\r\n' % token).encode('utf-8'))
  sock.send(('NICK %s\r\n' % username).encode('utf-8'))
  sock.send(('JOIN #%s\r\n' % sys.argv[1].lower()).encode('utf-8'))
  
  fileName = 'data/listen_result.txt'
  os.makedirs(os.path.dirname(fileName), exist_ok=True)

  with open(fileName, 'a') as myData:

    msgRe = re.compile('^:([a-zA-Z0-9_]+)\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.tmi\.twitch\.tv PRIVMSG #[a-zA-Z0-9_]+ :(.*)')
    pingRe = re.compile('^PING.*')

    while True:
      recvStr = sock.recv(1024).decode('utf-8')
      ping = pingRe.match(recvStr)
      if ping:
        sock.send(recvStr.replace('PING', 'PONG'))
        print(recvStr)
        continue
      result = msgRe.match(recvStr)
      if result:
        myData.write('%s : %s' % (result.group(1), result.group(2).replace('\r', '\n')))
        myData.flush()
      else:
        print(recvStr)

if __name__ == '__main__':
  main()
