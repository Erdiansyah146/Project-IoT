""" Create date program : Sabtu, 23 September 2023 """

import Adafruit_DHT 
import time
import telepot
from time import sleep
from datetime import datetime 
from telepot.loop import MessageLoop 

dht_sensor = Adafruit_DHT.DHT11
dht_pin = 4

kelembapan, suhu = Adafruit_DHT.read_retry(dht_sensor, dht_pin)

def handle(msg):
    global command
    global chat_id
    
    chat_id = msg['chat']['id'] 
    command = msg['text']  
    
    print ('Received:'+ str(chat_id))
   
    if command == '/start':
        bot.sendMessage (chat_id, 'Selamat Datang')
    elif command == '/suhu':
        bot.sendMessage (chat_id, str(suhu))
    elif command == '/kelembapan':
        bot.sendMessage (chat_id, str(kelembapan))
     
#toke telegram bot    
bot = telepot.Bot('isikan token bot telegram')
bot.message_loop(handle)

def main():
    wkatu_sekarang.datetime()
    #print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(suhu, kelembapan))
   
    file = open("/media/pi/1E9F-AC4C/log.csv","a")
    file.write(waktu_sekarang.strftime('%Y-%m-%d'+"," '%H:%M:%S')+","+"{0:0.1f}".format(suhu)+","+"{0:0.1f}".format(kelembapan)+"\n")
    file.close()
 
    time.sleep(1)
    
while True:
    main() 

