# Na0/Scripts/na0d.py
# $Id: Template.py 17 2004-09-07 16:09:27Z perky $

"""Launcher command line interface for daemon type frontends
"""

__all__ = []
__docformat__ = 'epytext'

import sys, os

def parse_options():
    """Parses command line options

    @return: parsed option and arguments
    @rtype: tuple that contains (options, args)
    """
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-c", "--config", dest="configfile", default='na0.ini',
                      help="configuration to read", metavar="FILE")
    parser.add_option("-f", "--foreground",
                      action="store_false", dest="daemonize", default=True,
                      help="don't go background")

    return parser.parse_args()

def parse_config(cfgfile):
    """Parses basic configuration file.

    The configuration file will have only few bits that can't be changed
    while a daemon is running. (eg. internal encoding and backend storage
    setup)

    @return: config instance with parsed configurations set.
    @rtype: L{Config} object
    """
    from ConfigParser import ConfigParser

    parser = ConfigParser()
    parser.read(cfgfile)
    # TODO: do some parse stuff

def main():
    """Runs main block of `na0d'.
    """
    (options, args) = parse_options()
    parse_config(options.configfile)
    # TODO: do rest of initializations
