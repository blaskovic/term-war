#!/usr/bin/python2

#
# term-war
#
# Copyright (c) 2013
#
# Author Branislav Blaskovic <branislav@blaskovic.sk>
#

class MainGame:
    def __init__(self):
        self.playerA = Player('A')
        self.playerB = Player('B')

class Player:
    def __init__(self, side):
        self.side = side
        self.key = None

    def set_key(self, key):
        # Sets unique communicating key
        self.key = key
