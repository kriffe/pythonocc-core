from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
TShort_Array1OfShortReal = NewType('TShort_Array1OfShortReal', Any)
#the following typedef cannot be wrapped as is
TShort_Array2OfShortReal = NewType('TShort_Array2OfShortReal', Any)
#the following typedef cannot be wrapped as is
TShort_SequenceOfShortReal = NewType('TShort_SequenceOfShortReal', Any)
