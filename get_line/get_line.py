#!/usr/bin/env python

"""fromstdin - Training and Testing Framework
Usage:  get_line.py <input> <line_since> <line_until>
get_line.py <input> <line>
get_line.py <input> [options]

Options:
    --since=<since>             Start at
    --until=<untile>            Finish at
    --line=<line>               exactly line

Read data from <input> file. Use "-" for reading from stdin.
"""

import sys
import select


def get_lines(text=None, line_number=None, line_since=None, line_until=None):
    buffer = []
    try:
        if text:
            if text[-1:] == "\n":
                text =  text[0:-1]
            text_buffer = text.split("\n")


        if line_number:
            line_number = int(line_number)
            assert line_number > 0

        if line_since:
            line_since = int(line_since)
            assert line_since > 0

        if line_until:
            line_until = int(line_until)
            if line_until > len(text_buffer):
                line_until = len(text_buffer)
            assert line_until >= line_since

        if isinstance(line_number, int)  and line_number <= len(text_buffer):
            buffer = text_buffer[line_number - 1:line_number]
        elif line_since > 0 and line_until <= len(text_buffer):
            buffer = text_buffer[line_since - 1:line_until]
    except:
        buffer = []
    return buffer

if __name__ == "__main__":

    if select.select([sys.stdin,],[],[],0.0)[0]:
        sys.argv.insert(1,'-')

    from docopt import docopt
    args = docopt(__doc__)

    f = f = sys.stdin if args['<input>'] == "-" else open(args['<input>'])
    line = args['<line>'] if '<line>' in args.keys() and args['<line>'] else args['--line']
    line_since = args['<line_since>'] if '<line_since>' in args.keys() and args['<line_since>'] else args['--since']
    line_until = args['<line_until>'] if '<line_until>' in args.keys() and args['<line_until>'] else args['--until']

    result = get_lines(text=f.read(), line_number=line, line_since=line_since, line_until=line_until)
    for l in result:
        print(l)
