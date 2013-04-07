#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
input.key_presses
"""
from __future__ import absolute_import, unicode_literals

import os
from PySide.QtCore import Qt as qt


class KeyHandler:
    """
    This class is designed to contain a QWidget instance and hang onto
    its key events.
    """
    def __init__(self):
        self.win = None

    def wire(self, window):
        self.win = window
        self.win.key_down = self.keyPressed

    def keyPressed(self, *args):
        print "str(args)"
