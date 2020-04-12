from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TopLoc import *
from OCC.Core.Message import *
from OCC.Core.TopAbs import *
from OCC.Core.TCollection import *

#the following typedef cannot be wrapped as is
TopTools_Array2OfShape = NewType('TopTools_Array2OfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfIntegerListOfShape = NewType('TopTools_DataMapIteratorOfDataMapOfIntegerListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfIntegerShape = NewType('TopTools_DataMapIteratorOfDataMapOfIntegerShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfOrientedShapeInteger = NewType('TopTools_DataMapIteratorOfDataMapOfOrientedShapeInteger', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfOrientedShapeShape = NewType('TopTools_DataMapIteratorOfDataMapOfOrientedShapeShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeBox = NewType('TopTools_DataMapIteratorOfDataMapOfShapeBox', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeInteger = NewType('TopTools_DataMapIteratorOfDataMapOfShapeInteger', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeListOfInteger = NewType('TopTools_DataMapIteratorOfDataMapOfShapeListOfInteger', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeListOfShape = NewType('TopTools_DataMapIteratorOfDataMapOfShapeListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeReal = NewType('TopTools_DataMapIteratorOfDataMapOfShapeReal', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeSequenceOfShape = NewType('TopTools_DataMapIteratorOfDataMapOfShapeSequenceOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapIteratorOfDataMapOfShapeShape = NewType('TopTools_DataMapIteratorOfDataMapOfShapeShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfIntegerListOfShape = NewType('TopTools_DataMapOfIntegerListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfIntegerShape = NewType('TopTools_DataMapOfIntegerShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfOrientedShapeInteger = NewType('TopTools_DataMapOfOrientedShapeInteger', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfOrientedShapeShape = NewType('TopTools_DataMapOfOrientedShapeShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfShapeBox = NewType('TopTools_DataMapOfShapeBox', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfShapeInteger = NewType('TopTools_DataMapOfShapeInteger', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfShapeListOfInteger = NewType('TopTools_DataMapOfShapeListOfInteger', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfShapeListOfShape = NewType('TopTools_DataMapOfShapeListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfShapeReal = NewType('TopTools_DataMapOfShapeReal', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfShapeSequenceOfShape = NewType('TopTools_DataMapOfShapeSequenceOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_DataMapOfShapeShape = NewType('TopTools_DataMapOfShapeShape', Any)
#the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeAddress = NewType('TopTools_IndexedDataMapOfShapeAddress', Any)
#the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeListOfShape = NewType('TopTools_IndexedDataMapOfShapeListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeReal = NewType('TopTools_IndexedDataMapOfShapeReal', Any)
#the following typedef cannot be wrapped as is
TopTools_IndexedDataMapOfShapeShape = NewType('TopTools_IndexedDataMapOfShapeShape', Any)
#the following typedef cannot be wrapped as is
TopTools_IndexedMapOfOrientedShape = NewType('TopTools_IndexedMapOfOrientedShape', Any)
#the following typedef cannot be wrapped as is
TopTools_IndexedMapOfShape = NewType('TopTools_IndexedMapOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_ListIteratorOfListOfListOfShape = NewType('TopTools_ListIteratorOfListOfListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_ListIteratorOfListOfShape = NewType('TopTools_ListIteratorOfListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_ListOfListOfShape = NewType('TopTools_ListOfListOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_ListOfShape = NewType('TopTools_ListOfShape', Any)
TopTools_LocationSetPtr = NewType('TopTools_LocationSetPtr', TopTools_LocationSet)
#the following typedef cannot be wrapped as is
TopTools_MapIteratorOfMapOfOrientedShape = NewType('TopTools_MapIteratorOfMapOfOrientedShape', Any)
#the following typedef cannot be wrapped as is
TopTools_MapIteratorOfMapOfShape = NewType('TopTools_MapIteratorOfMapOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_MapOfOrientedShape = NewType('TopTools_MapOfOrientedShape', Any)
#the following typedef cannot be wrapped as is
TopTools_MapOfShape = NewType('TopTools_MapOfShape', Any)
#the following typedef cannot be wrapped as is
TopTools_SequenceOfShape = NewType('TopTools_SequenceOfShape', Any)

class TopTools_Array1OfListOfShape:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> TopTools_ListOfShape: ...
    def __setitem__(self, index: int, value: TopTools_ListOfShape) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TopTools_ListOfShape]: ...
    def next(self) -> TopTools_ListOfShape: ...
    __next__ = next

class TopTools_Array1OfShape:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> TopoDS_Shape: ...
    def __setitem__(self, index: int, value: TopoDS_Shape) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TopoDS_Shape]: ...
    def next(self) -> TopoDS_Shape: ...
    __next__ = next

class TopTools:
	@staticmethod
	def Dummy(self, I: int) -> None: ...

class TopTools_LocationSet:
	def __init__(self) -> None: ...
	def Add(self, L: TopLoc_Location) -> int: ...
	def Clear(self) -> None: ...
	def GetProgress(self) -> Message_ProgressIndicator: ...
	def Index(self, L: TopLoc_Location) -> int: ...
	def Location(self, I: int) -> TopLoc_Location: ...
	def SetProgress(self, PR: Message_ProgressIndicator) -> None: ...

class TopTools_MutexForShapeProvider:
	def __init__(self) -> None: ...
	def CreateMutexForShape(self, theShape: TopoDS_Shape) -> None: ...
	def CreateMutexesForSubShapes(self, theShape: TopoDS_Shape, theType: TopAbs_ShapeEnum) -> None: ...
	def GetMutex(self, theShape: TopoDS_Shape) -> Standard_Mutex: ...
	def RemoveAllMutexes(self) -> None: ...

class TopTools_OrientedShapeMapHasher:
	@staticmethod
	def HashCode(self, theShape: TopoDS_Shape, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...

class TopTools_ShapeMapHasher:
	@staticmethod
	def HashCode(self, theShape: TopoDS_Shape, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...

class TopTools_ShapeSet:
	def __init__(self) -> None: ...
	def Add(self, S: TopoDS_Shape) -> int: ...
	def AddGeometry(self, S: TopoDS_Shape) -> None: ...
	def AddShapes(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
	def ChangeLocations(self) -> TopTools_LocationSet: ...
	def Check(self, T: TopAbs_ShapeEnum, S: TopoDS_Shape) -> None: ...
	def Clear(self) -> None: ...
	@overload
	def DumpExtent(self, S: TCollection_AsciiString) -> None: ...
	def FormatNb(self) -> int: ...
	def GetProgress(self) -> Message_ProgressIndicator: ...
	def Index(self, S: TopoDS_Shape) -> int: ...
	def Locations(self) -> TopTools_LocationSet: ...
	def NbShapes(self) -> int: ...
	def SetFormatNb(self, theFormatNb: int) -> None: ...
	def SetProgress(self, PR: Message_ProgressIndicator) -> None: ...
	def Shape(self, I: int) -> TopoDS_Shape: ...

# harray1 classes

class TopTools_HArray1OfShape(TopTools_Array1OfShape, Standard_Transient):
    def TopTools_HArray1OfShape(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TopTools_Array1OfShape: ...


class TopTools_HArray1OfListOfShape(TopTools_Array1OfListOfShape, Standard_Transient):
    def TopTools_HArray1OfListOfShape(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TopTools_Array1OfListOfShape: ...

# harray2 classes

class TopTools_HArray2OfShape(TopTools_Array2OfShape, Standard_Transient):
    def TopTools_HArray2OfShape(self, theRowLow: int, theRowUpp: int, theColLow: int, theColUpp: int) -> None: ...
    def TopTools_HArray2OfShape(self, theOther: TopTools_Array2OfShape) -> None: ...
    def Array2(self) -> TopTools_Array2OfShape: ...

# hsequence classes

class TopTools_HSequenceOfShape(TopTools_SequenceOfShape, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: TopTools_SequenceOfShape) -> None: ...
    def Sequence(self) -> TopTools_SequenceOfShape: ...
    def Append(self, theSequence: TopTools_SequenceOfShape) -> None: ...


toptools_Dummy = toptools.Dummy
toptools_Dump = toptools.Dump
TopTools_OrientedShapeMapHasher_HashCode = TopTools_OrientedShapeMapHasher.HashCode
TopTools_OrientedShapeMapHasher_IsEqual = TopTools_OrientedShapeMapHasher.IsEqual
TopTools_ShapeMapHasher_HashCode = TopTools_ShapeMapHasher.HashCode
TopTools_ShapeMapHasher_IsEqual = TopTools_ShapeMapHasher.IsEqual
