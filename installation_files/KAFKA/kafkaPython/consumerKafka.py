#!/usr/bin/python3
# consumerKafka.py

import sys

from kafka import KafkaConsumer
from kafka.errors import KafkaError

print('\nSTART PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')

try:
    consumerRun = KafkaConsumer('sports-event', bootstrap_servers='localhost:9092')                              
    print('CONSUMER waiting for ...')
    print('press CTRL-C to stop ...')
    print('')
except:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('A CONSUMER CONNECTION error occured.')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('')

try:
    for message in consumerRun:
        print('---------------------------------------------------------')
        print(message)
        print('')
except KeyboardInterrupt:
        print(' PROGRAM STOPPED <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        print('')
        sys.exit()

print('END PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')
