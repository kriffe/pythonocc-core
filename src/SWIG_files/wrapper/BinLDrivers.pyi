from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.BinMDF import *
from OCC.Core.TDocStd import *
from OCC.Core.TCollection import *
from OCC.Core.PCDM import *
from OCC.Core.CDM import *
from OCC.Core.Storage import *

#the following typedef cannot be wrapped as is
BinLDrivers_VectorOfDocumentSection = NewType('BinLDrivers_VectorOfDocumentSection', Any)

class BinLDrivers_Marker(IntEnum):
	BinLDrivers_ENDATTRLIST: int = ...
	BinLDrivers_ENDLABEL: int = ...
BinLDrivers_ENDATTRLIST = BinLDrivers_Marker.BinLDrivers_ENDATTRLIST
BinLDrivers_ENDLABEL = BinLDrivers_Marker.BinLDrivers_ENDLABEL

class binldrivers:
	@staticmethod
	def AttributeDrivers(self, MsgDrv: Message_Messenger) -> BinMDF_ADriverTable: ...
	@staticmethod
	def DefineFormat(self, theApp: TDocStd_Application) -> None: ...
	@staticmethod
	def Factory(self, theGUID: Standard_GUID) -> Standard_Transient: ...
	@staticmethod
	def StorageVersion(self) -> TCollection_AsciiString: ...

class BinLDrivers_DocumentRetrievalDriver(PCDM_RetrievalDriver):
	def __init__(self) -> None: ...
	def AttributeDrivers(self, theMsgDriver: Message_Messenger) -> BinMDF_ADriverTable: ...
	def CreateDocument(self) -> CDM_Document: ...
	@overload
	def Read(self, theFileName: TCollection_ExtendedString, theNewDocument: CDM_Document, theApplication: CDM_Application) -> None: ...

class BinLDrivers_DocumentSection:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theName: TCollection_AsciiString, isPostRead: bool) -> None: ...
	def IsPostRead(self) -> bool: ...
	def Length(self) -> False: ...
	def Name(self) -> TCollection_AsciiString: ...
	def Offset(self) -> False: ...

class BinLDrivers_DocumentStorageDriver(PCDM_StorageDriver):
	def __init__(self) -> None: ...
	def AddSection(self, theName: TCollection_AsciiString, isPostRead: Optional[bool]) -> None: ...
	def AttributeDrivers(self, theMsgDriver: Message_Messenger) -> BinMDF_ADriverTable: ...
	@overload
	def Write(self, theDocument: CDM_Document, theFileName: TCollection_ExtendedString) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

binldrivers_AttributeDrivers = binldrivers.AttributeDrivers
binldrivers_DefineFormat = binldrivers.DefineFormat
binldrivers_Factory = binldrivers.Factory
binldrivers_StorageVersion = binldrivers.StorageVersion
BinLDrivers_DocumentSection_ReadTOC = BinLDrivers_DocumentSection.ReadTOC
