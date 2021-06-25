#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('192.168.1.11',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello1')
def publish():
      channel.basic_publish(exchange='',
                            routing_key='hello',
                            body='Hello new message 2')
      #print(" [x] Sent 'Hello World!'")
      connection.close()
#stackoverflow.com/questions/27805086/how-to-connect-pika-to-rabbitmq-remote-server-python-pika
