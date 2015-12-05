#!/usr/bin/env python

""" Resize Window
Usage: resize_window.py <layout>

Options:
    --layout=<layout>           top, bottom, left, right

"""


import subprocess
import platform

from utils.window import Window




if __name__ == "__main__":

    from docopt import docopt
    args = docopt(__doc__)

    window = Window()
    window.resize_window(args['<layout>'])


