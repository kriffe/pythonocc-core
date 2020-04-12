from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
TShort_Array2OfShortReal = NewType('TShort_Array2OfShortReal', Any)
#the following typedef cannot be wrapped as is
TShort_SequenceOfShortReal = NewType('TShort_SequenceOfShortReal', Any)

class TShort_Array1OfShortReal:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> Standard_ShortReal: ...
    def __setitem__(self, index: int, value: Standard_ShortReal) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Standard_ShortReal]: ...
    def next(self) -> Standard_ShortReal: ...
    __next__ = next

# harray1 classes

class TShort_HArray1OfShortReal(TShort_Array1OfShortReal, Standard_Transient):
    def TShort_HArray1OfShortReal(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TShort_Array1OfShortReal: ...

# harray2 classes

class TShort_HArray2OfShortReal(TShort_Array2OfShortReal, Standard_Transient):
    def TShort_HArray2OfShortReal(self, theRowLow: int, theRowUpp: int, theColLow: int, theColUpp: int) -> None: ...
    def TShort_HArray2OfShortReal(self, theOther: TShort_Array2OfShortReal) -> None: ...
    def Array2(self) -> TShort_Array2OfShortReal: ...

# hsequence classes

class TShort_HSequenceOfShortReal(TShort_SequenceOfShortReal, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: TShort_SequenceOfShortReal) -> None: ...
    def Sequence(self) -> TShort_SequenceOfShortReal: ...
    def Append(self, theSequence: TShort_SequenceOfShortReal) -> None: ...


