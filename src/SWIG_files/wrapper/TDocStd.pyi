from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TDF import *
from OCC.Core.CDF import *
from OCC.Core.TCollection import *
from OCC.Core.PCDM import *
from OCC.Core.Message import *
from OCC.Core.TColStd import *
from OCC.Core.Resource import *
from OCC.Core.CDM import *

#the following typedef cannot be wrapped as is
TDocStd_DataMapIteratorOfLabelIDMapDataMap = NewType('TDocStd_DataMapIteratorOfLabelIDMapDataMap', Any)
#the following typedef cannot be wrapped as is
TDocStd_LabelIDMapDataMap = NewType('TDocStd_LabelIDMapDataMap', Any)
#the following typedef cannot be wrapped as is
TDocStd_SequenceOfApplicationDelta = NewType('TDocStd_SequenceOfApplicationDelta', Any)
#the following typedef cannot be wrapped as is
TDocStd_SequenceOfDocument = NewType('TDocStd_SequenceOfDocument', Any)
TDocStd_XLinkPtr = NewType('TDocStd_XLinkPtr', TDocStd_XLink)

class tdocstd:
	@staticmethod
	def IDList(self, anIDList: TDF_IDList) -> None: ...

class TDocStd_Application(CDF_Application):
	def __init__(self) -> None: ...
	def Close(self, aDoc: TDocStd_Document) -> None: ...
	def DefineFormat(self, theFormat: TCollection_AsciiString, theDescription: TCollection_AsciiString, theExtension: TCollection_AsciiString, theReader: PCDM_RetrievalDriver, theWriter: PCDM_StorageDriver) -> None: ...
	def GetDocument(self, index: int, aDoc: TDocStd_Document) -> None: ...
	def InitDocument(self, aDoc: TDocStd_Document) -> None: ...
	def IsDriverLoaded(self) -> bool: ...
	def IsInSession(self, path: TCollection_ExtendedString) -> int: ...
	def MessageDriver(self) -> Message_Messenger: ...
	def NbDocuments(self) -> int: ...
	def NewDocument(self, format: TCollection_ExtendedString, aDoc: TDocStd_Document) -> None: ...
	def OnAbortTransaction(self, theDoc: TDocStd_Document) -> None: ...
	def OnCommitTransaction(self, theDoc: TDocStd_Document) -> None: ...
	def OnOpenTransaction(self, theDoc: TDocStd_Document) -> None: ...
	@overload
	def Open(self, path: TCollection_ExtendedString, aDoc: TDocStd_Document) -> PCDM_ReaderStatus: ...
	def ReadingFormats(self, theFormats: TColStd_SequenceOfAsciiString) -> None: ...
	def Resources(self) -> Resource_Manager: ...
	def ResourcesName(self) -> str: ...
	@overload
	def Save(self, aDoc: TDocStd_Document) -> PCDM_StoreStatus: ...
	@overload
	def Save(self, aDoc: TDocStd_Document, theStatusMessage: TCollection_ExtendedString) -> PCDM_StoreStatus: ...
	@overload
	def SaveAs(self, aDoc: TDocStd_Document, path: TCollection_ExtendedString) -> PCDM_StoreStatus: ...
	@overload
	def SaveAs(self, aDoc: TDocStd_Document, path: TCollection_ExtendedString, theStatusMessage: TCollection_ExtendedString) -> PCDM_StoreStatus: ...
	def WritingFormats(self, theFormats: TColStd_SequenceOfAsciiString) -> None: ...

class TDocStd_ApplicationDelta(Standard_Transient):
	def __init__(self) -> None: ...
	def GetDocuments(self) -> TDocStd_SequenceOfDocument: ...
	def GetName(self) -> TCollection_ExtendedString: ...
	def SetName(self, theName: TCollection_ExtendedString) -> None: ...

class TDocStd_CompoundDelta(TDF_Delta):
	def __init__(self) -> None: ...

class TDocStd_Context:
	def __init__(self) -> None: ...
	def ModifiedReferences(self) -> bool: ...
	def SetModifiedReferences(self, Mod: bool) -> None: ...

class TDocStd_Document(CDM_Document):
	def __init__(self, astorageformat: TCollection_ExtendedString) -> None: ...
	def AbortCommand(self) -> None: ...
	def BeforeClose(self) -> None: ...
	def ChangeStorageFormat(self, newStorageFormat: TCollection_ExtendedString) -> None: ...
	def ClearRedos(self) -> None: ...
	def ClearUndos(self) -> None: ...
	def CommitCommand(self) -> bool: ...
	def EmptyLabelsSavingMode(self) -> bool: ...
	@staticmethod
	def Get(self, L: TDF_Label) -> TDocStd_Document: ...
	def GetAvailableRedos(self) -> int: ...
	def GetAvailableUndos(self) -> int: ...
	def GetData(self) -> TDF_Data: ...
	def GetModified(self) -> TDF_LabelMap: ...
	def GetName(self) -> TCollection_ExtendedString: ...
	def GetPath(self) -> TCollection_ExtendedString: ...
	def GetRedos(self) -> TDF_DeltaList: ...
	def GetSavedTime(self) -> int: ...
	def GetUndoLimit(self) -> int: ...
	def GetUndos(self) -> TDF_DeltaList: ...
	def HasOpenCommand(self) -> bool: ...
	def InitDeltaCompaction(self) -> bool: ...
	def IsChanged(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsNestedTransactionMode(self) -> bool: ...
	def IsSaved(self) -> bool: ...
	def IsValid(self) -> bool: ...
	def Main(self) -> TDF_Label: ...
	def ModificationMode(self) -> bool: ...
	def NewCommand(self) -> None: ...
	def OpenCommand(self) -> None: ...
	def PerformDeltaCompaction(self) -> bool: ...
	def PurgeModified(self) -> None: ...
	def Recompute(self) -> None: ...
	def Redo(self) -> bool: ...
	def RemoveFirstUndo(self) -> None: ...
	def SetData(self, data: TDF_Data) -> None: ...
	def SetEmptyLabelsSavingMode(self, isAllowed: bool) -> None: ...
	def SetModificationMode(self, theTransactionOnly: bool) -> None: ...
	def SetModified(self, L: TDF_Label) -> None: ...
	def SetNestedTransactionMode(self, isAllowed: Optional[bool]) -> None: ...
	def SetSaved(self) -> None: ...
	def SetSavedTime(self, theTime: int) -> None: ...
	def SetUndoLimit(self, L: int) -> None: ...
	def StorageFormat(self) -> TCollection_ExtendedString: ...
	def Undo(self) -> bool: ...
	def Update(self, aToDocument: CDM_Document, aReferenceIdentifier: int, aModifContext: None) -> None: ...
	def UpdateReferences(self, aDocEntry: TCollection_AsciiString) -> None: ...

class TDocStd_Modified(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def Add(self, alabel: TDF_Label) -> bool: ...
	def AddLabel(self, L: TDF_Label) -> bool: ...
	@overload
	@staticmethod
	def Clear(self, access: TDF_Label) -> None: ...
	@overload
	def Clear(self) -> None: ...
	@staticmethod
	def Contains(self, alabel: TDF_Label) -> bool: ...
	@overload
	@staticmethod
	def Get(self, access: TDF_Label) -> TDF_LabelMap: ...
	@overload
	def Get(self) -> TDF_LabelMap: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	@staticmethod
	def IsEmpty(self, access: TDF_Label) -> bool: ...
	@overload
	def IsEmpty(self) -> bool: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	@staticmethod
	def Remove(self, alabel: TDF_Label) -> bool: ...
	def RemoveLabel(self, L: TDF_Label) -> bool: ...
	def Restore(self, With: TDF_Attribute) -> None: ...

class TDocStd_MultiTransactionManager(Standard_Transient):
	def __init__(self) -> None: ...
	def AbortCommand(self) -> None: ...
	def AddDocument(self, theDoc: TDocStd_Document) -> None: ...
	def ClearRedos(self) -> None: ...
	def ClearUndos(self) -> None: ...
	@overload
	def CommitCommand(self) -> bool: ...
	@overload
	def CommitCommand(self, theName: TCollection_ExtendedString) -> bool: ...
	def Documents(self) -> TDocStd_SequenceOfDocument: ...
	def GetAvailableRedos(self) -> TDocStd_SequenceOfApplicationDelta: ...
	def GetAvailableUndos(self) -> TDocStd_SequenceOfApplicationDelta: ...
	def GetUndoLimit(self) -> int: ...
	def HasOpenCommand(self) -> bool: ...
	def IsNestedTransactionMode(self) -> bool: ...
	def ModificationMode(self) -> bool: ...
	def OpenCommand(self) -> None: ...
	def Redo(self) -> None: ...
	def RemoveDocument(self, theDoc: TDocStd_Document) -> None: ...
	def RemoveLastUndo(self) -> None: ...
	def SetModificationMode(self, theTransactionOnly: bool) -> None: ...
	def SetNestedTransactionMode(self, isAllowed: Optional[bool]) -> None: ...
	def SetUndoLimit(self, theLimit: int) -> None: ...
	def Undo(self) -> None: ...

class TDocStd_Owner(TDF_Attribute):
	def __init__(self) -> None: ...
	@overload
	@staticmethod
	def GetDocument(self, ofdata: TDF_Data) -> TDocStd_Document: ...
	@overload
	def GetDocument(self) -> TDocStd_Document: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def SetDocument(self, indata: TDF_Data, doc: TDocStd_Document) -> None: ...
	@overload
	def SetDocument(self, document: TDocStd_Document) -> None: ...

class TDocStd_PathParser:
	def __init__(self, path: TCollection_ExtendedString) -> None: ...
	def Extension(self) -> TCollection_ExtendedString: ...
	def Length(self) -> int: ...
	def Name(self) -> TCollection_ExtendedString: ...
	def Parse(self) -> None: ...
	def Path(self) -> TCollection_ExtendedString: ...
	def Trek(self) -> TCollection_ExtendedString: ...

class TDocStd_XLink(TDF_Attribute):
	def __init__(self) -> None: ...
	def AfterAddition(self) -> None: ...
	def AfterUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool]) -> bool: ...
	def BackupCopy(self) -> TDF_Attribute: ...
	def BeforeRemoval(self) -> None: ...
	def BeforeUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool]) -> bool: ...
	@overload
	def DocumentEntry(self, aDocEntry: TCollection_AsciiString) -> None: ...
	@overload
	def DocumentEntry(self) -> TCollection_AsciiString: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	def LabelEntry(self, aLabel: TDF_Label) -> None: ...
	@overload
	def LabelEntry(self, aLabEntry: TCollection_AsciiString) -> None: ...
	@overload
	def LabelEntry(self) -> TCollection_AsciiString: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, intoAttribute: TDF_Attribute, aRelocationTable: TDF_RelocationTable) -> None: ...
	def Restore(self, anAttribute: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, atLabel: TDF_Label) -> TDocStd_XLink: ...
	def Update(self) -> TDF_Reference: ...

class TDocStd_XLinkIterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, D: TDocStd_Document) -> None: ...
	def Initialize(self, D: TDocStd_Document) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> TDocStd_XLinkPtr: ...

class TDocStd_XLinkRoot(TDF_Attribute):
	def BackupCopy(self) -> TDF_Attribute: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@staticmethod
	def Insert(self, anXLinkPtr: TDocStd_XLinkPtr) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, intoAttribute: TDF_Attribute, aRelocationTable: TDF_RelocationTable) -> None: ...
	@staticmethod
	def Remove(self, anXLinkPtr: TDocStd_XLinkPtr) -> None: ...
	def Restore(self, anAttribute: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, aDF: TDF_Data) -> TDocStd_XLinkRoot: ...

class TDocStd_XLinkTool:
	def __init__(self) -> None: ...
	def Copy(self, intarget: TDF_Label, fromsource: TDF_Label) -> None: ...
	def CopyWithLink(self, intarget: TDF_Label, fromsource: TDF_Label) -> None: ...
	def DataSet(self) -> TDF_DataSet: ...
	def IsDone(self) -> bool: ...
	def RelocationTable(self) -> TDF_RelocationTable: ...
	def UpdateLink(self, L: TDF_Label) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

tdocstd_IDList = tdocstd.IDList
TDocStd_Document_Get = TDocStd_Document.Get
TDocStd_Modified_Add = TDocStd_Modified.Add
TDocStd_Modified_Clear = TDocStd_Modified.Clear
TDocStd_Modified_Contains = TDocStd_Modified.Contains
TDocStd_Modified_Get = TDocStd_Modified.Get
TDocStd_Modified_GetID = TDocStd_Modified.GetID
TDocStd_Modified_IsEmpty = TDocStd_Modified.IsEmpty
TDocStd_Modified_Remove = TDocStd_Modified.Remove
TDocStd_Owner_GetDocument = TDocStd_Owner.GetDocument
TDocStd_Owner_GetID = TDocStd_Owner.GetID
TDocStd_Owner_SetDocument = TDocStd_Owner.SetDocument
TDocStd_XLink_GetID = TDocStd_XLink.GetID
TDocStd_XLink_Set = TDocStd_XLink.Set
TDocStd_XLinkRoot_GetID = TDocStd_XLinkRoot.GetID
TDocStd_XLinkRoot_Insert = TDocStd_XLinkRoot.Insert
TDocStd_XLinkRoot_Remove = TDocStd_XLinkRoot.Remove
TDocStd_XLinkRoot_Set = TDocStd_XLinkRoot.Set
