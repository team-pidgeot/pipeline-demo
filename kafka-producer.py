from kafka import KafkaProducer
from kafka.errors import KafkaError
producer = KafkaProducer(bootstrap_servers=['34.217.221.173:9092'])
future = producer.send('test', b'Hello hello hello')
#producer.send('test', key=b'message-two', value=b'Helo hello hello')

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    log.exception()
    pass
