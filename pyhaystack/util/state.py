# -*- coding: utf-8 -*-
"""
State machine interface.  This is a base class for implementing state machines.
"""

from .operation import HAVE_FUTURE, NotReadyError, BaseHaystackOperation
from .asyncexc import AsynchronousException


assert NotReadyError
assert BaseHaystackOperation


if HAVE_FUTURE == 'asyncio':
    from .awaitableop import HaystackOperation
else:
    class HaystackOperation(BaseHaystackOperation):
        pass
