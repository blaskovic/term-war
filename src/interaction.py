#!/usr/bin/python2

#
# term-war
#
# Copyright (c) 2013
#
# Author Branislav Blaskovic <branislav@blaskovic.sk>
#

import sys
from decorations import Colors

Color = Colors()

class Writer:

    def __init__(self):
        pass

    def out(self, text, color=Color.ENDC, new_line=True):
        # Write some message to terminal in choosen color
        sys.stdout.write(color + text + Color.ENDC)
        if new_line:
            sys.stdout.write("\n")

writer = Writer()

class Prompt:
    def __init__(self):
        pass

    def ask(self, text, color=Color.ENDC):
        writer.out(text, color)
        return raw_input("> ")
