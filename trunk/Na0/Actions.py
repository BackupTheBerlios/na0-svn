# Na0/Actions.py
# $Id$

"""Common request handler interface
"""

__all__ = ['do_action']
__docformat__ = 'epytext'

def do_action(file, action, req):
    """Run action handler for specified action and request variables

    @param file: file to write output
    @type file: file-like object
    @param action: action name to run
    @type action: str
    @param req: request object
    @type req: L{Request} instance
    """
    handler = globals().get('_run_' + action.lower())
    if not handler:
        raise ValueError, 'Unknown action specified'

    handler(file, req)

def _run_default(file, req):
    """Handler function for ``default'' action.

    @param file: file to write output
    @type file: file-like object
    @param req: request object
    @type req: L{Request} instance
    """
    file.write('Content-type: text/plain\r\n')
    file.write('\r\n')
    file.write('hahaaMERRER')
