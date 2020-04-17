#!/usr/bin/python3
# producerKafka.py

from time import sleep
from json import dumps

import time
from datetime import date

import random

import sys
import logging

from kafka import KafkaProducer
from kafka.errors import KafkaError

print('\nSTART PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')

try:
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             retries=0, acks="all", batch_size=16384, buffer_memory=33554432, linger_ms=0)
except:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('A PRODUCER CONNECTION error occured.')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('')

myyear  = date.today().year
mymonth = date.today().month
myday   = date.today().day

myCreationDate = str(myyear) + '-' + str(mymonth).zfill(2) + '-' + str(myday).zfill(2)

mynames    = ['football','soccer', 'basket', 'baseball', 'volley']

myfootball = [ ['Arizona', 'Baltimore'], ['Atlanta', 'Buffalo'], ['Carolina', 'Chicago'], ['Cincinnati', 'Dallas'], ['Cleveland', 'Denver'] ]
mysoccer   = [ ['Columbus', 'Montreal'], ['Orlando', 'New England'], ['New York CIty', 'Philadelphia'], ['Colorado', 'Los Angeles'], ['Minnesota', 'Portland'] ]
mybasket   = [ ['Boston', 'Indiana'], ['Broklyn', 'Phoenix'], ['Milwaukee', 'Oklahoma'], ['Houston', 'Memphis'], ['New Orleans', 'San Antonio'] ]
mybaseball = [ ['Oregon', 'Kentucky'], ['Arkansas', 'Florida'], ['Stanford', 'Ohio'], ['Jacksonville', 'Georgia'], ['Missouri', 'Tennessee'] ]
myvolley   = [ ['Florida', 'Washington'], ['Michigan', 'Texas'], ['Denver', 'San Bernardino'], ['Alabama', 'Illinois'], ['Alaska', 'Washburn'] ]

mychannels = [ ['NBC', 'CBS'], ['ABC', 'Fox'], ['The CW', 'PBS'], ['FNX', 'ABC'], ['BBC', 'UKTV'] ]

# ---------------------------------------------------------------------------
# set how many times you wanto to repeat the main cicle (25 messages)
# times = myend - mybegin
## from begin to end mi permette di generare se il consumer si legge tutto ciò che arriva
# relativ al topic sempre, oppure solo quello che arriva ad ogni invio.



# if (myend - mybegin = 1) then the cicle is run once (25 messages generated)
mybegin  = 0
myend    = 1
# ---------------------------------------------------------------------------
# set mystart as a first valid key to generate
# first run: mystart = 0
mystart  = 0
# ---------------------------------------------------------------------------

myrange  = 1
myfinish = mystart + myrange

myteams = [ ]

for m in range (mybegin, myend):

    for n in range (0, 5):
    
        if n == 0:
            myteams = myfootball
        elif n == 1:
            myteams = mysoccer       
        elif n == 2:
            myteams = mybasket       
        elif n == 3:
            myteams = mybaseball      
        elif n == 4:
            myteams = myvolley       
        else:
            myteams = [ ]

        j = 0
                
        for id in range(mystart, myfinish):
         
            mystring1 = time.ctime()
            mysplit1  = mystring1.split()
        
            time.sleep(1)
        
            mystring2 = time.ctime()
            mysplit2  = mystring2.split()
        
            myStartTime           = mysplit1[3]
            mysuspendAt           = random.choice(range(150))
            myexternalUID         = random.choice(range(100))
            myclassSortRef        = random.choice(range(25))
            mysportsEventTypeRef  = random.choice(range(50))
            mydisplayOrder        = random.choice(range(75))
            myactualStartTime     = mysplit2[3] 
            sportsEventMeetingRef = random.choice(range(125))
      
            data = {
                'creationDate': myCreationDate
                ,'name': mynames[n]
                ,'startTime': myStartTime
                ,'suspendAt': mysuspendAt
                ,'externalUID': myexternalUID
                ,'classSortRef': myclassSortRef
                ,'sportsEventTypeRef': mysportsEventTypeRef
                ,'teams': myteams[j]
                ,'channels': mychannels[j]
                ,'displayOrder': mydisplayOrder
                ,'actualStartTime': myactualStartTime
                ,'sportsEventMeetingRef': sportsEventMeetingRef 
            }

            print('---------------------------------------------------------')
            print('key='+str(id)+';  '+'value='+str(data)) 
            print('')

            mykey = bytes(str(id), 'utf-8')
            mymess = bytes(str(data), 'utf-8')

            try:
                producer.send('sports-event', key=mykey, value=mymess)
            except:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('A PRODUCER SEND error occured.')
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('')
            j = j + 1
        
            time.sleep(1)
    
        mystart  = myfinish
        myfinish = myfinish + myrange

try:
    producer.close()
except:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('A PRODUCER CLOSE error occured.')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('')

print('END PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')
