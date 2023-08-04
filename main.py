from picozero import RGBLED
from time import sleep

rgb = RGBLED(red = 13, green = 14, blue = 15, active_high=False)

rgb.color = (255, 0, 0)

import network
import socket
import time

port=3131
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSWD')

while(wlan.isconnected() == False):
    time.sleep(1)

ip = wlan.ifconfig()[0]
print(ip)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
s.bind((ip,port))
print('waiting....')
rgb.color = (0, 255, 0)
while True:
    data,addr=s.recvfrom(1024)
    s.sendto(data,addr)
    
    s_data = data.decode('utf-8')
    s_data_splitted = s_data.split(',')
    rv = int(s_data_splitted[0])
    gv = int(s_data_splitted[1])
    bv = int(s_data_splitted[2])
    
    rgb.color = (rv, gv, bv)
