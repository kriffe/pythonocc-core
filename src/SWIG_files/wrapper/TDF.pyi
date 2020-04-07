from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *

TDF_LabelNodePtr = NewType('TDF_LabelNodePtr', TDF_LabelNode)

class TDF:
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
	def DeltaOnModification(self, anOldAttribute: TDF_Attribute) -> TDF_DeltaOnModification: ...
	def DeltaOnModification(self, aDelta: TDF_DeltaOnModification) -> None: ...
	def DeltaOnRemoval(self) -> TDF_DeltaOnRemoval: ...
	def DeltaOnResume(self) -> TDF_DeltaOnResume: ...
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
	def Descendants(self, aStatus: bool) -> None: ...
	def Descendants(self) -> bool: ...
	def References(self, aStatus: bool) -> None: ...
	def References(self) -> bool: ...

class TDF_ClosureTool:
	@staticmethod
	def Closure(self, aDataSet: TDF_DataSet) -> None: ...
	@staticmethod
	def Closure(self, aDataSet: TDF_DataSet, aFilter: TDF_IDFilter, aMode: TDF_ClosureMode) -> None: ...
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
	@staticmethod
	def ExternalReferences(self, Lab: TDF_Label, aExternals: TDF_AttributeMap, aFilter: TDF_IDFilter) -> bool: ...
	@staticmethod
	def ExternalReferences(self, aRefLab: TDF_Label, Lab: TDF_Label, aExternals: TDF_AttributeMap, aFilter: TDF_IDFilter, aDataSet: TDF_DataSet) -> None: ...
	def IsDone(self) -> bool: ...
	def Load(self, aSource: TDF_Label, aTarget: TDF_Label) -> None: ...
	def Perform(self) -> None: ...
	def RelocationTable(self) -> TDF_RelocationTable: ...
	def UseFilter(self, aFilter: TDF_IDFilter) -> None: ...

class TDF_CopyTool:
	@staticmethod
	def Copy(self, aSourceDataSet: TDF_DataSet, aRelocationTable: TDF_RelocationTable) -> None: ...
	@staticmethod
	def Copy(self, aSourceDataSet: TDF_DataSet, aRelocationTable: TDF_RelocationTable, aPrivilegeFilter: TDF_IDFilter) -> None: ...
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
	def Ignore(self, anID: Standard_GUID) -> None: ...
	def Ignore(self, anIDList: TDF_IDList) -> None: ...
	def IgnoreAll(self, ignore: bool) -> None: ...
	def IgnoreAll(self) -> bool: ...
	def IsIgnored(self, anID: Standard_GUID) -> bool: ...
	def IsIgnored(self, anAtt: TDF_Attribute) -> bool: ...
	def IsKept(self, anID: Standard_GUID) -> bool: ...
	def IsKept(self, anAtt: TDF_Attribute) -> bool: ...
	def Keep(self, anID: Standard_GUID) -> None: ...
	def Keep(self, anIDList: TDF_IDList) -> None: ...

class TDF_Label:
	def __init__(self) -> None: ...
	def AddAttribute(self, anAttribute: TDF_Attribute, append: Optional[bool]) -> None: ...
	def AttributesModified(self) -> bool: ...
	def Data(self) -> TDF_Data: ...
	def Depth(self) -> int: ...
	def Father(self) -> TDF_Label: ...
	def FindAttribute(self, anID: Standard_GUID, anAttribute: TDF_Attribute) -> bool: ...
	def FindAttribute(self, anID: Standard_GUID, aTransaction: int, anAttribute: TDF_Attribute) -> bool: ...
	def FindChild(self, aTag: int, create: Optional[bool]) -> TDF_Label: ...
	def ForgetAllAttributes(self, clearChildren: Optional[bool]) -> None: ...
	def ForgetAttribute(self, anAttribute: TDF_Attribute) -> None: ...
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
	def AfterRelocate(self, afterRelocate: bool) -> None: ...
	def AfterRelocate(self) -> bool: ...
	def AttributeTable(self) -> TDF_AttributeDataMap: ...
	def Clear(self) -> None: ...
	def HasRelocation(self, aSourceLabel: TDF_Label, aTargetLabel: TDF_Label) -> bool: ...
	def HasRelocation(self, aSourceAttribute: TDF_Attribute, aTargetAttribute: TDF_Attribute) -> bool: ...
	def HasTransientRelocation(self, aSourceTransient: Standard_Transient, aTargetTransient: Standard_Transient) -> bool: ...
	def LabelTable(self) -> TDF_LabelDataMap: ...
	def SelfRelocate(self, selfRelocate: bool) -> None: ...
	def SelfRelocate(self) -> bool: ...
	def SetRelocation(self, aSourceLabel: TDF_Label, aTargetLabel: TDF_Label) -> None: ...
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
	@staticmethod
	def IsSelfContained(self, aLabel: TDF_Label) -> bool: ...
	@staticmethod
	def IsSelfContained(self, aLabel: TDF_Label, aFilter: TDF_IDFilter) -> bool: ...
	@staticmethod
	def Label(self, aDF: TDF_Data, anEntry: TCollection_AsciiString, aLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@staticmethod
	def Label(self, aDF: TDF_Data, anEntry: str, aLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@staticmethod
	def Label(self, aDF: TDF_Data, aTagList: TColStd_ListOfInteger, aLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@staticmethod
	def NbAttributes(self, aLabel: TDF_Label) -> int: ...
	@staticmethod
	def NbAttributes(self, aLabel: TDF_Label, aFilter: TDF_IDFilter) -> int: ...
	@staticmethod
	def NbLabels(self, aLabel: TDF_Label) -> int: ...
	@staticmethod
	def OutReferences(self, aLabel: TDF_Label, atts: TDF_AttributeMap) -> None: ...
	@staticmethod
	def OutReferences(self, aLabel: TDF_Label, aFilterForReferers: TDF_IDFilter, aFilterForReferences: TDF_IDFilter, atts: TDF_AttributeMap) -> None: ...
	@staticmethod
	def OutReferers(self, theLabel: TDF_Label, theAtts: TDF_AttributeMap) -> None: ...
	@staticmethod
	def OutReferers(self, aLabel: TDF_Label, aFilterForReferers: TDF_IDFilter, aFilterForReferences: TDF_IDFilter, atts: TDF_AttributeMap) -> None: ...
	@staticmethod
	def RelocateLabel(self, aSourceLabel: TDF_Label, fromRoot: TDF_Label, toRoot: TDF_Label, aTargetLabel: TDF_Label, create: Optional[bool]) -> None: ...
	@staticmethod
	def TagList(self, aLabel: TDF_Label, aTagList: TColStd_ListOfInteger) -> None: ...
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
	@staticmethod
	def Set(self, I: TDF_Label, Origin: TDF_Label) -> TDF_Reference: ...
	def Set(self, Origin: TDF_Label) -> None: ...

class TDF_TagSource(TDF_Attribute):
	def __init__(self) -> None: ...
	def Get(self) -> int: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@staticmethod
	def NewChild(self, L: TDF_Label) -> TDF_Label: ...
	def NewChild(self) -> TDF_Label: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def NewTag(self) -> int: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def Restore(self, with_: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDF_TagSource: ...
	def Set(self, T: int) -> None: ...

class TDF_DefaultDeltaOnModification(TDF_DeltaOnModification):
	def __init__(self, anAttribute: TDF_Attribute) -> None: ...
	def Apply(self) -> None: ...

class TDF_DefaultDeltaOnRemoval(TDF_DeltaOnRemoval):
	def __init__(self, anAttribute: TDF_Attribute) -> None: ...
	def Apply(self) -> None: ...

#classnotwrapped
class TDF_LabelNode:
	pass
