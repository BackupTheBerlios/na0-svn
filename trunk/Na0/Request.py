# Na0/Request.py
# $Id$

"""Common request handler interface
"""

__all__ = ['Request', 'CGIRequest', 'process_request']
__docformat__ = 'epytext'

import os.path

class Request:
    """A base request class that handles data that is incoming via
    HTTP or HTTP-like protocols"""

    protocol = None         # CGI, SCGI, mod_python ..

    # HTTP Request Headers
    accept_charset = ''     # Accept-Charset
    accept_encoding = ''    # Accept-Encoding
    accept_language = ''    # Accept-Language
    host = ''               # Host
    user_agent = ''         # User-Agent

    # common variables
    remote_addr = ''        # client address
    request_uri = ''        # requested uri
    script_name = ''        # script path
    query = {}              # GET + POST variables


class CGIRequest(Request):
    """A request class for CGI-like protocols"""

    def __init__(self, env, file):
        """Initializes L{CGIRequest} class

        @param env: CGI environment variables
        @type env: dict
        @param content: content payload
        @type content: str
        """
        self.env = env
        self.file = file
        self.parse_env()

    def parse_env(self):
        """Converts environment variables to instance attributes"""
        env = self.env

        self.accept_charset = env.get('HTTP_ACCEPT_CHARSET', '')
        self.accept_encoding = env.get('HTTP_ACCEPT_ENCODING', '')
        self.accept_language = env.get('HTTP_ACCEPT_LANGUAGE', '')
        self.host = env.get('HTTP_HOST', '')
        self.user_agent = env.get('HTTP_USER_AGENT', '')

        self.remote_addr = env.get('REMOTE_ADDR', '')
        self.request_uri = env.get('REQUEST_URI', '')
        self.script_name = env.get('SCRIPT_NAME', '')

        import cgi
        self.query = dict(cgi.parse(self.file, self.env))


def fatal_error(file, message):
    file.write('Content-type: text/plain\r\n')
    file.write('\r\n')
    file.write('Fatal error: %s\r\n' % message)

def process_request(req, file):
    """Processes the requests

    @param req: request object
    @type req: instance of L{Request} or its subclasses
    @param file: file to output result
    @type file: file-like object
    """
    base_url = '/na0/' # XXX: to configuration
    if req.script_name.startswith(base_url):
        req.query['request_args'] = req.script_name[len(base_url):].split('/')
    else:
        fatal_error(file, 'base url not set')
        return

    from Na0 import Actions
    action = req.query.get('action', ['default'])[0]
    Actions.do_action(file, action, req)
