from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
Plugin_DataMapIteratorOfMapOfFunctions = NewType('Plugin_DataMapIteratorOfMapOfFunctions', Any)
#the following typedef cannot be wrapped as is
Plugin_MapOfFunctions = NewType('Plugin_MapOfFunctions', Any)

#classnotwrapped
class Plugin:
	pass
