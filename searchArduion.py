#!/usr/bin/python
# search Arduino

import serial

for com in range (0,4):
 try:
  PORT = '/dev/ttyACM'#str(com)
  BAUD = 9600
 



  board = serial.Serial(PORT,BAUD)
  print 'Arduino erkannt an /dev/ttyACM'+str(com)
  board.close()
  break
 except:
  print 'Kein Arduino an /dev/ttyACM'+str(com) 

