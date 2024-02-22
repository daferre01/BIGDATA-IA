from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['193.144.42.95:9093'])

# for i in range(10):
producer.send("bigdata", value={'BigData'})
# Como el envío es asíncrono, para que no se salga del programa antes de enviar el mensaje, esperamos 1 seg
time.sleep(1)
# producer.flush()