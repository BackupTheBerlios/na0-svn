# Na0/Frontend/SCGIPrefork.py
# $Id$

"""SCGI frontend adapter
"""

__all__ = ['Na0SCGIHandler']
__docformat__ = 'epytext'

import sys
from scgi import scgi_server

class Na0SCGIHandler(scgi_server.SCGIHandler):

    def handle_connection(self, conn):
        input = conn.makefile("r")
        output = conn.makefile("w")

        env = self.read_env(input)
        output.write("Content-Type: text/plain\r\n")
        output.write("\r\n")
        for k, v in env.items():
            output.write("[%s] %r\n" % (k, v))

        output.close()
        input.close()
        conn.close()

def main():
    if len(sys.argv) == 2:
        port = int(sys.argv[1])
    else:
        port = 6942 # default port for Na0
    scgi_server.SCGIServer(Na0SCGIHandler, port=port).serve()

if __name__ == '__main__':
    main()
