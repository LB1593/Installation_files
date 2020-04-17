#!/usr/bin/python3
# deleteTopic.py

## RICORDATI SEMPRE DI CHIUDERE IL CONSUMER PRIMA DI ELIMINARE UNA TOPIC!!!!!

## MA SE ELIMINI UNA TOPIC I DATI NON SONO PIù LEGGEBILI(però c'è un tool di ZK 
##che permete un rollback della topic che era fleggata)

from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError

print('\nSTART PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')

try:
    admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
except:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('A CLIENT ADMIN CONNECTION error occured.')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('')

topic_list = []
topic_name = "sports-event"
topic_list.append(topic_name)
   
try:
    admin_client.delete_topics(topic_list, timeout_ms=None)
    print('TOPIC: ' + topic_name + ' DELETED CORRECTLY ...')
    print('') 
except:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('A CLIENT DELETE TOPIC error occured.')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('')
  
print('END PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')
