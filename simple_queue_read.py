# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:42:55 2019
simple_queue_read.py
@author: martidav
"""

#import urlparse
import os
import pika
import config

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()
channel.queue_declare(queue='hello')

def read():
    """
    Permet de lire les messages en attente sur CLOUDAMQP
    """
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,                          
                          auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

#test
#read()
 
"""
Compteur de messages
"""