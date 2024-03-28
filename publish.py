import pika
import json

def publish_channel(queue_name, message):
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)

    message_json = json.dumps(message)

    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message_json,
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))
    
    connection.close()