#!/usr/binn
# -*- codi as logng: utf-8 -*-
"""
markdown_editor.app
=================
markdown editor application file
"""
from __future__ import absolute_import, unicode_literals

import sys
import logging as log

from PySide.QtCore import *
from PySide.QtGui import *
from ui import ControlMainWindow


def main():
    app = QApplication(sys.argv)

    # Create and init the main window from the ui package
    win = ControlMainWindow()
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    try:
        main()
    except:
        log.exception("Error in main")
