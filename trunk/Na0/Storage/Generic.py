# Na0/Storage/Generic.py
# $Id$

"""Generic Storage Backend (just for interface)
"""

__all__ = []
__docformat__ = 'epytext'

class GenericStorage:
    """Interface for Na Yeong backend drivers."""

    def __init__(self):
        """Initializes the storage class."""
        raise NotImplemented

    def connect(self):
        """Connects to storage."""
        raise NotImplemented
