#!/usr/bin/env python
from rethinkdb import RqlDriverError
import sys

from app import App
import argparse
from constants import HELP


def run():
    parser = argparse.ArgumentParser(description='Command line key-value store.',
                                     add_help=False)
    parser.add_argument('strings', metavar='action', type=str, nargs='+',
                        help='action')

    args = parser.parse_args(args=['help'])
    try:
        application = App()
    except RqlDriverError as rde:
        sys.exit('''No running rethinkdb instance found\n'''
                 '''Kaboom expects a running rethinkdb instance\n'''
                 '''on localhost at default port''')
    proc = args.strings[0]
    # print 'Command: %s' % proc
    if not hasattr(application, proc):
        print "Command `%s` not found" % proc
    else:
        application.call(proc, *tuple(args.strings[1:]))


if __name__ == "__main__":
    run()
