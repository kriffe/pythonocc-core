from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Storage import *
from OCC.Core.TCollection import *
from OCC.Core.Message import *
from OCC.Core.TColStd import *
from OCC.Core.CDM import *

PCDM_BaseDriverPointer = NewType('PCDM_BaseDriverPointer', Storage_BaseDriver)
#the following typedef cannot be wrapped as is
PCDM_SequenceOfDocument = NewType('PCDM_SequenceOfDocument', Any)
#the following typedef cannot be wrapped as is
PCDM_SequenceOfReference = NewType('PCDM_SequenceOfReference', Any)

class PCDM_StoreStatus(IntEnum):
	PCDM_SS_OK: int = ...
	PCDM_SS_DriverFailure: int = ...
	PCDM_SS_WriteFailure: int = ...
	PCDM_SS_Failure: int = ...
	PCDM_SS_Doc_IsNull: int = ...
	PCDM_SS_No_Obj: int = ...
	PCDM_SS_Info_Section_Error: int = ...
PCDM_SS_OK = PCDM_StoreStatus.PCDM_SS_OK
PCDM_SS_DriverFailure = PCDM_StoreStatus.PCDM_SS_DriverFailure
PCDM_SS_WriteFailure = PCDM_StoreStatus.PCDM_SS_WriteFailure
PCDM_SS_Failure = PCDM_StoreStatus.PCDM_SS_Failure
PCDM_SS_Doc_IsNull = PCDM_StoreStatus.PCDM_SS_Doc_IsNull
PCDM_SS_No_Obj = PCDM_StoreStatus.PCDM_SS_No_Obj
PCDM_SS_Info_Section_Error = PCDM_StoreStatus.PCDM_SS_Info_Section_Error

class PCDM_TypeOfFileDriver(IntEnum):
	PCDM_TOFD_File: int = ...
	PCDM_TOFD_CmpFile: int = ...
	PCDM_TOFD_XmlFile: int = ...
	PCDM_TOFD_Unknown: int = ...
PCDM_TOFD_File = PCDM_TypeOfFileDriver.PCDM_TOFD_File
PCDM_TOFD_CmpFile = PCDM_TypeOfFileDriver.PCDM_TOFD_CmpFile
PCDM_TOFD_XmlFile = PCDM_TypeOfFileDriver.PCDM_TOFD_XmlFile
PCDM_TOFD_Unknown = PCDM_TypeOfFileDriver.PCDM_TOFD_Unknown

class PCDM_ReaderStatus(IntEnum):
	PCDM_RS_OK: int = ...
	PCDM_RS_NoDriver: int = ...
	PCDM_RS_UnknownFileDriver: int = ...
	PCDM_RS_OpenError: int = ...
	PCDM_RS_NoVersion: int = ...
	PCDM_RS_NoSchema: int = ...
	PCDM_RS_NoDocument: int = ...
	PCDM_RS_ExtensionFailure: int = ...
	PCDM_RS_WrongStreamMode: int = ...
	PCDM_RS_FormatFailure: int = ...
	PCDM_RS_TypeFailure: int = ...
	PCDM_RS_TypeNotFoundInSchema: int = ...
	PCDM_RS_UnrecognizedFileFormat: int = ...
	PCDM_RS_MakeFailure: int = ...
	PCDM_RS_PermissionDenied: int = ...
	PCDM_RS_DriverFailure: int = ...
	PCDM_RS_AlreadyRetrievedAndModified: int = ...
	PCDM_RS_AlreadyRetrieved: int = ...
	PCDM_RS_UnknownDocument: int = ...
	PCDM_RS_WrongResource: int = ...
	PCDM_RS_ReaderException: int = ...
	PCDM_RS_NoModel: int = ...
PCDM_RS_OK = PCDM_ReaderStatus.PCDM_RS_OK
PCDM_RS_NoDriver = PCDM_ReaderStatus.PCDM_RS_NoDriver
PCDM_RS_UnknownFileDriver = PCDM_ReaderStatus.PCDM_RS_UnknownFileDriver
PCDM_RS_OpenError = PCDM_ReaderStatus.PCDM_RS_OpenError
PCDM_RS_NoVersion = PCDM_ReaderStatus.PCDM_RS_NoVersion
PCDM_RS_NoSchema = PCDM_ReaderStatus.PCDM_RS_NoSchema
PCDM_RS_NoDocument = PCDM_ReaderStatus.PCDM_RS_NoDocument
PCDM_RS_ExtensionFailure = PCDM_ReaderStatus.PCDM_RS_ExtensionFailure
PCDM_RS_WrongStreamMode = PCDM_ReaderStatus.PCDM_RS_WrongStreamMode
PCDM_RS_FormatFailure = PCDM_ReaderStatus.PCDM_RS_FormatFailure
PCDM_RS_TypeFailure = PCDM_ReaderStatus.PCDM_RS_TypeFailure
PCDM_RS_TypeNotFoundInSchema = PCDM_ReaderStatus.PCDM_RS_TypeNotFoundInSchema
PCDM_RS_UnrecognizedFileFormat = PCDM_ReaderStatus.PCDM_RS_UnrecognizedFileFormat
PCDM_RS_MakeFailure = PCDM_ReaderStatus.PCDM_RS_MakeFailure
PCDM_RS_PermissionDenied = PCDM_ReaderStatus.PCDM_RS_PermissionDenied
PCDM_RS_DriverFailure = PCDM_ReaderStatus.PCDM_RS_DriverFailure
PCDM_RS_AlreadyRetrievedAndModified = PCDM_ReaderStatus.PCDM_RS_AlreadyRetrievedAndModified
PCDM_RS_AlreadyRetrieved = PCDM_ReaderStatus.PCDM_RS_AlreadyRetrieved
PCDM_RS_UnknownDocument = PCDM_ReaderStatus.PCDM_RS_UnknownDocument
PCDM_RS_WrongResource = PCDM_ReaderStatus.PCDM_RS_WrongResource
PCDM_RS_ReaderException = PCDM_ReaderStatus.PCDM_RS_ReaderException
PCDM_RS_NoModel = PCDM_ReaderStatus.PCDM_RS_NoModel

class PCDM:
	@overload
	@staticmethod
	def FileDriverType(self, aFileName: TCollection_AsciiString, aBaseDriver: PCDM_BaseDriverPointer) -> PCDM_TypeOfFileDriver: ...

class PCDM_ReadWriter(Standard_Transient):
	@overload
	@staticmethod
	def FileFormat(self, aFileName: TCollection_ExtendedString) -> TCollection_ExtendedString: ...
	@staticmethod
	def Open(self, aDriver: Storage_BaseDriver, aFileName: TCollection_ExtendedString, anOpenMode: Storage_OpenMode) -> None: ...
	def ReadDocumentVersion(self, aFileName: TCollection_ExtendedString, theMsgDriver: Message_Messenger) -> int: ...
	def ReadExtensions(self, aFileName: TCollection_ExtendedString, theExtensions: TColStd_SequenceOfExtendedString, theMsgDriver: Message_Messenger) -> None: ...
	def ReadReferenceCounter(self, theFileName: TCollection_ExtendedString, theMsgDriver: Message_Messenger) -> int: ...
	def ReadReferences(self, aFileName: TCollection_ExtendedString, theReferences: PCDM_SequenceOfReference, theMsgDriver: Message_Messenger) -> None: ...
	@staticmethod
	def Reader(self, aFileName: TCollection_ExtendedString) -> PCDM_ReadWriter: ...
	def Version(self) -> TCollection_AsciiString: ...
	def WriteExtensions(self, aData: Storage_Data, aDocument: CDM_Document) -> None: ...
	@staticmethod
	def WriteFileFormat(self, aData: Storage_Data, aDocument: CDM_Document) -> None: ...
	def WriteReferenceCounter(self, aData: Storage_Data, aDocument: CDM_Document) -> None: ...
	def WriteReferences(self, aData: Storage_Data, aDocument: CDM_Document, theReferencerFileName: TCollection_ExtendedString) -> None: ...
	def WriteVersion(self, aData: Storage_Data, aDocument: CDM_Document) -> None: ...
	@staticmethod
	def Writer(self) -> PCDM_ReadWriter: ...

class PCDM_Reader(Standard_Transient):
	def CreateDocument(self) -> CDM_Document: ...
	def GetStatus(self) -> PCDM_ReaderStatus: ...
	@overload
	def Read(self, aFileName: TCollection_ExtendedString, aNewDocument: CDM_Document, anApplication: CDM_Application) -> None: ...

class PCDM_Reference:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aReferenceIdentifier: int, aFileName: TCollection_ExtendedString, aDocumentVersion: int) -> None: ...
	def DocumentVersion(self) -> int: ...
	def FileName(self) -> TCollection_ExtendedString: ...
	def ReferenceIdentifier(self) -> int: ...

class PCDM_ReferenceIterator(Standard_Transient):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def Init(self, aMetaData: CDM_MetaData) -> None: ...
	def LoadReferences(self, aDocument: CDM_Document, aMetaData: CDM_MetaData, anApplication: CDM_Application, UseStorageConfiguration: bool) -> None: ...

class PCDM_Writer(Standard_Transient):
	@overload
	def Write(self, aDocument: CDM_Document, aFileName: TCollection_ExtendedString) -> None: ...

class PCDM_ReadWriter_1(PCDM_ReadWriter):
	def __init__(self) -> None: ...
	def ReadDocumentVersion(self, aFileName: TCollection_ExtendedString, theMsgDriver: Message_Messenger) -> int: ...
	def ReadExtensions(self, aFileName: TCollection_ExtendedString, theExtensions: TColStd_SequenceOfExtendedString, theMsgDriver: Message_Messenger) -> None: ...
	def ReadReferenceCounter(self, aFileName: TCollection_ExtendedString, theMsgDriver: Message_Messenger) -> int: ...
	def ReadReferences(self, aFileName: TCollection_ExtendedString, theReferences: PCDM_SequenceOfReference, theMsgDriver: Message_Messenger) -> None: ...
	def Version(self) -> TCollection_AsciiString: ...
	def WriteExtensions(self, aData: Storage_Data, aDocument: CDM_Document) -> None: ...
	def WriteReferenceCounter(self, aData: Storage_Data, aDocument: CDM_Document) -> None: ...
	def WriteReferences(self, aData: Storage_Data, aDocument: CDM_Document, theReferencerFileName: TCollection_ExtendedString) -> None: ...
	def WriteVersion(self, aData: Storage_Data, aDocument: CDM_Document) -> None: ...

class PCDM_RetrievalDriver(PCDM_Reader):
	@staticmethod
	def DocumentVersion(self, theFileName: TCollection_ExtendedString, theMsgDriver: Message_Messenger) -> int: ...
	def GetFormat(self) -> TCollection_ExtendedString: ...
	@staticmethod
	def ReferenceCounter(self, theFileName: TCollection_ExtendedString, theMsgDriver: Message_Messenger) -> int: ...
	def SetFormat(self, aformat: TCollection_ExtendedString) -> None: ...

class PCDM_StorageDriver(PCDM_Writer):
	def GetFormat(self) -> TCollection_ExtendedString: ...
	def GetStoreStatus(self) -> PCDM_StoreStatus: ...
	def IsError(self) -> bool: ...
	@overload
	def Make(self, aDocument: CDM_Document) -> PCDM_Document: ...
	@overload
	def Make(self, aDocument: CDM_Document, Documents: PCDM_SequenceOfDocument) -> None: ...
	def SetFormat(self, aformat: TCollection_ExtendedString) -> None: ...
	def SetIsError(self, theIsError: bool) -> None: ...
	def SetStoreStatus(self, theStoreStatus: PCDM_StoreStatus) -> None: ...
	@overload
	def Write(self, aDocument: CDM_Document, aFileName: TCollection_ExtendedString) -> None: ...

#classnotwrapped
class PCDM_DOMHeaderParser:
	pass

#classnotwrapped
class PCDM_Document:
	pass

# harray1 classes
# harray2 classes
# harray2 classes

pcdm_FileDriverType = pcdm.FileDriverType
pcdm_FileDriverType = pcdm.FileDriverType
PCDM_ReadWriter_FileFormat = PCDM_ReadWriter.FileFormat
PCDM_ReadWriter_FileFormat = PCDM_ReadWriter.FileFormat
PCDM_ReadWriter_Open = PCDM_ReadWriter.Open
PCDM_ReadWriter_Reader = PCDM_ReadWriter.Reader
PCDM_ReadWriter_WriteFileFormat = PCDM_ReadWriter.WriteFileFormat
PCDM_ReadWriter_Writer = PCDM_ReadWriter.Writer
PCDM_RetrievalDriver_DocumentVersion = PCDM_RetrievalDriver.DocumentVersion
PCDM_RetrievalDriver_ReferenceCounter = PCDM_RetrievalDriver.ReferenceCounter
