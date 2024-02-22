from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'register_user_two_partitions',
        bootstrap_servers=['localhost:9094'],
        auto_offset_reset='earliest', # Consuming from starting message.
        group_id='consumer_group_A'
    )

    print('Starting the consumer.')
    for msg in consumer:
        print('Registered user: {}'.format(json.loads(msg.value)))