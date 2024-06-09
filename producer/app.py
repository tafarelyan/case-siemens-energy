import json
import time
import uuid
from datetime import datetime

from kafka import KafkaProducer
from lorem_text import lorem

KAFKA_TOPIC = 'siemens_energy'
KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_message() -> dict:
    return {
        'id': str(uuid.uuid4()),
        'message': lorem.sentence(),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

if __name__ == '__main__':
    while True:
        message = generate_message()
        producer.send(KAFKA_TOPIC, value=message)
        # print(f'Messagem enviada do producer: {message}')
        time.sleep(1)