from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *

#the following typedef cannot be wrapped as is
TColStd_Array2OfBoolean = NewType('TColStd_Array2OfBoolean', Any)
#the following typedef cannot be wrapped as is
TColStd_Array2OfCharacter = NewType('TColStd_Array2OfCharacter', Any)
#the following typedef cannot be wrapped as is
TColStd_Array2OfInteger = NewType('TColStd_Array2OfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_Array2OfReal = NewType('TColStd_Array2OfReal', Any)
#the following typedef cannot be wrapped as is
TColStd_Array2OfTransient = NewType('TColStd_Array2OfTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapIteratorOfDataMapOfAsciiStringInteger = NewType('TColStd_DataMapIteratorOfDataMapOfAsciiStringInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapIteratorOfDataMapOfIntegerInteger = NewType('TColStd_DataMapIteratorOfDataMapOfIntegerInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapIteratorOfDataMapOfIntegerListOfInteger = NewType('TColStd_DataMapIteratorOfDataMapOfIntegerListOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapIteratorOfDataMapOfIntegerReal = NewType('TColStd_DataMapIteratorOfDataMapOfIntegerReal', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapIteratorOfDataMapOfIntegerTransient = NewType('TColStd_DataMapIteratorOfDataMapOfIntegerTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapIteratorOfDataMapOfStringInteger = NewType('TColStd_DataMapIteratorOfDataMapOfStringInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapIteratorOfDataMapOfTransientTransient = NewType('TColStd_DataMapIteratorOfDataMapOfTransientTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapOfAsciiStringInteger = NewType('TColStd_DataMapOfAsciiStringInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapOfIntegerInteger = NewType('TColStd_DataMapOfIntegerInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapOfIntegerListOfInteger = NewType('TColStd_DataMapOfIntegerListOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapOfIntegerReal = NewType('TColStd_DataMapOfIntegerReal', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapOfIntegerTransient = NewType('TColStd_DataMapOfIntegerTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapOfStringInteger = NewType('TColStd_DataMapOfStringInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_DataMapOfTransientTransient = NewType('TColStd_DataMapOfTransientTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_IndexedDataMapOfStringString = NewType('TColStd_IndexedDataMapOfStringString', Any)
#the following typedef cannot be wrapped as is
TColStd_IndexedDataMapOfTransientTransient = NewType('TColStd_IndexedDataMapOfTransientTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_IndexedMapOfInteger = NewType('TColStd_IndexedMapOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_IndexedMapOfReal = NewType('TColStd_IndexedMapOfReal', Any)
#the following typedef cannot be wrapped as is
TColStd_IndexedMapOfTransient = NewType('TColStd_IndexedMapOfTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_ListIteratorOfListOfAsciiString = NewType('TColStd_ListIteratorOfListOfAsciiString', Any)
#the following typedef cannot be wrapped as is
TColStd_ListIteratorOfListOfInteger = NewType('TColStd_ListIteratorOfListOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_ListIteratorOfListOfReal = NewType('TColStd_ListIteratorOfListOfReal', Any)
#the following typedef cannot be wrapped as is
TColStd_ListIteratorOfListOfTransient = NewType('TColStd_ListIteratorOfListOfTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_ListOfAsciiString = NewType('TColStd_ListOfAsciiString', Any)
#the following typedef cannot be wrapped as is
TColStd_ListOfInteger = NewType('TColStd_ListOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_ListOfReal = NewType('TColStd_ListOfReal', Any)
#the following typedef cannot be wrapped as is
TColStd_ListOfTransient = NewType('TColStd_ListOfTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_MapIntegerHasher = NewType('TColStd_MapIntegerHasher', Any)
#the following typedef cannot be wrapped as is
TColStd_MapIteratorOfMapOfAsciiString = NewType('TColStd_MapIteratorOfMapOfAsciiString', Any)
#the following typedef cannot be wrapped as is
TColStd_MapIteratorOfMapOfInteger = NewType('TColStd_MapIteratorOfMapOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_MapIteratorOfMapOfReal = NewType('TColStd_MapIteratorOfMapOfReal', Any)
#the following typedef cannot be wrapped as is
TColStd_MapIteratorOfMapOfTransient = NewType('TColStd_MapIteratorOfMapOfTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_MapIteratorOfPackedMapOfInteger = NewType('TColStd_MapIteratorOfPackedMapOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_MapOfAsciiString = NewType('TColStd_MapOfAsciiString', Any)
#the following typedef cannot be wrapped as is
TColStd_MapOfInteger = NewType('TColStd_MapOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_MapOfReal = NewType('TColStd_MapOfReal', Any)
#the following typedef cannot be wrapped as is
TColStd_MapOfTransient = NewType('TColStd_MapOfTransient', Any)
#the following typedef cannot be wrapped as is
TColStd_MapRealHasher = NewType('TColStd_MapRealHasher', Any)
#the following typedef cannot be wrapped as is
TColStd_MapTransientHasher = NewType('TColStd_MapTransientHasher', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfAddress = NewType('TColStd_SequenceOfAddress', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfAsciiString = NewType('TColStd_SequenceOfAsciiString', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfBoolean = NewType('TColStd_SequenceOfBoolean', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfExtendedString = NewType('TColStd_SequenceOfExtendedString', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfHAsciiString = NewType('TColStd_SequenceOfHAsciiString', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfHExtendedString = NewType('TColStd_SequenceOfHExtendedString', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfInteger = NewType('TColStd_SequenceOfInteger', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfReal = NewType('TColStd_SequenceOfReal', Any)
#the following typedef cannot be wrapped as is
TColStd_SequenceOfTransient = NewType('TColStd_SequenceOfTransient', Any)

class TColStd_Array1OfAsciiString:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> TCollection_AsciiString: ...
    def __setitem__(self, index: int, value: TCollection_AsciiString) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TCollection_AsciiString]:
    def next(self) -> TCollection_AsciiString: ...
    __next__ = next

class TColStd_Array1OfBoolean:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> bool: ...
    def __setitem__(self, index: int, value: bool) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[bool]:
    def next(self) -> bool: ...
    __next__ = next

class TColStd_Array1OfByte:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> str: ...
    def __setitem__(self, index: int, value: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]:
    def next(self) -> str: ...
    __next__ = next

class TColStd_Array1OfCharacter:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> str: ...
    def __setitem__(self, index: int, value: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]:
    def next(self) -> str: ...
    __next__ = next

class TColStd_Array1OfExtendedString:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> TCollection_ExtendedString: ...
    def __setitem__(self, index: int, value: TCollection_ExtendedString) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TCollection_ExtendedString]:
    def next(self) -> TCollection_ExtendedString: ...
    __next__ = next

class TColStd_Array1OfInteger:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> int: ...
    def __setitem__(self, index: int, value: int) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]:
    def next(self) -> int: ...
    __next__ = next

class TColStd_Array1OfListOfInteger:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> TColStd_ListOfInteger: ...
    def __setitem__(self, index: int, value: TColStd_ListOfInteger) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TColStd_ListOfInteger]:
    def next(self) -> TColStd_ListOfInteger: ...
    __next__ = next

class TColStd_Array1OfReal:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> float: ...
    def __setitem__(self, index: int, value: float) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[float]:
    def next(self) -> float: ...
    __next__ = next

class TColStd_Array1OfTransient:
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

class TColStd_HPackedMapOfInteger(Standard_Transient):
	@overload
	def __init__(self, NbBuckets: Optional[int]) -> None: ...
	@overload
	def __init__(self, theOther: TColStd_PackedMapOfInteger) -> None: ...
	def ChangeMap(self) -> TColStd_PackedMapOfInteger: ...
	def Map(self) -> TColStd_PackedMapOfInteger: ...

#classnotwrapped
class TColStd_PackedMapOfInteger: ...

# harray1 classes
class TColStd_HArray1OfExtendedString(TColStd_Array1OfExtendedString, Standard_Transient): ...

class TColStd_HArray1OfCharacter(TColStd_Array1OfCharacter, Standard_Transient): ...

class TColStd_HArray1OfBoolean(TColStd_Array1OfBoolean, Standard_Transient): ...

class TColStd_HArray1OfAsciiString(TColStd_Array1OfAsciiString, Standard_Transient): ...

class TColStd_HArray1OfReal(TColStd_Array1OfReal, Standard_Transient): ...

class TColStd_HArray1OfInteger(TColStd_Array1OfInteger, Standard_Transient): ...

class TColStd_HArray1OfListOfInteger(TColStd_Array1OfListOfInteger, Standard_Transient): ...

class TColStd_HArray1OfTransient(TColStd_Array1OfTransient, Standard_Transient): ...

class TColStd_HArray1OfByte(TColStd_Array1OfByte, Standard_Transient): ...

# harray2 classes

class TColStd_HArray2OfBoolean(TColStd_Array2OfBoolean, Standard_Transient): ...


class TColStd_HArray2OfTransient(TColStd_Array2OfTransient, Standard_Transient): ...


class TColStd_HArray2OfReal(TColStd_Array2OfReal, Standard_Transient): ...


class TColStd_HArray2OfInteger(TColStd_Array2OfInteger, Standard_Transient): ...


class TColStd_HArray2OfCharacter(TColStd_Array2OfCharacter, Standard_Transient): ...

# harray2 classes

class TColStd_HSequenceOfHAsciiString(TColStd_SequenceOfHAsciiString, Standard_Transient): ...


class TColStd_HSequenceOfTransient(TColStd_SequenceOfTransient, Standard_Transient): ...


class TColStd_HSequenceOfAsciiString(TColStd_SequenceOfAsciiString, Standard_Transient): ...


class TColStd_HSequenceOfHExtendedString(TColStd_SequenceOfHExtendedString, Standard_Transient): ...


class TColStd_HSequenceOfInteger(TColStd_SequenceOfInteger, Standard_Transient): ...


class TColStd_HSequenceOfExtendedString(TColStd_SequenceOfExtendedString, Standard_Transient): ...


class TColStd_HSequenceOfReal(TColStd_SequenceOfReal, Standard_Transient): ...


