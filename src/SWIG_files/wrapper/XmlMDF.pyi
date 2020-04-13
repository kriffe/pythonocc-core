from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.XmlObjMgt import *
from OCC.Core.TCollection import *

#the following typedef cannot be wrapped as is
XmlMDF_DataMapIteratorOfMapOfDriver = NewType('XmlMDF_DataMapIteratorOfMapOfDriver', Any)
#the following typedef cannot be wrapped as is
XmlMDF_DataMapIteratorOfTypeADriverMap = NewType('XmlMDF_DataMapIteratorOfTypeADriverMap', Any)
#the following typedef cannot be wrapped as is
XmlMDF_MapOfDriver = NewType('XmlMDF_MapOfDriver', Any)
#the following typedef cannot be wrapped as is
XmlMDF_TypeADriverMap = NewType('XmlMDF_TypeADriverMap', Any)

class xmlmdf:
	@staticmethod
	def AddDrivers(self, aDriverTable: XmlMDF_ADriverTable, theMessageDriver: Message_Messenger) -> None: ...
	@overload
	@staticmethod
	def FromTo(self, aSource: TDF_Data, aTarget: XmlObjMgt_Element, aReloc: XmlObjMgt_SRelocationTable, aDrivers: XmlMDF_ADriverTable) -> None: ...
	@overload
	@staticmethod
	def FromTo(self, aSource: XmlObjMgt_Element, aTarget: TDF_Data, aReloc: XmlObjMgt_RRelocationTable, aDrivers: XmlMDF_ADriverTable) -> bool: ...

class XmlMDF_ADriver(Standard_Transient):
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, aSource: XmlObjMgt_Persistent, aTarget: TDF_Attribute, aRelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, aSource: TDF_Attribute, aTarget: XmlObjMgt_Persistent, aRelocTable: XmlObjMgt_SRelocationTable) -> None: ...
	def SourceType(self) -> Standard_Type: ...
	def TypeName(self) -> TCollection_AsciiString: ...
	def VersionNumber(self) -> int: ...

class XmlMDF_ADriverTable(Standard_Transient):
	def __init__(self) -> None: ...
	def AddDriver(self, anHDriver: XmlMDF_ADriver) -> None: ...
	def GetDriver(self, aType: Standard_Type, anHDriver: XmlMDF_ADriver) -> bool: ...
	def GetDrivers(self) -> XmlMDF_TypeADriverMap: ...

class XmlMDF_ReferenceDriver(XmlMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, Source: XmlObjMgt_Persistent, Target: TDF_Attribute, RelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, Source: TDF_Attribute, Target: XmlObjMgt_Persistent, RelocTable: XmlObjMgt_SRelocationTable) -> None: ...

class XmlMDF_TagSourceDriver(XmlMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, Source: XmlObjMgt_Persistent, Target: TDF_Attribute, RelocTable: XmlObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, Source: TDF_Attribute, Target: XmlObjMgt_Persistent, RelocTable: XmlObjMgt_SRelocationTable) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

xmlmdf_AddDrivers = xmlmdf.AddDrivers
xmlmdf_FromTo = xmlmdf.FromTo
xmlmdf_FromTo = xmlmdf.FromTo
