import pika
import time
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
luminosidade = 10
info = 'luminosidade'
while(True):
    message = f'Luminosidade atual e {luminosidade} lux'
    channel.basic_publish(
        exchange='direct_logs', routing_key=info, body=message)
    print(f" {info} : Mandando menssagem : {message}")
    luminosidade = luminosidade + 1
    time.sleep(60)

connection.close()