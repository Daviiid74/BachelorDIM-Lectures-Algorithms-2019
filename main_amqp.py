# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:21:05 2019
main_amqp.py
@author: martidav
"""
import argparse
import simple_queue_publish
import simple_queue_read

#Choix d'envoyer un message ou de recevoir
parser = argparse.ArgumentParser(description='Envoyer un message (s) ou recevoir un message (r)')
parser.add_argument('commande')
parser.add_argument('msg')
args = parser.parse_args()

#Envoyer appeler la function send() dans simple_queue_publish
if args.commande == 's':
    simple_queue_publish.send(args.msg)
    print('envoyer', args.msg)
#Recevoir appeller la fonction read() dans simple_queue_read
if args.commande == 'r':
    simple_queue_read.read()
    print('recevoir')
