#!/usr/bin/env python

"""fromstdin - Training and Testing Framework
Usage:  get_line.py
get_line.py <site>
get_line.py <site> <user>

Options:
    --since=<since>             Start at
    --until=<untile>            Finish at
    --line=<line>               exactly line

Read data from <input> file. Use "-" for reading from stdin.
"""

credentials = [
    {'site': 's1', 'user': 'u1', 'pass': 'abc'},
    {'site': 's2', 'user': 'u2', 'pass': 'bcd'},
    ]

string_encoders = ['abc', 'bcd']


def encode(text):
    response = ''
    for c in text:
        candidates = []
        for se in string_encoders:
            if c in se:
                candidates.append(se)
        # print(candidates)
        # elegir un cadidato al azar
        try:
            encoder = candidates[0]
        except:
            print("ERROR no se puede codificar la clave")

        response += encoder[0]
        response += str(encoder.index(c))

    return response


if __name__ == "__main__":

    from docopt import docopt
    args = docopt(__doc__)

    # print(args)

    if not args['<site>']:
        print('sites')
        for c in credentials:
            print(c['site'])

    elif not args['<user>']:
        # filter credentials
        new_credentials = []
        for c in credentials:
            if c['site'] == args['<site>']:
                # new_credentials.append(c)
                print(c['user'])
        # print(new_credentials)
    else:
        new_credentials = []
        for c in credentials:
            if c['site'] == args['<site>'] and c['user'] == args['<user>']:
                print('paswd: ' + encode(c['pass']))



