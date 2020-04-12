from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *

#the following typedef cannot be wrapped as is
TColGeom_Array2OfBezierSurface = NewType('TColGeom_Array2OfBezierSurface', Any)
#the following typedef cannot be wrapped as is
TColGeom_Array2OfSurface = NewType('TColGeom_Array2OfSurface', Any)
#the following typedef cannot be wrapped as is
TColGeom_SequenceOfBoundedCurve = NewType('TColGeom_SequenceOfBoundedCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom_SequenceOfCurve = NewType('TColGeom_SequenceOfCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom_SequenceOfSurface = NewType('TColGeom_SequenceOfSurface', Any)

class TColGeom_Array1OfBSplineCurve:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]:
    def next(self) -> False: ...
    __next__ = next

class TColGeom_Array1OfBezierCurve:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]:
    def next(self) -> False: ...
    __next__ = next

class TColGeom_Array1OfCurve:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]:
    def next(self) -> False: ...
    __next__ = next

class TColGeom_Array1OfSurface:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]:
    def next(self) -> False: ...
    __next__ = next

# harray1 classes
class TColGeom_HArray1OfSurface(TColGeom_Array1OfSurface, Standard_Transient): ...

class TColGeom_HArray1OfBezierCurve(TColGeom_Array1OfBezierCurve, Standard_Transient): ...

class TColGeom_HArray1OfBSplineCurve(TColGeom_Array1OfBSplineCurve, Standard_Transient): ...

class TColGeom_HArray1OfCurve(TColGeom_Array1OfCurve, Standard_Transient): ...

# harray2 classes

class TColGeom_HArray2OfSurface(TColGeom_Array2OfSurface, Standard_Transient): ...

# harray2 classes

class TColGeom_HSequenceOfBoundedCurve(TColGeom_SequenceOfBoundedCurve, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: TColGeom_SequenceOfBoundedCurve) -> None: ...
    def Sequence(self) -> TColGeom_SequenceOfBoundedCurve: ...
    def Append(self, theSequence: TColGeom_SequenceOfBoundedCurve) -> None: ...


class TColGeom_HSequenceOfCurve(TColGeom_SequenceOfCurve, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: TColGeom_SequenceOfCurve) -> None: ...
    def Sequence(self) -> TColGeom_SequenceOfCurve: ...
    def Append(self, theSequence: TColGeom_SequenceOfCurve) -> None: ...


