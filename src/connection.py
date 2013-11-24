#!/usr/bin/python2

#
# term-war
#
# Copyright (c) 2013
#
# Author Branislav Blaskovic <branislav@blaskovic.sk>
#

import socket
import SocketServer

#
# Config
#

BUFFER = 9999

#
# Client part
#

class ClientConnection:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

    def send(self, data):
        self.connect()
        self.sock.sendall(str(data))
        respond = self.receive()
        self.end()
        return respond

    def receive(self):
        return self.sock.recv(BUFFER)

    def end(self):
        self.sock.close()

#
# Server part
#

class ServerTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # Received data
        data = self.request.recv(BUFFER)
        print "{} wrote:".format(self.client_address[0])
        print data

        # What to do?
        argv = data.split(" ")
        action = argv[0]
        print 'Action: ' + str(action)

        # Just try to process connection
        try:
            if action == 'CHECK':
                self.send_back('ACK')
            elif action == 'SETKEY' and len(argv) == 3:
                action, key, player = argv
                if player not in ['A', 'B']:
                    self.send_back('You have to choose between A or B')
                else:
                    self.send_back('ACK')

        except:
            print 'ERROR in handle()'

        print '---'

    def send_back(self, data):
        self.request.sendall(data)

class ServerConnection:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        # Create the server, binding to localhost on port 9999
        server = SocketServer.TCPServer((self.ip, self.port), ServerTCPHandler)

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C 
        server.serve_forever()
