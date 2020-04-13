from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *

#the following typedef cannot be wrapped as is
TDF_AttributeDataMap = NewType('TDF_AttributeDataMap', Any)
#the following typedef cannot be wrapped as is
TDF_AttributeDeltaList = NewType('TDF_AttributeDeltaList', Any)
#the following typedef cannot be wrapped as is
TDF_AttributeDoubleMap = NewType('TDF_AttributeDoubleMap', Any)
#the following typedef cannot be wrapped as is
TDF_AttributeIndexedMap = NewType('TDF_AttributeIndexedMap', Any)
#the following typedef cannot be wrapped as is
TDF_AttributeList = NewType('TDF_AttributeList', Any)
#the following typedef cannot be wrapped as is
TDF_AttributeMap = NewType('TDF_AttributeMap', Any)
#the following typedef cannot be wrapped as is
TDF_AttributeSequence = NewType('TDF_AttributeSequence', Any)
#the following typedef cannot be wrapped as is
TDF_DataMapIteratorOfAttributeDataMap = NewType('TDF_DataMapIteratorOfAttributeDataMap', Any)
#the following typedef cannot be wrapped as is
TDF_DataMapIteratorOfLabelDataMap = NewType('TDF_DataMapIteratorOfLabelDataMap', Any)
#the following typedef cannot be wrapped as is
TDF_DataMapIteratorOfLabelIntegerMap = NewType('TDF_DataMapIteratorOfLabelIntegerMap', Any)
#the following typedef cannot be wrapped as is
TDF_DeltaList = NewType('TDF_DeltaList', Any)
#the following typedef cannot be wrapped as is
TDF_DoubleMapIteratorOfAttributeDoubleMap = NewType('TDF_DoubleMapIteratorOfAttributeDoubleMap', Any)
#the following typedef cannot be wrapped as is
TDF_DoubleMapIteratorOfGUIDProgIDMap = NewType('TDF_DoubleMapIteratorOfGUIDProgIDMap', Any)
#the following typedef cannot be wrapped as is
TDF_DoubleMapIteratorOfLabelDoubleMap = NewType('TDF_DoubleMapIteratorOfLabelDoubleMap', Any)
#the following typedef cannot be wrapped as is
TDF_GUIDProgIDMap = NewType('TDF_GUIDProgIDMap', Any)
#the following typedef cannot be wrapped as is
TDF_HAllocator = NewType('TDF_HAllocator', Any)
#the following typedef cannot be wrapped as is
TDF_IDList = NewType('TDF_IDList', Any)
#the following typedef cannot be wrapped as is
TDF_IDMap = NewType('TDF_IDMap', Any)
#the following typedef cannot be wrapped as is
TDF_LabelDataMap = NewType('TDF_LabelDataMap', Any)
#the following typedef cannot be wrapped as is
TDF_LabelDoubleMap = NewType('TDF_LabelDoubleMap', Any)
#the following typedef cannot be wrapped as is
TDF_LabelIndexedMap = NewType('TDF_LabelIndexedMap', Any)
#the following typedef cannot be wrapped as is
TDF_LabelIntegerMap = NewType('TDF_LabelIntegerMap', Any)
#the following typedef cannot be wrapped as is
TDF_LabelList = NewType('TDF_LabelList', Any)
#the following typedef cannot be wrapped as is
TDF_LabelMap = NewType('TDF_LabelMap', Any)
TDF_LabelNodePtr = NewType('TDF_LabelNodePtr', TDF_LabelNode)
#the following typedef cannot be wrapped as is
TDF_LabelSequence = NewType('TDF_LabelSequence', Any)
#the following typedef cannot be wrapped as is
TDF_ListIteratorOfAttributeDeltaList = NewType('TDF_ListIteratorOfAttributeDeltaList', Any)
#the following typedef cannot be wrapped as is
TDF_ListIteratorOfAttributeList = NewType('TDF_ListIteratorOfAttributeList', Any)
#the following typedef cannot be wrapped as is
TDF_ListIteratorOfDeltaList = NewType('TDF_ListIteratorOfDeltaList', Any)
#the following typedef cannot be wrapped as is
TDF_ListIteratorOfIDList = NewType('TDF_ListIteratorOfIDList', Any)
#the following typedef cannot be wrapped as is
TDF_ListIteratorOfLabelList = NewType('TDF_ListIteratorOfLabelList', Any)
#the following typedef cannot be wrapped as is
TDF_MapIteratorOfAttributeMap = NewType('TDF_MapIteratorOfAttributeMap', Any)
#the following typedef cannot be wrapped as is
TDF_MapIteratorOfIDMap = NewType('TDF_MapIteratorOfIDMap', Any)
#the following typedef cannot be wrapped as is
TDF_MapIteratorOfLabelMap = NewType('TDF_MapIteratorOfLabelMap', Any)

class TDF_AttributeArray1:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]: ...
    def next(self) -> False: ...
    __next__ = next

class tdf:
	@staticmethod
	def AddLinkGUIDToProgID(self, ID: Standard_GUID, ProgID: TCollection_ExtendedString) -> None: ...
	@staticmethod
	def GUIDFromProgID(self, ProgID: TCollection_ExtendedString, ID: Standard_GUID) -> bool: ...
	@staticmethod
	def LowestID(self) -> Standard_GUID: ...
	@staticmethod
	def ProgIDFromGUID(self, ID: Standard_GUID, ProgID: TCollection_ExtendedString) -> bool: ...
	@staticmethod
	def UppestID(self) -> Standard_GUID: ...

class TDF_Attribute(Standard_Transient):
	def AddAttribute(self, other: TDF_Attribute) -> None: ...
	def AfterAddition(self) -> None: ...
	def AfterResume(self) -> None: ...
	def AfterRetrieval(self, forceIt: Optional[bool]) -> bool: ...
	def AfterUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool]) -> bool: ...
	def Backup(self) -> None: ...
	def BackupCopy(self) -> TDF_Attribute: ...
	def BeforeCommitTransaction(self) -> None: ...
	def BeforeForget(self) -> None: ...
	def BeforeRemoval(self) -> None: ...
	def BeforeUndo(self, anAttDelta: TDF_AttributeDelta, forceIt: Optional[bool]) -> bool: ...
	def DeltaOnAddition(self) -> TDF_DeltaOnAddition: ...
	def DeltaOnForget(self) -> TDF_DeltaOnForget: ...
	@overload
	def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
	@overload
	def DeltaOnModification(self, aDelta: TDF_DeltaOnModification) -> None: ...
	def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval: ...
	def DeltaOnResume(self) -> TDF_DeltaOnResume: ...
	@overload
	def FindAttribute(self, anID: Standard_GUID, anAttribute: TDF_Attribute) -> bool: ...
	def Forget(self, aTransaction: int) -> None: ...
	def ForgetAllAttributes(self, clearChildren: Optional[bool]) -> None: ...
	def ForgetAttribute(self, aguid: Standard_GUID) -> bool: ...
	def ID(self) -> Standard_GUID: ...
	def IsAttribute(self, anID: Standard_GUID) -> bool: ...
	def IsBackuped(self) -> bool: ...
	def IsForgotten(self) -> bool: ...
	def IsNew(self) -> bool: ...
	def IsValid(self) -> bool: ...
	def Label(self) -> TDF_Label: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, intoAttribute: TDF_Attribute, aRelocationTable: TDF_RelocationTable) -> None: ...
	def References(self, aDataSet: TDF_DataSet) -> None: ...
	def Restore(self, anAttribute: TDF_Attribute) -> None: ...
	@overload
	def SetID(self) -> None: ...
	def Transaction(self) -> int: ...
	def UntilTransaction(self) -> int: ...

class TDF_AttributeDelta(Standard_Transient):
	def Apply(self) -> None: ...
	def Attribute(self) -> TDF_Attribute: ...
	def ID(self) -> Standard_GUID: ...
	def Label(self) -> TDF_Label: ...

class TDF_AttributeIterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aLabel: TDF_Label, withoutForgotten: Optional[bool]) -> None: ...
	@overload
	def __init__(self, aLabelNode: TDF_LabelNodePtr, withoutForgotten: Optional[bool]) -> None: ...
	def Initialize(self, aLabel: TDF_Label, withoutForgotten: Optional[bool]) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def PtrValue(self) -> TDF_Attribute: ...
	def Value(self) -> TDF_Attribute: ...

class TDF_ChildIDIterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aLabel: TDF_Label, anID: Standard_GUID, allLevels: Optional[bool]) -> None: ...
	def Initialize(self, aLabel: TDF_Label, anID: Standard_GUID, allLevels: Optional[bool]) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def NextBrother(self) -> None: ...
	def Value(self) -> TDF_Attribute: ...

class TDF_ChildIterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aLabel: TDF_Label, allLevels: Optional[bool]) -> None: ...
	def Initialize(self, aLabel: TDF_Label, allLevels: Optional[bool]) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def NextBrother(self) -> None: ...
	def Value(self) -> TDF_Label: ...

class TDF_ClosureMode:
	def __init__(self, aMode: Optional[bool]) -> None: ...
	@overload
	def Descendants(self, aStatus: bool) -> None: ...
	@overload
	def Descendants(self) -> bool: ...
	@overload
	def References(self, aStatus: bool) -> None: ...
	@overload
	def References(self) -> bool: ...

class TDF_ClosureTool:
	@overload
	@staticmethod
	def Closure(self, aDataSet: TDF_DataSet) -> None: ...
	@overload
	@staticmethod
	def Closure(self, aDataSet: TDF_DataSet, aFilter: TDF_IDFilter, aMode: TDF_ClosureMode) -> None: ...
	@overload
	@staticmethod
	def Closure(self, aLabel: TDF_Label, aLabMap: TDF_LabelMap, anAttMap: TDF_AttributeMap, aFilter: TDF_IDFilter, aMode: TDF_ClosureMode) -> None: ...

class TDF_ComparisonTool:
	@staticmethod
	def Compare(self, aSourceDataSet: TDF_DataSet, aTargetDataSet: TDF_DataSet, aFilter: TDF_IDFilter, aRelocationTable: TDF_RelocationTable) -> None: ...
	@staticmethod
	def Cut(self, aDataSet: TDF_DataSet) -> None: ...
	@staticmethod
	def IsSelfContained(self, aLabel: TDF_Label, aDataSet: TDF_DataSet) -> bool: ...
	@staticmethod
	def SourceUnbound(self, aRefDataSet: TDF_DataSet, aRelocationTable: TDF_RelocationTable, aFilter: TDF_IDFilter, aDiffDataSet: TDF_DataSet, anOption: Optional[int]) -> bool: ...
	@staticmethod
	def TargetUnbound(self, aRefDataSet: TDF_DataSet, aRelocationTable: TDF_RelocationTable, aFilter: TDF_IDFilter, aDiffDataSet: TDF_DataSet, anOption: Optional[int]) -> bool: ...

class TDF_CopyLabel:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aSource: TDF_Label, aTarget: TDF_Label) -> None: ...
	@overload
	@staticmethod
	def ExternalReferences(self, Lab: TDF_Label, aExternals: TDF_AttributeMap, aFilter: TDF_IDFilter) -> bool: ...
	@overload
	@staticmethod
	def ExternalReferences(self, aRefLab: TDF_Label, Lab: TDF_Label, aExternals: TDF_AttributeMap, aFilter: TDF_IDFilter, aDataSet: TDF_DataSet) -> None: ...
	def IsDone(self) -> bool: ...
	def Load(self, aSource: TDF_Label, aTarget: TDF_Label) -> None: ...
	def Perform(self) -> None: ...
	def RelocationTable(self) -> TDF_RelocationTable: ...
	def UseFilter(self, aFilter: TDF_IDFilter) -> None: ...

class TDF_CopyTool:
	@overload
	@staticmethod
	def Copy(self, aSourceDataSet: TDF_DataSet, aRelocationTable: TDF_RelocationTable) -> None: ...
	@overload
	@staticmethod
	def Copy(self, aSourceDataSet: TDF_DataSet, aRelocationTable: TDF_RelocationTable, aPrivilegeFilter: TDF_IDFilter) -> None: ...
	@overload
	@staticmethod
	def Copy(self, aSourceDataSet: TDF_DataSet, aRelocationTable: TDF_RelocationTable, aPrivilegeFilter: TDF_IDFilter, aRefFilter: TDF_IDFilter, setSelfContained: bool) -> None: ...

class TDF_Data(Standard_Transient):
	def __init__(self) -> None: ...
	def AllowModification(self, isAllowed: bool) -> None: ...
	def Destroy(self) -> None: ...
	def IsApplicable(self, aDelta: TDF_Delta) -> bool: ...
	def IsModificationAllowed(self) -> bool: ...
	def LabelNodeAllocator(self) -> TDF_HAllocator: ...
	def NotUndoMode(self) -> bool: ...
	def Root(self) -> TDF_Label: ...
	def Time(self) -> int: ...
	def Transaction(self) -> int: ...
	def Undo(self, aDelta: TDF_Delta, withDelta: Optional[bool]) -> TDF_Delta: ...

class TDF_DataSet(Standard_Transient):
	def __init__(self) -> None: ...
	def AddAttribute(self, anAttribute: TDF_Attribute) -> None: ...
	def AddLabel(self, aLabel: TDF_Label) -> None: ...
	def AddRoot(self, aLabel: TDF_Label) -> None: ...
	def Attributes(self) -> TDF_AttributeMap: ...
	def Clear(self) -> None: ...
	def ContainsAttribute(self, anAttribute: TDF_Attribute) -> bool: ...
	def ContainsLabel(self, aLabel: TDF_Label) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Labels(self) -> TDF_LabelMap: ...
	def Roots(self) -> TDF_LabelList: ...

class TDF_Delta(Standard_Transient):
	def __init__(self) -> None: ...
	def AttributeDeltas(self) -> TDF_AttributeDeltaList: ...
	def BeginTime(self) -> int: ...
	def EndTime(self) -> int: ...
	def IsApplicable(self, aCurrentTime: int) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Labels(self, aLabelList: TDF_LabelList) -> None: ...
	def Name(self) -> TCollection_ExtendedString: ...
	def SetName(self, theName: TCollection_ExtendedString) -> None: ...

class TDF_IDFilter:
	def __init__(self, ignoreMode: Optional[bool]) -> None: ...
	def Copy(self, fromFilter: TDF_IDFilter) -> None: ...
	def IDList(self, anIDList: TDF_IDList) -> None: ...
	@overload
	def Ignore(self, anID: Standard_GUID) -> None: ...
	@overload
	def Ignore(self, anIDList: TDF_IDList) -> None: ...
	@overload
	def IgnoreAll(self, ignore: bool) -> None: ...
	@overload
	def IgnoreAll(self) -> bool: ...
	@overload
	def IsIgnored(self, anID: Standard_GUID) -> bool: ...
	@overload
	def IsIgnored(self, anAtt: TDF_Attribute) -> bool: ...
	@overload
	def IsKept(self, anID: Standard_GUID) -> bool: ...
	@overload
	def IsKept(self, anAtt: TDF_Attribute) -> bool: ...
	@overload
	def Keep(self, anID: Standard_GUID) -> None: ...
	@overload
	def Keep(self, anIDList: TDF_IDList) -> None: ...

class TDF_Label:
	def __init__(self) -> None: ...
	def AddAttribute(self, anAttribute: TDF_Attribute, append: Optional[bool]) -> None: ...
	def AttributesModified(self) -> bool: ...
	def Data(self) -> TDF_Data: ...
	def Depth(self) -> int: ...
	def Father(self) -> TDF_Label: ...
	@overload
	def FindAttribute(self, anID: Standard_GUID, anAttribute: TDF_Attribute) -> bool: ...
	@overload
	def FindAttribute(self, anID: Standard_GUID, aTransaction: int, anAttribute: TDF_Attribute) -> bool: ...
	def FindChild(self, aTag: int, create: Optional[bool]) -> TDF_Label: ...
	def ForgetAllAttributes(self, clearChildren: Optional[bool]) -> None: ...
	@overload
	def ForgetAttribute(self, anAttribute: TDF_Attribute) -> None: ...
	@overload
	def ForgetAttribute(self, aguid: Standard_GUID) -> bool: ...
	def HasAttribute(self) -> bool: ...
	def HasChild(self) -> bool: ...
	def HasGreaterNode(self, otherLabel: TDF_Label) -> bool: ...
	def HasLowerNode(self, otherLabel: TDF_Label) -> bool: ...
	def Imported(self, aStatus: bool) -> None: ...
	def IsAttribute(self, anID: Standard_GUID) -> bool: ...
	def IsDescendant(self, aLabel: TDF_Label) -> bool: ...
	def IsDifferent(self, aLabel: TDF_Label) -> bool: ...
	def IsEqual(self, aLabel: TDF_Label) -> bool: ...
	def IsImported(self) -> bool: ...
	def IsNull(self) -> bool: ...
	def IsRoot(self) -> bool: ...
	def MayBeModified(self) -> bool: ...
	def NbAttributes(self) -> int: ...
	def NbChildren(self) -> int: ...
	def NewChild(self) -> TDF_Label: ...
	def Nullify(self) -> None: ...
	def ResumeAttribute(self, anAttribute: TDF_Attribute) -> None: ...
	def Root(self) -> TDF_Label: ...
	def Tag(self) -> int: ...
	def Transaction(self) -> int: ...

class TDF_LabelMapHasher:
	@staticmethod
	def HashCode(self, theLabel: TDF_Label, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, aLab1: TDF_Label, aLab2: TDF_Label) -> bool: ...

class TDF_RelocationTable(Standard_Transient):
	def __init__(self, selfRelocate: Optional[bool]) -> None: ...
	@overload
	def AfterRelocate(self, afterRelocate: bool) -> None: ...
	@overload
	def AfterRelocate(self) -> bool: ...
	def AttributeTable(self) -> TDF_AttributeDataMap: ...
	def Clear(self) -> None: ...
	@overload
	def HasRelocation(self, aSourceLabel: TDF_Label, aTargetLabel: TDF_Label) -> bool: ...
	@overload
	def HasRelocation(self, aSourceAttribute: TDF_Attribute, aTargetAttribute: TDF_Attribute) -> bool: ...
	def HasTransientRelocation(self, aSourceTransient: Standard_Transient, aTargetTransient: Standard_Transient) -> bool: ...
	def LabelTable(self) -> TDF_LabelDataMap: ...
	@overload
	def SelfRelocate(self, selfRelocate: bool) -> None: ...
	@overload
	def SelfRelocate(self) -> bool: ...
	@overload
	def SetRelocation(self, aSourceLabel: TDF_Label, aTargetLabel: TDF_Label) -> None: ...
	@overload
	def SetRelocation(self, aSourceAttribute: TDF_Attribute, aTargetAttribute: TDF_Attribute) -> None: ...
	def SetTransientRelocation(self, aSourceTransient: Standard_Transient, aTargetTransient: Standard_Transient) -> None: ...
	def TargetAttributeMap(self, anAttributeMap: TDF_AttributeMap) -> None: ...
	def TargetLabelMap(self, aLabelMap: TDF_LabelMap) -> None: ...
	def TransientTable(self) -> TColStd_IndexedDataMapOfTransientTransient: ...

class TDF_Tool:
	@staticmethod
	def CountLabels(self, aLabelList: TDF_LabelList, aLabelMap: TDF_LabelIntegerMap) -> None: ...
	@staticmethod
	def DeductLabels(self, aLabelList: TDF_LabelList, aLabelMap: TDF_LabelIntegerMap) -> None: ...
	@staticmethod
	def Entry(self, aLabel: TDF_Label, anEntry: TCollection_AsciiString) -> None: ...
	@overload
	@staticmethod
	def IsSelfContained(self, aLabel: TDF_Label) -> bool: ...
	@overload
	@staticmethod
	def IsSelfContained(self, aLabel: TDF_Label, aFilter: TDF_IDFilter) -> bool: ...
	@overload
	@staticmethod
	def Label(self, aDF: TDF_Data, anEntry: TCollection_AsciiString, aLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def Label(self, aDF: TDF_Data, anEntry: str, aLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def Label(self, aDF: TDF_Data, aTagList: TColStd_ListOfInteger, aLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def NbAttributes(self, aLabel: TDF_Label) -> int: ...
	@overload
	@staticmethod
	def NbAttributes(self, aLabel: TDF_Label, aFilter: TDF_IDFilter) -> int: ...
	@staticmethod
	def NbLabels(self, aLabel: TDF_Label) -> int: ...
	@overload
	@staticmethod
	def OutReferences(self, aLabel: TDF_Label, atts: TDF_AttributeMap) -> None: ...
	@overload
	@staticmethod
	def OutReferences(self, aLabel: TDF_Label, aFilterForReferers: TDF_IDFilter, aFilterForReferences: TDF_IDFilter, atts: TDF_AttributeMap) -> None: ...
	@overload
	@staticmethod
	def OutReferers(self, theLabel: TDF_Label, theAtts: TDF_AttributeMap) -> None: ...
	@overload
	@staticmethod
	def OutReferers(self, aLabel: TDF_Label, aFilterForReferers: TDF_IDFilter, aFilterForReferences: TDF_IDFilter, atts: TDF_AttributeMap) -> None: ...
	@staticmethod
	def RelocateLabel(self, aSourceLabel: TDF_Label, fromRoot: TDF_Label, toRoot: TDF_Label, aTargetLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def TagList(self, aLabel: TDF_Label, aTagList: TColStd_ListOfInteger) -> None: ...
	@overload
	@staticmethod
	def TagList(self, anEntry: TCollection_AsciiString, aTagList: TColStd_ListOfInteger) -> None: ...

class TDF_Transaction:
	@overload
	def __init__(self, aName: Optional[TCollection_AsciiString]) -> None: ...
	@overload
	def __init__(self, aDF: TDF_Data, aName: Optional[TCollection_AsciiString]) -> None: ...
	def Abort(self) -> None: ...
	def Commit(self, withDelta: Optional[bool]) -> TDF_Delta: ...
	def Data(self) -> TDF_Data: ...
	def Initialize(self, aDF: TDF_Data) -> None: ...
	def IsOpen(self) -> bool: ...
	def Name(self) -> TCollection_AsciiString: ...
	def Open(self) -> int: ...
	def Transaction(self) -> int: ...

class TDF_DeltaOnAddition(TDF_AttributeDelta):
	def __init__(self, anAtt: TDF_Attribute) -> None: ...
	def Apply(self) -> None: ...

class TDF_DeltaOnForget(TDF_AttributeDelta):
	def __init__(self, anAtt: TDF_Attribute) -> None: ...
	def Apply(self) -> None: ...

class TDF_DeltaOnModification(TDF_AttributeDelta):
	def Apply(self) -> None: ...

class TDF_DeltaOnRemoval(TDF_AttributeDelta):
	pass

class TDF_DeltaOnResume(TDF_AttributeDelta):
	def __init__(self, anAtt: TDF_Attribute) -> None: ...
	def Apply(self) -> None: ...

class TDF_Reference(TDF_Attribute):
	def __init__(self) -> None: ...
	def Get(self) -> TDF_Label: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def References(self, DS: TDF_DataSet) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(self, I: TDF_Label, Origin: TDF_Label) -> TDF_Reference: ...
	@overload
	def Set(self, Origin: TDF_Label) -> None: ...

class TDF_TagSource(TDF_Attribute):
	def __init__(self) -> None: ...
	def Get(self) -> int: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@overload
	@staticmethod
	def NewChild(self, L: TDF_Label) -> TDF_Label: ...
	@overload
	def NewChild(self) -> TDF_Label: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def NewTag(self) -> int: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def Restore(self, with_: TDF_Attribute) -> None: ...
	@overload
	@staticmethod
	def Set(self, label: TDF_Label) -> TDF_TagSource: ...
	@overload
	def Set(self, T: int) -> None: ...

class TDF_DefaultDeltaOnModification(TDF_DeltaOnModification):
	def __init__(self, anAttribute: TDF_Attribute) -> None: ...
	def Apply(self) -> None: ...

class TDF_DefaultDeltaOnRemoval(TDF_DeltaOnRemoval):
	def __init__(self, anAttribute: TDF_Attribute) -> None: ...
	def Apply(self) -> None: ...

#classnotwrapped
class TDF_LabelNode: ...

# harray1 classes

class TDF_HAttributeArray1(TDF_AttributeArray1, Standard_Transient):
    def TDF_HAttributeArray1(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TDF_AttributeArray1: ...

# harray2 classes
# hsequence classes

tdf_AddLinkGUIDToProgID = tdf.AddLinkGUIDToProgID
tdf_GUIDFromProgID = tdf.GUIDFromProgID
tdf_LowestID = tdf.LowestID
tdf_ProgIDFromGUID = tdf.ProgIDFromGUID
tdf_UppestID = tdf.UppestID
TDF_ClosureTool_Closure = TDF_ClosureTool.Closure
TDF_ClosureTool_Closure = TDF_ClosureTool.Closure
TDF_ClosureTool_Closure = TDF_ClosureTool.Closure
TDF_ComparisonTool_Compare = TDF_ComparisonTool.Compare
TDF_ComparisonTool_Cut = TDF_ComparisonTool.Cut
TDF_ComparisonTool_IsSelfContained = TDF_ComparisonTool.IsSelfContained
TDF_ComparisonTool_SourceUnbound = TDF_ComparisonTool.SourceUnbound
TDF_ComparisonTool_TargetUnbound = TDF_ComparisonTool.TargetUnbound
TDF_CopyLabel_ExternalReferences = TDF_CopyLabel.ExternalReferences
TDF_CopyLabel_ExternalReferences = TDF_CopyLabel.ExternalReferences
TDF_CopyTool_Copy = TDF_CopyTool.Copy
TDF_CopyTool_Copy = TDF_CopyTool.Copy
TDF_CopyTool_Copy = TDF_CopyTool.Copy
TDF_LabelMapHasher_HashCode = TDF_LabelMapHasher.HashCode
TDF_LabelMapHasher_IsEqual = TDF_LabelMapHasher.IsEqual
TDF_Tool_CountLabels = TDF_Tool.CountLabels
TDF_Tool_DeductLabels = TDF_Tool.DeductLabels
TDF_Tool_DeepDump = TDF_Tool.DeepDump
TDF_Tool_DeepDump = TDF_Tool.DeepDump
TDF_Tool_Entry = TDF_Tool.Entry
TDF_Tool_ExtendedDeepDump = TDF_Tool.ExtendedDeepDump
TDF_Tool_ExtendedDeepDump = TDF_Tool.ExtendedDeepDump
TDF_Tool_IsSelfContained = TDF_Tool.IsSelfContained
TDF_Tool_IsSelfContained = TDF_Tool.IsSelfContained
TDF_Tool_Label = TDF_Tool.Label
TDF_Tool_Label = TDF_Tool.Label
TDF_Tool_Label = TDF_Tool.Label
TDF_Tool_NbAttributes = TDF_Tool.NbAttributes
TDF_Tool_NbAttributes = TDF_Tool.NbAttributes
TDF_Tool_NbLabels = TDF_Tool.NbLabels
TDF_Tool_OutReferences = TDF_Tool.OutReferences
TDF_Tool_OutReferences = TDF_Tool.OutReferences
TDF_Tool_OutReferers = TDF_Tool.OutReferers
TDF_Tool_OutReferers = TDF_Tool.OutReferers
TDF_Tool_RelocateLabel = TDF_Tool.RelocateLabel
TDF_Tool_TagList = TDF_Tool.TagList
TDF_Tool_TagList = TDF_Tool.TagList
TDF_Reference_GetID = TDF_Reference.GetID
TDF_Reference_Set = TDF_Reference.Set
TDF_TagSource_GetID = TDF_TagSource.GetID
TDF_TagSource_NewChild = TDF_TagSource.NewChild
TDF_TagSource_Set = TDF_TagSource.Set
