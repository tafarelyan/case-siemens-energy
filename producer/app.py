import json
import time
import uuid
from datetime import datetime

from kafka import KafkaProducer
from lorem_text import lorem

MAX_RETRIES = 5
DELAY = 5
KAFKA_TOPIC = 'siemens_energy'
KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'

for _ in range(MAX_RETRIES):
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        break
    except Exception as e:
        print(f'Conexão falhou: {e}')
        time.sleep(DELAY)
else:
    raise Exception('Não deu pra conectar com o Kafka depois de várias tentativas')

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