from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
TColQuantity_Array2OfLength = NewType('TColQuantity_Array2OfLength', Any)

class TColQuantity_Array1OfLength:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> Quantity_Length: ...
    def __setitem__(self, index: int, value: Quantity_Length) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Quantity_Length]:
    def next(self) -> Quantity_Length: ...
    __next__ = next

# harray1 classes
class TColQuantity_HArray1OfLength(TColQuantity_Array1OfLength, Standard_Transient): ...

# harray2 classes

class TColQuantity_HArray2OfLength(TColQuantity_Array2OfLength, Standard_Transient): ...

# harray2 classes

