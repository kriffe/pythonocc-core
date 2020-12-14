from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TDocStd import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.gp import *

#the following typedef cannot be wrapped as is
TObj_TIntSparseArray_MapOfData = NewType('TObj_TIntSparseArray_MapOfData', Any)
#the following typedef cannot be wrapped as is
TObj_TIntSparseArray_VecOfData = NewType('TObj_TIntSparseArray_VecOfData', Any)

class TObj_SequenceOfIterator:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class TObj_SequenceOfObject:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class TObj_DeletingMode(IntEnum):
	TObj_FreeOnly: int = ...
	TObj_KeepDepending: int = ...
	TObj_Forced: int = ...
TObj_FreeOnly = TObj_DeletingMode.TObj_FreeOnly
TObj_KeepDepending = TObj_DeletingMode.TObj_KeepDepending
TObj_Forced = TObj_DeletingMode.TObj_Forced

class TObj_Application(TDocStd_Application):
	def CreateNewDocument(self, theDoc: TDocStd_Document, theFormat: TCollection_ExtendedString) -> bool: ...
	@overload
	def ErrorMessage(self, theMsg: TCollection_ExtendedString, theLevel: Message_Gravity) -> None: ...
	@overload
	def ErrorMessage(self, theMsg: TCollection_ExtendedString) -> None: ...
	@staticmethod
	def GetInstance() -> TObj_Application: ...
	def IsVerbose(self) -> bool: ...
	def LoadDocument(self, theSourceFile: TCollection_ExtendedString, theTargetDoc: TDocStd_Document) -> bool: ...
	def Messenger(self) -> Message_Messenger: ...
	def ResourcesName(self) -> str: ...
	def SaveDocument(self, theSourceDoc: TDocStd_Document, theTargetFile: TCollection_ExtendedString) -> bool: ...
	def SetVerbose(self, isVerbose: bool) -> None: ...

class TObj_Assistant:
	@staticmethod
	def BindModel(theModel: TObj_Model) -> None: ...
	@staticmethod
	def BindType(theType: Standard_Type) -> int: ...
	@staticmethod
	def ClearModelMap() -> None: ...
	@staticmethod
	def ClearTypeMap() -> None: ...
	@staticmethod
	def FindModel(theName: str) -> TObj_Model: ...
	@staticmethod
	def FindType(theTypeIndex: int) -> Standard_Type: ...
	@staticmethod
	def FindTypeIndex(theType: Standard_Type) -> int: ...
	@staticmethod
	def GetAppVersion() -> int: ...
	@staticmethod
	def GetCurrentModel() -> TObj_Model: ...
	@staticmethod
	def SetCurrentModel(theModel: TObj_Model) -> None: ...
	@staticmethod
	def UnSetCurrentModel() -> None: ...

class TObj_CheckModel(Message_Algorithm):
	def __init__(self, theModel: TObj_Model) -> None: ...
	def GetModel(self) -> TObj_Model: ...
	def IsToFix(self) -> bool: ...
	def Perform(self) -> bool: ...
	def SetToFix(self, theToFix: bool) -> None: ...

class TObj_Model(Standard_Transient):
	def AbortCommand(self) -> None: ...
	def Close(self) -> bool: ...
	def CloseDocument(self, theDoc: TDocStd_Document) -> None: ...
	def CommitCommand(self) -> None: ...
	def CopyReferences(self, theTarget: TObj_Model, theRelocTable: TDF_RelocationTable) -> None: ...
	def FindObject(self, theName: TCollection_HExtendedString, theDictionary: TObj_TNameContainer) -> TObj_Object: ...
	def GetApplication(self) -> TObj_Application: ...
	def GetChecker(self) -> TObj_CheckModel: ...
	def GetChildren(self) -> TObj_ObjectIterator: ...
	def GetDictionary(self) -> TObj_TNameContainer: ...
	def GetDocument(self) -> TDocStd_Document: ...
	@staticmethod
	def GetDocumentModel(theLabel: TDF_Label) -> TObj_Model: ...
	def GetFile(self) -> TCollection_HExtendedString: ...
	def GetFormat(self) -> TCollection_ExtendedString: ...
	def GetFormatVersion(self) -> int: ...
	def GetGUID(self) -> Standard_GUID: ...
	def GetLabel(self) -> TDF_Label: ...
	def GetMainPartition(self) -> TObj_Partition: ...
	def GetModelName(self) -> TCollection_HExtendedString: ...
	def GetObjects(self) -> TObj_ObjectIterator: ...
	def GetRoot(self) -> TObj_Object: ...
	def HasOpenCommand(self) -> bool: ...
	def IsModified(self) -> bool: ...
	def IsRegisteredName(self, theName: TCollection_HExtendedString, theDictionary: TObj_TNameContainer) -> bool: ...
	def Load(self, theFile: TCollection_ExtendedString) -> bool: ...
	def Messenger(self) -> Message_Messenger: ...
	def NewEmpty(self) -> TObj_Model: ...
	def OpenCommand(self) -> None: ...
	def Paste(self, theModel: TObj_Model, theRelocTable: Optional[TDF_RelocationTable] = 0) -> bool: ...
	def RegisterName(self, theName: TCollection_HExtendedString, theLabel: TDF_Label, theDictionary: TObj_TNameContainer) -> None: ...
	def Save(self) -> bool: ...
	def SaveAs(self, theFile: TCollection_ExtendedString) -> bool: ...
	def SetLabel(self, theLabel: TDF_Label) -> None: ...
	def SetMessenger(self, theMsgr: Message_Messenger) -> None: ...
	def SetModified(self, theModified: bool) -> None: ...
	@staticmethod
	def SetNewName(theObject: TObj_Object) -> None: ...
	def UnRegisterName(self, theName: TCollection_HExtendedString, theDictionary: TObj_TNameContainer) -> None: ...
	def Update(self) -> bool: ...

class TObj_Object(Standard_Transient):
	def AddBackReference(self, theObject: TObj_Object) -> None: ...
	def AfterRetrieval(self) -> None: ...
	def BeforeStoring(self) -> None: ...
	def CanDetach(self, theMode: Optional[TObj_DeletingMode] = TObj_FreeOnly) -> bool: ...
	def CanRemoveReference(self, theObject: TObj_Object) -> bool: ...
	def ClearBackReferences(self) -> None: ...
	def ClearFlags(self, theMask: Optional[int] = ~0) -> None: ...
	def Clone(self, theTargetLabel: TDF_Label, theRelocTable: Optional[TDF_RelocationTable] = 0) -> TObj_Object: ...
	def CopyChildren(self, theTargetLabel: TDF_Label, theRelocTable: TDF_RelocationTable) -> None: ...
	def CopyReferences(self, theTargetObject: TObj_Object, theRelocTable: TDF_RelocationTable) -> None: ...
	@overload
	def Detach(self, theMode: Optional[TObj_DeletingMode] = TObj_FreeOnly) -> bool: ...
	@overload
	@staticmethod
	def Detach(theLabel: TDF_Label, theMode: Optional[TObj_DeletingMode] = TObj_FreeOnly) -> bool: ...
	def GetBackReferences(self, theType: Optional[Standard_Type] = None) -> TObj_ObjectIterator: ...
	def GetBadReference(self, theRoot: TDF_Label, theBadReference: TDF_Label) -> bool: ...
	def GetChildLabel(self) -> TDF_Label: ...
	def GetChildren(self, theType: Optional[Standard_Type] = None) -> TObj_ObjectIterator: ...
	def GetDataLabel(self) -> TDF_Label: ...
	def GetDictionary(self) -> TObj_TNameContainer: ...
	def GetFatherObject(self, theType: Optional[Standard_Type] = None) -> TObj_Object: ...
	def GetFlags(self) -> int: ...
	def GetLabel(self) -> TDF_Label: ...
	def GetModel(self) -> TObj_Model: ...
	@overload
	def GetName(self) -> TCollection_HExtendedString: ...
	@overload
	def GetName(self, theName: TCollection_ExtendedString) -> bool: ...
	@overload
	def GetName(self, theName: TCollection_AsciiString) -> bool: ...
	@staticmethod
	def GetObj(theLabel: TDF_Label, theResult: TObj_Object, isSuper: Optional[bool] = False) -> bool: ...
	def GetOrder(self) -> int: ...
	def GetReferenceLabel(self) -> TDF_Label: ...
	def GetReferences(self, theType: Optional[Standard_Type] = None) -> TObj_ObjectIterator: ...
	def GetTypeFlags(self) -> int: ...
	def HasBackReferences(self) -> bool: ...
	def HasModifications(self) -> bool: ...
	def HasReference(self, theObject: TObj_Object) -> bool: ...
	def IsAlive(self) -> bool: ...
	def RelocateReferences(self, theFromRoot: TDF_Label, theToRoot: TDF_Label, theUpdateBackRefs: Optional[bool] = True) -> bool: ...
	def RemoveAllReferences(self) -> None: ...
	def RemoveBackReference(self, theObject: TObj_Object, theSingleOnly: Optional[bool] = True) -> None: ...
	def RemoveBackReferences(self, theMode: Optional[TObj_DeletingMode] = TObj_FreeOnly) -> bool: ...
	def RemoveReference(self, theObject: TObj_Object) -> None: ...
	def ReplaceReference(self, theOldObject: TObj_Object, theNewObject: TObj_Object) -> None: ...
	def SetFlags(self, theMask: int) -> None: ...
	@overload
	def SetName(self, theName: TCollection_HExtendedString) -> bool: ...
	@overload
	def SetName(self, theName: TCollection_HAsciiString) -> bool: ...
	@overload
	def SetName(self, name: str) -> bool: ...
	def SetOrder(self, theIndx: int) -> bool: ...
	def TestFlags(self, theMask: int) -> bool: ...
	def getChildLabel(self, theRank: int) -> TDF_Label: ...

class TObj_ObjectIterator(Standard_Transient):
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> TObj_Object: ...

class TObj_Persistence:
	@staticmethod
	def CreateNewObject(theType: str, theLabel: TDF_Label) -> TObj_Object: ...

class TObj_TIntSparseArray(TDF_Attribute):
	def __init__(self) -> None: ...
	def AfterUndo(self, theDelta: TDF_AttributeDelta, toForce: bool) -> bool: ...
	def BackupCopy(self) -> TDF_Attribute: ...
	def BeforeCommitTransaction(self) -> None: ...
	def Clear(self) -> None: ...
	def ClearDelta(self) -> None: ...
	def DeltaOnModification(self, theDelta: TDF_DeltaOnModification) -> None: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def GetIterator(self) -> False: ...
	def HasValue(self, theId: int) -> bool: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, theInto: TDF_Attribute, theRT: TDF_RelocationTable) -> None: ...
	def Restore(self, theDelta: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(theLabel: TDF_Label) -> TObj_TIntSparseArray: ...
	def SetDoBackup(self, toDo: bool) -> None: ...
	def SetValue(self, theId: int, theValue: int) -> None: ...
	def Size(self) -> int: ...
	def UnsetValue(self, theId: int) -> None: ...
	def Value(self, theId: int) -> int: ...

class TObj_TModel(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def Model(self) -> TObj_Model: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, theInto: TDF_Attribute, theRT: TDF_RelocationTable) -> None: ...
	def Restore(self, theWith: TDF_Attribute) -> None: ...
	def Set(self, theModel: TObj_Model) -> None: ...

class TObj_TNameContainer(TDF_Attribute):
	def __init__(self) -> None: ...
	def Clear(self) -> None: ...
	def Get(self) -> TObj_DataMapOfNameLabel: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def IsRegistered(self, theName: TCollection_HExtendedString) -> bool: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, theInto: TDF_Attribute, theRT: TDF_RelocationTable) -> None: ...
	def RecordName(self, theName: TCollection_HExtendedString, theLabel: TDF_Label) -> None: ...
	def RemoveName(self, theName: TCollection_HExtendedString) -> None: ...
	def Restore(self, theWith: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(theLabel: TDF_Label) -> TObj_TNameContainer: ...
	@overload
	def Set(self, theElem: TObj_DataMapOfNameLabel) -> None: ...

class TObj_TObject(TDF_Attribute):
	def __init__(self) -> None: ...
	def AfterUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: bool) -> bool: ...
	def BeforeForget(self) -> None: ...
	def Get(self) -> TObj_Object: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, theInto: TDF_Attribute, theRT: TDF_RelocationTable) -> None: ...
	def Restore(self, theWith: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(theLabel: TDF_Label, theElem: TObj_Object) -> TObj_TObject: ...
	@overload
	def Set(self, theElem: TObj_Object) -> None: ...

class TObj_TReference(TDF_Attribute):
	def __init__(self) -> None: ...
	def AfterResume(self) -> None: ...
	def AfterRetrieval(self, forceIt: Optional[bool] = False) -> bool: ...
	def AfterUndo(self, theDelta: TDF_AttributeDelta, isForced: Optional[bool] = False) -> bool: ...
	def BeforeForget(self) -> None: ...
	def BeforeUndo(self, theDelta: TDF_AttributeDelta, isForced: Optional[bool] = False) -> bool: ...
	def Get(self) -> TObj_Object: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def GetLabel(self) -> TDF_Label: ...
	def GetMasterLabel(self) -> TDF_Label: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, theInto: TDF_Attribute, theRT: TDF_RelocationTable) -> None: ...
	def Restore(self, theWith: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(theLabel: TDF_Label, theObject: TObj_Object, theMaster: TObj_Object) -> TObj_TReference: ...
	@overload
	def Set(self, theObject: TObj_Object, theMasterLabel: TDF_Label) -> None: ...
	@overload
	def Set(self, theLabel: TDF_Label, theMasterLabel: TDF_Label) -> None: ...

class TObj_TXYZ(TDF_Attribute):
	def __init__(self) -> None: ...
	def Get(self) -> gp_XYZ: ...
	@staticmethod
	def GetID() -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, theInto: TDF_Attribute, theRT: TDF_RelocationTable) -> None: ...
	def Restore(self, theWith: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(theLabel: TDF_Label, theXYZ: gp_XYZ) -> TObj_TXYZ: ...
	@overload
	def Set(self, theXYZ: gp_XYZ) -> None: ...

class TObj_LabelIterator(TObj_ObjectIterator):
	def LabelValue(self) -> TDF_Label: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> TObj_Object: ...

class TObj_ModelIterator(TObj_ObjectIterator):
	def __init__(self, theModel: TObj_Model) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> TObj_Object: ...

class TObj_Partition(TObj_Object):
	def AfterRetrieval(self) -> None: ...
	@staticmethod
	def Create(theLabel: TDF_Label, theSetName: Optional[bool] = True) -> TObj_Partition: ...
	def GetLastIndex(self) -> int: ...
	def GetNamePrefix(self) -> TCollection_HExtendedString: ...
	def GetNewName(self, theIsToChangeCount: Optional[bool] = True) -> TCollection_HExtendedString: ...
	@staticmethod
	def GetPartition(theObject: TObj_Object) -> TObj_Partition: ...
	def NewLabel(self) -> TDF_Label: ...
	def SetLastIndex(self, theIndex: int) -> None: ...
	def SetName(self, theName: TCollection_HExtendedString) -> bool: ...
	def SetNamePrefix(self, thePrefix: TCollection_HExtendedString) -> None: ...
	def Update(self) -> bool: ...

class TObj_SequenceIterator(TObj_ObjectIterator):
	def __init__(self, theObjects: TObj_HSequenceOfObject, theType: Optional[Standard_Type] = None) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> TObj_Object: ...

class TObj_HiddenPartition(TObj_Partition):
	def __init__(self, theLabel: TDF_Label) -> None: ...
	def GetTypeFlags(self) -> int: ...

class TObj_OcafObjectIterator(TObj_LabelIterator):
	def __init__(self, theLabel: TDF_Label, theType: Optional[Standard_Type] = None, theRecursive: Optional[bool] = False, theAllSubChildren: Optional[bool] = False) -> None: ...

class TObj_ReferenceIterator(TObj_LabelIterator):
	def __init__(self, theLabel: TDF_Label, theType: Optional[Standard_Type] = None, theRecursive: Optional[bool] = True) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

class TObj_HSequenceOfObject(TObj_SequenceOfObject, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: TObj_SequenceOfObject) -> None: ...
    def Sequence(self) -> TObj_SequenceOfObject: ...
    def Append(self, theSequence: TObj_SequenceOfObject) -> None: ...


TObj_Application_GetInstance = TObj_Application.GetInstance
TObj_Assistant_BindModel = TObj_Assistant.BindModel
TObj_Assistant_BindType = TObj_Assistant.BindType
TObj_Assistant_ClearModelMap = TObj_Assistant.ClearModelMap
TObj_Assistant_ClearTypeMap = TObj_Assistant.ClearTypeMap
TObj_Assistant_FindModel = TObj_Assistant.FindModel
TObj_Assistant_FindType = TObj_Assistant.FindType
TObj_Assistant_FindTypeIndex = TObj_Assistant.FindTypeIndex
TObj_Assistant_GetAppVersion = TObj_Assistant.GetAppVersion
TObj_Assistant_GetCurrentModel = TObj_Assistant.GetCurrentModel
TObj_Assistant_SetCurrentModel = TObj_Assistant.SetCurrentModel
TObj_Assistant_UnSetCurrentModel = TObj_Assistant.UnSetCurrentModel
TObj_Model_GetDocumentModel = TObj_Model.GetDocumentModel
TObj_Model_SetNewName = TObj_Model.SetNewName
TObj_Object_Detach = TObj_Object.Detach
TObj_Object_GetObj = TObj_Object.GetObj
TObj_Persistence_CreateNewObject = TObj_Persistence.CreateNewObject
TObj_TIntSparseArray_GetID = TObj_TIntSparseArray.GetID
TObj_TIntSparseArray_Set = TObj_TIntSparseArray.Set
TObj_TModel_GetID = TObj_TModel.GetID
TObj_TNameContainer_GetID = TObj_TNameContainer.GetID
TObj_TNameContainer_Set = TObj_TNameContainer.Set
TObj_TObject_GetID = TObj_TObject.GetID
TObj_TObject_Set = TObj_TObject.Set
TObj_TReference_GetID = TObj_TReference.GetID
TObj_TReference_Set = TObj_TReference.Set
TObj_TXYZ_GetID = TObj_TXYZ.GetID
TObj_TXYZ_Set = TObj_TXYZ.Set
TObj_Partition_Create = TObj_Partition.Create
TObj_Partition_GetPartition = TObj_Partition.GetPartition
