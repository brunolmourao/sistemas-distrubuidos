import pika
import time
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
temperature = 25
info = 'temperature'
while(True):
    message = f'Temperatura atual e {temperature}'
    channel.basic_publish(
        exchange='direct_logs', routing_key=info, body=message)
    print(f" {info} : Mandando menssagem : {message}")
    temperature = temperature + 1
    time.sleep(60)

connection.close()