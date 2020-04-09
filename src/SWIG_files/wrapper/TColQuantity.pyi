from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
TColQuantity_Array1OfLength = NewType('TColQuantity_Array1OfLength', Any)
#the following typedef cannot be wrapped as is
TColQuantity_Array2OfLength = NewType('TColQuantity_Array2OfLength', Any)

# harray1 classes
class TColQuantity_HArray1OfLength(TColQuantity_Array1OfLength, Standard_Transient): ...

# harray2 classes

class TColQuantity_HArray2OfLength(TColQuantity_Array2OfLength, Standard_Transient): ...

# harray2 classes

