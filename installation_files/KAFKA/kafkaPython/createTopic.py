#!/usr/bin/python3
# createTopic.py

# importo i moduli che mi servono per la comunicazione in Kafka
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError

print('\nSTART PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')

# cerca una connessione al localhost:9092
try:
    admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
except:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('A CLIENT ADMIN CONNECTION error occured.')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('')

# mi sono creto una lista dove poter aggiungere le TOPIC e poi inviare tutto serialmente
topic_list = []
topic_name = "sports-event"
topic_list.append(NewTopic(name=topic_name, num_partitions=1, replication_factor=1))

# creo le topic
try:
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    print('TOPIC: ' + topic_name + ' CREATED CORRECTLY ...')
    print('')
except:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('A CLIENT CREATE TOPIC error occured.')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('')

print('END PROGRAM <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
print('')

###da terminale :


#### KAFKA LIST TOPICS

## qua chiedo i TOPICS ma sulla shell KAFKA

##sudo /usr/local/kafka/kafka_2.13-2.4.0/bin/kafka-topics.sh --zookeeper localhost:2181 --list   
