from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.BinObjMgt import *
from OCC.Core.TCollection import *

#the following typedef cannot be wrapped as is
BinMDF_DataMapIteratorOfTypeADriverMap = NewType('BinMDF_DataMapIteratorOfTypeADriverMap', Any)
#the following typedef cannot be wrapped as is
BinMDF_DoubleMapIteratorOfTypeIdMap = NewType('BinMDF_DoubleMapIteratorOfTypeIdMap', Any)
BinMDF_StringIdMap = NewType('BinMDF_StringIdMap', TColStd_DataMapOfAsciiStringInteger)
#the following typedef cannot be wrapped as is
BinMDF_TypeADriverMap = NewType('BinMDF_TypeADriverMap', Any)
#the following typedef cannot be wrapped as is
BinMDF_TypeIdMap = NewType('BinMDF_TypeIdMap', Any)

class BinMDF:
	@staticmethod
	def AddDrivers(self, aDriverTable: BinMDF_ADriverTable, aMsgDrv: Message_Messenger) -> None: ...

class BinMDF_ADriver(Standard_Transient):
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, aSource: BinObjMgt_Persistent, aTarget: TDF_Attribute, aRelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, aSource: TDF_Attribute, aTarget: BinObjMgt_Persistent, aRelocTable: BinObjMgt_SRelocationTable) -> None: ...
	def SourceType(self) -> Standard_Type: ...
	def TypeName(self) -> TCollection_AsciiString: ...

class BinMDF_ADriverTable(Standard_Transient):
	def __init__(self) -> None: ...
	def AddDriver(self, theDriver: BinMDF_ADriver) -> None: ...
	@overload
	def AssignIds(self, theTypes: TColStd_IndexedMapOfTransient) -> None: ...
	@overload
	def AssignIds(self, theTypeNames: TColStd_SequenceOfAsciiString) -> None: ...
	@overload
	def GetDriver(self, theType: Standard_Type, theDriver: BinMDF_ADriver) -> int: ...
	@overload
	def GetDriver(self, theTypeId: int) -> BinMDF_ADriver: ...

class BinMDF_ReferenceDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDF_TagSourceDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

binmdf_AddDrivers = binmdf.AddDrivers
