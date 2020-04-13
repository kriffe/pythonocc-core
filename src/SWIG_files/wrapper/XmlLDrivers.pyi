from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Message import *
from OCC.Core.XmlMDF import *
from OCC.Core.TCollection import *
from OCC.Core.TDocStd import *
from OCC.Core.PCDM import *
from OCC.Core.CDM import *
from OCC.Core.Storage import *

#the following typedef cannot be wrapped as is
XmlLDrivers_SequenceOfNamespaceDef = NewType('XmlLDrivers_SequenceOfNamespaceDef', Any)

class xmlldrivers:
	@staticmethod
	def AttributeDrivers(theMsgDriver: Message_Messenger) -> XmlMDF_ADriverTable: ...
	@staticmethod
	def CreationDate() -> TCollection_AsciiString: ...
	@staticmethod
	def DefineFormat(theApp: TDocStd_Application) -> None: ...
	@staticmethod
	def Factory(theGUID: Standard_GUID) -> Standard_Transient: ...
	@staticmethod
	def StorageVersion() -> int: ...

class XmlLDrivers_DocumentRetrievalDriver(PCDM_RetrievalDriver):
	def __init__(self) -> None: ...
	def AttributeDrivers(self, theMsgDriver: Message_Messenger) -> XmlMDF_ADriverTable: ...
	def CreateDocument(self) -> CDM_Document: ...
	@overload
	def Read(self, theFileName: TCollection_ExtendedString, theNewDocument: CDM_Document, theApplication: CDM_Application) -> None: ...

class XmlLDrivers_DocumentStorageDriver(PCDM_StorageDriver):
	def __init__(self, theCopyright: TCollection_ExtendedString) -> None: ...
	def AttributeDrivers(self, theMsgDriver: Message_Messenger) -> XmlMDF_ADriverTable: ...
	@overload
	def Write(self, theDocument: CDM_Document, theFileName: TCollection_ExtendedString) -> None: ...

class XmlLDrivers_NamespaceDef:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, thePrefix: TCollection_AsciiString, theURI: TCollection_AsciiString) -> None: ...
	def Prefix(self) -> TCollection_AsciiString: ...
	def URI(self) -> TCollection_AsciiString: ...

# harray1 classes
# harray2 classes
# hsequence classes

xmlldrivers_AttributeDrivers = xmlldrivers.AttributeDrivers
xmlldrivers_CreationDate = xmlldrivers.CreationDate
xmlldrivers_DefineFormat = xmlldrivers.DefineFormat
xmlldrivers_Factory = xmlldrivers.Factory
xmlldrivers_StorageVersion = xmlldrivers.StorageVersion
