import json
import time
import uuid
from datetime import datetime

from kafka import KafkaProducer
from lorem_text import lorem

def get_kafka_producer(bootstrap_servers, max_retries=5, delay=5) -> KafkaProducer:
    for _ in range(max_retries):
        try:
            return KafkaProducer(
                bootstrap_servers=bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        except Exception as e:
            print(f'Conexão falhou: {e}')
            time.sleep(delay)
    else:
        raise Exception('Não deu pra conectar com o Kafka depois de várias tentativas')


def generate_message() -> dict:
    return {
        'id': str(uuid.uuid4()),
        'message': lorem.sentence(),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }


if __name__ == '__main__':
    kafka_topic = 'siemens_energy'
    kafka_bootstrap_servers = ['kafka:9092']

    producer = get_kafka_producer(bootstrap_servers=kafka_bootstrap_servers)

    while True:
        message = generate_message()
        producer.send(kafka_topic, value=message)
        # print(f'Messagem enviada do produtor: {message}')
        time.sleep(1)