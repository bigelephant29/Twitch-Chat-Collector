#!/usr/bin/python3

import sys
import socket
import configparser

def main():
  
  print('Twitch-Chat-Collector author:bigelephant29')

  if len(sys.argv) != 2:
    return print('Number of arguments error!')

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
  
  while True:
    print(sock.recv(1024).decode('utf-8'))

if __name__ == '__main__':
  main()
