import pika
import time
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
humidade = 10
info = 'humidade'
while(True):
    message = f'Humidade  atual e {humidade}%'
    channel.basic_publish(
        exchange='direct_logs', routing_key=info, body=message)
    print(f" {info} : Mandando menssagem : {message}")
    humidade = humidade + 1
    time.sleep(60)

connection.close()