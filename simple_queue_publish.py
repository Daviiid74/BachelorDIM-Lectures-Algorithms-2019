# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:41:31 2019
simple_queue_publish.py
@author: martidav
"""
#import urlparse
import os
import pika
import config

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()
channel.queue_declare(queue='hello')

def send(msg):
    """
    Arg: une message de type string
    Permet d'envoyer un message sur CLOUDAMQP
    """
    channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=msg)
                              
    print(" [x] votre message est envoyer'")
        
    connection.close()   