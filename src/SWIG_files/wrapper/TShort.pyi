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

# harray1 classes
class TShort_HArray1OfShortReal(TShort_Array1OfShortReal, Standard_Transient): ...

# harray2 classes

class TShort_HArray2OfShortReal(TShort_Array2OfShortReal, Standard_Transient): ...

# harray2 classes

class TShort_HSequenceOfShortReal(TShort_SequenceOfShortReal, Standard_Transient): ...


