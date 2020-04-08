from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

FSD_BStream = NewType('FSD_BStream', FILE)
#the following typedef cannot be wrapped as is
FSD_FStream = NewType('FSD_FStream', Any)

#classnotwrapped
class FSD_Base64Decoder:
	pass

#classnotwrapped
class FSD_File:
	pass

#classnotwrapped
class FSD_BinaryFile:
	pass

#classnotwrapped
class FSD_CmpFile:
	pass

#classnotwrapped
class FSD_FileHeader:
	pass
