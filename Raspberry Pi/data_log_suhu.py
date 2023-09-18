"""
 Create date program : Sabtu, 23 September 2023
"""

import Adafruit_DHT 
import time
import datetime
import telepot
from time import sleep
#from datetime import datetime 
from telepot.loop import MessageLoop 

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

now = datetime.datetime.now() 

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

def handle(msg):
    global command
    global chat_id
    
    chat_id = msg['chat']['id'] 
    command = msg['text']  
    
    print ('Received:'+ str(chat_id))
   
    if command == '/start':
        bot.sendMessage (chat_id, 'Selamat Datang')
    elif command == '/suhu':
        bot.sendMessage (chat_id, str(temperature))
    elif command == '/kelembapan':
        bot.sendMessage (chat_id, str(humidity))
     
#toke telegram bot    
bot = telepot.Bot('6634584328:AAGX-T6t8ONmKncAYECUjy1lwkeHqdir0kk')

bot.message_loop(handle)

def main():
    #print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
   
    file = open("/media/pi/1E9F-AC4C/log.csv","a")
    file.write(datetime.datetime.now().strftime('%Y-%m-%d'+"," '%H:%M:%S')+","+"{0:0.1f}".format(temperature)+","+"{0:0.1f}".format(humidity)+"\n")
    
    time.sleep(1)
    
    file.close()
    
while True:
    main() 

