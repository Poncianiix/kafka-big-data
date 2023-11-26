import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(0,11,5))

# Cree un mensaje JSON
data = {'value1': 20}

# Publique el mensaje en el tópico `my_topic`
producer.send('test', json.dumps(data).encode('utf-8'))

# Espere a que el mensaje se envíe
producer.flush()


'''

kafka-topics --create --topic test --partitions 3 --replication-factor 3 --bootstrap-server localhost:9092

bash -c "seq 10 | kafka-console-producer --broker-list kafka1:29091,kafka2:29092,kafka3:29093 --topic test && echo 'Produced 10 messages.'"


kafka-console-consumer --bootstrap-server kafka1:29091,kafka2:29092,kafka3:29093 --topic test --from-beginning

'''