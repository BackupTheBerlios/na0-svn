# Na0/Frontend/SCGIPrefork.py
# $Id$

"""SCGI frontend adapter
"""

__all__ = ['Na0SCGIHandler']
__docformat__ = 'epytext'

import sys
from scgi import scgi_server
from Na0.Frontend import Request

class Na0SCGIHandler(scgi_server.SCGIHandler):
    """SCGI handler class adapter for NaYeong"""

    def handle_connection(self, conn):
	"""Handles connections received from SCGI web server and
	processes a round.
        
        @param conn: connection object
        @type conn: connected socket instance
        """
        input = conn.makefile('r')
        output = conn.makefile('w')

        env = self.read_env(input)
        req = Request.CGIRequest(env, input.read(int(env['CONTENT_LENGTH'])))
        req.process(file=output)

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
