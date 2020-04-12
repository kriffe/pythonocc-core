from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepBasic import *
from OCC.Core.TCollection import *
from OCC.Core.StepVisual import *
from OCC.Core.StepData import *
from OCC.Core.StepRepr import *
from OCC.Core.StepShape import *
from OCC.Core.StepGeom import *
from OCC.Core.Interface import *


class StepAP214_Array1OfApprovalItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_ApprovalItem: ...
    def __setitem__(self, index: int, value: StepAP214_ApprovalItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_ApprovalItem]:
    def next(self) -> StepAP214_ApprovalItem: ...
    __next__ = next

class StepAP214_Array1OfAutoDesignDateAndPersonItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_AutoDesignDateAndPersonItem: ...
    def __setitem__(self, index: int, value: StepAP214_AutoDesignDateAndPersonItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_AutoDesignDateAndPersonItem]:
    def next(self) -> StepAP214_AutoDesignDateAndPersonItem: ...
    __next__ = next

class StepAP214_Array1OfAutoDesignDateAndTimeItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_AutoDesignDateAndTimeItem: ...
    def __setitem__(self, index: int, value: StepAP214_AutoDesignDateAndTimeItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_AutoDesignDateAndTimeItem]:
    def next(self) -> StepAP214_AutoDesignDateAndTimeItem: ...
    __next__ = next

class StepAP214_Array1OfAutoDesignDatedItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_AutoDesignDatedItem: ...
    def __setitem__(self, index: int, value: StepAP214_AutoDesignDatedItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_AutoDesignDatedItem]:
    def next(self) -> StepAP214_AutoDesignDatedItem: ...
    __next__ = next

class StepAP214_Array1OfAutoDesignGeneralOrgItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_AutoDesignGeneralOrgItem: ...
    def __setitem__(self, index: int, value: StepAP214_AutoDesignGeneralOrgItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_AutoDesignGeneralOrgItem]:
    def next(self) -> StepAP214_AutoDesignGeneralOrgItem: ...
    __next__ = next

class StepAP214_Array1OfAutoDesignGroupedItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_AutoDesignGroupedItem: ...
    def __setitem__(self, index: int, value: StepAP214_AutoDesignGroupedItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_AutoDesignGroupedItem]:
    def next(self) -> StepAP214_AutoDesignGroupedItem: ...
    __next__ = next

class StepAP214_Array1OfAutoDesignPresentedItemSelect:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_AutoDesignPresentedItemSelect: ...
    def __setitem__(self, index: int, value: StepAP214_AutoDesignPresentedItemSelect) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_AutoDesignPresentedItemSelect]:
    def next(self) -> StepAP214_AutoDesignPresentedItemSelect: ...
    __next__ = next

class StepAP214_Array1OfAutoDesignReferencingItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_AutoDesignReferencingItem: ...
    def __setitem__(self, index: int, value: StepAP214_AutoDesignReferencingItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_AutoDesignReferencingItem]:
    def next(self) -> StepAP214_AutoDesignReferencingItem: ...
    __next__ = next

class StepAP214_Array1OfDateAndTimeItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_DateAndTimeItem: ...
    def __setitem__(self, index: int, value: StepAP214_DateAndTimeItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_DateAndTimeItem]:
    def next(self) -> StepAP214_DateAndTimeItem: ...
    __next__ = next

class StepAP214_Array1OfDateItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_DateItem: ...
    def __setitem__(self, index: int, value: StepAP214_DateItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_DateItem]:
    def next(self) -> StepAP214_DateItem: ...
    __next__ = next

class StepAP214_Array1OfDocumentReferenceItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_DocumentReferenceItem: ...
    def __setitem__(self, index: int, value: StepAP214_DocumentReferenceItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_DocumentReferenceItem]:
    def next(self) -> StepAP214_DocumentReferenceItem: ...
    __next__ = next

class StepAP214_Array1OfExternalIdentificationItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_ExternalIdentificationItem: ...
    def __setitem__(self, index: int, value: StepAP214_ExternalIdentificationItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_ExternalIdentificationItem]:
    def next(self) -> StepAP214_ExternalIdentificationItem: ...
    __next__ = next

class StepAP214_Array1OfGroupItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_GroupItem: ...
    def __setitem__(self, index: int, value: StepAP214_GroupItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_GroupItem]:
    def next(self) -> StepAP214_GroupItem: ...
    __next__ = next

class StepAP214_Array1OfOrganizationItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_OrganizationItem: ...
    def __setitem__(self, index: int, value: StepAP214_OrganizationItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_OrganizationItem]:
    def next(self) -> StepAP214_OrganizationItem: ...
    __next__ = next

class StepAP214_Array1OfPersonAndOrganizationItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_PersonAndOrganizationItem: ...
    def __setitem__(self, index: int, value: StepAP214_PersonAndOrganizationItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_PersonAndOrganizationItem]:
    def next(self) -> StepAP214_PersonAndOrganizationItem: ...
    __next__ = next

class StepAP214_Array1OfPresentedItemSelect:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_PresentedItemSelect: ...
    def __setitem__(self, index: int, value: StepAP214_PresentedItemSelect) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_PresentedItemSelect]:
    def next(self) -> StepAP214_PresentedItemSelect: ...
    __next__ = next

class StepAP214_Array1OfSecurityClassificationItem:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> StepAP214_SecurityClassificationItem: ...
    def __setitem__(self, index: int, value: StepAP214_SecurityClassificationItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP214_SecurityClassificationItem]:
    def next(self) -> StepAP214_SecurityClassificationItem: ...
    __next__ = next

class StepAP214:
	@staticmethod
	def Protocol(self) -> StepAP214_Protocol: ...

class StepAP214_AppliedApprovalAssignment(StepBasic_ApprovalAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedApproval: StepBasic_Approval, aItems: StepAP214_HArray1OfApprovalItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfApprovalItem: ...
	def ItemsValue(self, num: int) -> StepAP214_ApprovalItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfApprovalItem) -> None: ...

class StepAP214_AppliedDateAndTimeAssignment(StepBasic_DateAndTimeAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDateAndTime: StepBasic_DateAndTime, aRole: StepBasic_DateTimeRole, aItems: StepAP214_HArray1OfDateAndTimeItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfDateAndTimeItem: ...
	def ItemsValue(self, num: int) -> StepAP214_DateAndTimeItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfDateAndTimeItem) -> None: ...

class StepAP214_AppliedDateAssignment(StepBasic_DateAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDate: StepBasic_Date, aRole: StepBasic_DateRole, aItems: StepAP214_HArray1OfDateItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfDateItem: ...
	def ItemsValue(self, num: int) -> StepAP214_DateItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfDateItem) -> None: ...

class StepAP214_AppliedDocumentReference(StepBasic_DocumentReference):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDocument: StepBasic_Document, aSource: TCollection_HAsciiString, aItems: StepAP214_HArray1OfDocumentReferenceItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfDocumentReferenceItem: ...
	def ItemsValue(self, num: int) -> StepAP214_DocumentReferenceItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfDocumentReferenceItem) -> None: ...

class StepAP214_AppliedExternalIdentificationAssignment(StepBasic_ExternalIdentificationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aIdentificationAssignment_AssignedId: TCollection_HAsciiString, aIdentificationAssignment_Role: StepBasic_IdentificationRole, aExternalIdentificationAssignment_Source: StepBasic_ExternalSource, aItems: StepAP214_HArray1OfExternalIdentificationItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfExternalIdentificationItem: ...
	def SetItems(self, Items: StepAP214_HArray1OfExternalIdentificationItem) -> None: ...

class StepAP214_AppliedGroupAssignment(StepBasic_GroupAssignment):
	def __init__(self) -> None: ...
	def Init(self, aGroupAssignment_AssignedGroup: StepBasic_Group, aItems: StepAP214_HArray1OfGroupItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfGroupItem: ...
	def SetItems(self, Items: StepAP214_HArray1OfGroupItem) -> None: ...

class StepAP214_AppliedOrganizationAssignment(StepBasic_OrganizationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedOrganization: StepBasic_Organization, aRole: StepBasic_OrganizationRole, aItems: StepAP214_HArray1OfOrganizationItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfOrganizationItem: ...
	def ItemsValue(self, num: int) -> StepAP214_OrganizationItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfOrganizationItem) -> None: ...

class StepAP214_AppliedPersonAndOrganizationAssignment(StepBasic_PersonAndOrganizationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedPersonAndOrganization: StepBasic_PersonAndOrganization, aRole: StepBasic_PersonAndOrganizationRole, aItems: StepAP214_HArray1OfPersonAndOrganizationItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfPersonAndOrganizationItem: ...
	def ItemsValue(self, num: int) -> StepAP214_PersonAndOrganizationItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfPersonAndOrganizationItem) -> None: ...

class StepAP214_AppliedPresentedItem(StepVisual_PresentedItem):
	def __init__(self) -> None: ...
	def Init(self, aItems: StepAP214_HArray1OfPresentedItemSelect) -> None: ...
	def Items(self) -> StepAP214_HArray1OfPresentedItemSelect: ...
	def ItemsValue(self, num: int) -> StepAP214_PresentedItemSelect: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfPresentedItemSelect) -> None: ...

class StepAP214_AppliedSecurityClassificationAssignment(StepBasic_SecurityClassificationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedSecurityClassification: StepBasic_SecurityClassification, aItems: StepAP214_HArray1OfSecurityClassificationItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfSecurityClassificationItem: ...
	def ItemsValue(self, num: int) -> StepAP214_SecurityClassificationItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfSecurityClassificationItem) -> None: ...

class StepAP214_ApprovalItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AssemblyComponentUsageSubstitute(self) -> StepRepr_AssemblyComponentUsageSubstitute: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ConfigurationItem(self) -> StepRepr_ConfigurationItem: ...
	def Date(self) -> StepBasic_Date: ...
	def Document(self) -> StepBasic_Document: ...
	def DocumentFile(self) -> StepBasic_DocumentFile: ...
	def Effectivity(self) -> StepBasic_Effectivity: ...
	def Group(self) -> StepBasic_Group: ...
	def GroupRelationship(self) -> StepBasic_GroupRelationship: ...
	def MaterialDesignation(self) -> StepRepr_MaterialDesignation: ...
	def MechanicalDesignGeometricPresentationRepresentation(self) -> StepVisual_MechanicalDesignGeometricPresentationRepresentation: ...
	def PresentationArea(self) -> StepVisual_PresentationArea: ...
	def Product(self) -> StepBasic_Product: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
	def ProductDefinitionFormationRelationship(self) -> StepBasic_ProductDefinitionFormationRelationship: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def PropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def Representation(self) -> StepRepr_Representation: ...
	def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...
	def ShapeRepresentation(self) -> StepShape_ShapeRepresentation: ...

class StepAP214_AutoDesignActualDateAndTimeAssignment(StepBasic_DateAndTimeAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDateAndTime: StepBasic_DateAndTime, aRole: StepBasic_DateTimeRole, aItems: StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignDateAndTimeItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignDateAndTimeItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: ...

class StepAP214_AutoDesignActualDateAssignment(StepBasic_DateAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDate: StepBasic_Date, aRole: StepBasic_DateRole, aItems: StepAP214_HArray1OfAutoDesignDatedItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignDatedItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignDatedItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignDatedItem) -> None: ...

class StepAP214_AutoDesignApprovalAssignment(StepBasic_ApprovalAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedApproval: StepBasic_Approval, aItems: StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignGeneralOrgItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignGeneralOrgItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: ...

class StepAP214_AutoDesignDateAndPersonAssignment(StepBasic_PersonAndOrganizationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedPersonAndOrganization: StepBasic_PersonAndOrganization, aRole: StepBasic_PersonAndOrganizationRole, aItems: StepAP214_HArray1OfAutoDesignDateAndPersonItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignDateAndPersonItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignDateAndPersonItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignDateAndPersonItem) -> None: ...

class StepAP214_AutoDesignDateAndPersonItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AutoDesignDocumentReference(self) -> StepAP214_AutoDesignDocumentReference: ...
	def AutoDesignOrganizationAssignment(self) -> StepAP214_AutoDesignOrganizationAssignment: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ExternallyDefinedRepresentation(self) -> StepRepr_ExternallyDefinedRepresentation: ...
	def Product(self) -> StepBasic_Product: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def ProductDefinitionWithAssociatedDocuments(self) -> StepBasic_ProductDefinitionWithAssociatedDocuments: ...
	def Representation(self) -> StepRepr_Representation: ...

class StepAP214_AutoDesignDateAndTimeItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApprovalPersonOrganization(self) -> StepBasic_ApprovalPersonOrganization: ...
	def AutoDesignDateAndPersonAssignment(self) -> StepAP214_AutoDesignDateAndPersonAssignment: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionEffectivity(self) -> StepBasic_ProductDefinitionEffectivity: ...

class StepAP214_AutoDesignDatedItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApprovalPersonOrganization(self) -> StepBasic_ApprovalPersonOrganization: ...
	def AutoDesignDateAndPersonAssignment(self) -> StepAP214_AutoDesignDateAndPersonAssignment: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionEffectivity(self) -> StepBasic_ProductDefinitionEffectivity: ...

class StepAP214_AutoDesignDocumentReference(StepBasic_DocumentReference):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDocument: StepBasic_Document, aSource: TCollection_HAsciiString, aItems: StepAP214_HArray1OfAutoDesignReferencingItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignReferencingItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignReferencingItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignReferencingItem) -> None: ...

class StepAP214_AutoDesignGeneralOrgItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AutoDesignDocumentReference(self) -> StepAP214_AutoDesignDocumentReference: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ExternallyDefinedRepresentation(self) -> StepRepr_ExternallyDefinedRepresentation: ...
	def Product(self) -> StepBasic_Product: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def ProductDefinitionWithAssociatedDocuments(self) -> StepBasic_ProductDefinitionWithAssociatedDocuments: ...
	def Representation(self) -> StepRepr_Representation: ...

class StepAP214_AutoDesignGroupAssignment(StepBasic_GroupAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedGroup: StepBasic_Group, aItems: StepAP214_HArray1OfAutoDesignGroupedItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignGroupedItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignGroupedItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignGroupedItem) -> None: ...

class StepAP214_AutoDesignGroupedItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AdvancedBrepShapeRepresentation(self) -> StepShape_AdvancedBrepShapeRepresentation: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CsgShapeRepresentation(self) -> StepShape_CsgShapeRepresentation: ...
	def FacetedBrepShapeRepresentation(self) -> StepShape_FacetedBrepShapeRepresentation: ...
	def GeometricallyBoundedSurfaceShapeRepresentation(self) -> StepShape_GeometricallyBoundedSurfaceShapeRepresentation: ...
	def GeometricallyBoundedWireframeShapeRepresentation(self) -> StepShape_GeometricallyBoundedWireframeShapeRepresentation: ...
	def ManifoldSurfaceShapeRepresentation(self) -> StepShape_ManifoldSurfaceShapeRepresentation: ...
	def Representation(self) -> StepRepr_Representation: ...
	def RepresentationItem(self) -> StepRepr_RepresentationItem: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeRepresentation(self) -> StepShape_ShapeRepresentation: ...
	def TemplateInstance(self) -> StepVisual_TemplateInstance: ...

class StepAP214_AutoDesignNominalDateAndTimeAssignment(StepBasic_DateAndTimeAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDateAndTime: StepBasic_DateAndTime, aRole: StepBasic_DateTimeRole, aItems: StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignDateAndTimeItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignDateAndTimeItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignDateAndTimeItem) -> None: ...

class StepAP214_AutoDesignNominalDateAssignment(StepBasic_DateAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedDate: StepBasic_Date, aRole: StepBasic_DateRole, aItems: StepAP214_HArray1OfAutoDesignDatedItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignDatedItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignDatedItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignDatedItem) -> None: ...

class StepAP214_AutoDesignOrganizationAssignment(StepBasic_OrganizationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedOrganization: StepBasic_Organization, aRole: StepBasic_OrganizationRole, aItems: StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignGeneralOrgItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignGeneralOrgItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: ...

class StepAP214_AutoDesignPersonAndOrganizationAssignment(StepBasic_PersonAndOrganizationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedPersonAndOrganization: StepBasic_PersonAndOrganization, aRole: StepBasic_PersonAndOrganizationRole, aItems: StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignGeneralOrgItem: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignGeneralOrgItem: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignGeneralOrgItem) -> None: ...

class StepAP214_AutoDesignPresentedItem(StepVisual_PresentedItem):
	def __init__(self) -> None: ...
	def Init(self, aItems: StepAP214_HArray1OfAutoDesignPresentedItemSelect) -> None: ...
	def Items(self) -> StepAP214_HArray1OfAutoDesignPresentedItemSelect: ...
	def ItemsValue(self, num: int) -> StepAP214_AutoDesignPresentedItemSelect: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepAP214_HArray1OfAutoDesignPresentedItemSelect) -> None: ...

class StepAP214_AutoDesignPresentedItemSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DocumentRelationship(self) -> StepBasic_DocumentRelationship: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape: ...
	def RepresentationRelationship(self) -> StepRepr_RepresentationRelationship: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...

class StepAP214_AutoDesignReferencingItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def Approval(self) -> StepBasic_Approval: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DocumentRelationship(self) -> StepBasic_DocumentRelationship: ...
	def ExternallyDefinedRepresentation(self) -> StepRepr_ExternallyDefinedRepresentation: ...
	def MappedItem(self) -> StepRepr_MappedItem: ...
	def MaterialDesignation(self) -> StepRepr_MaterialDesignation: ...
	def PresentationArea(self) -> StepVisual_PresentationArea: ...
	def PresentationView(self) -> StepVisual_PresentationView: ...
	def ProductCategory(self) -> StepBasic_ProductCategory: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def PropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def Representation(self) -> StepRepr_Representation: ...
	def RepresentationRelationship(self) -> StepRepr_RepresentationRelationship: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...

class StepAP214_AutoDesignSecurityClassificationAssignment(StepBasic_SecurityClassificationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aAssignedSecurityClassification: StepBasic_SecurityClassification, aItems: StepBasic_HArray1OfApproval) -> None: ...
	def Items(self) -> StepBasic_HArray1OfApproval: ...
	def ItemsValue(self, num: int) -> StepBasic_Approval: ...
	def NbItems(self) -> int: ...
	def SetItems(self, aItems: StepBasic_HArray1OfApproval) -> None: ...

class StepAP214_Class(StepBasic_Group):
	def __init__(self) -> None: ...

class StepAP214_DocumentReferenceItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AppliedExternalIdentificationAssignment(self) -> StepAP214_AppliedExternalIdentificationAssignment: ...
	def Approval(self) -> StepBasic_Approval: ...
	def AssemblyComponentUsage(self) -> StepRepr_AssemblyComponentUsage: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CharacterizedObject(self) -> StepBasic_CharacterizedObject: ...
	def DescriptiveRepresentationItem(self) -> StepRepr_DescriptiveRepresentationItem: ...
	def DimensionalSize(self) -> StepShape_DimensionalSize: ...
	def ExternallyDefinedItem(self) -> StepBasic_ExternallyDefinedItem: ...
	def Group(self) -> StepBasic_Group: ...
	def GroupRelationship(self) -> StepBasic_GroupRelationship: ...
	def MaterialDesignation(self) -> StepRepr_MaterialDesignation: ...
	def MeasureRepresentationItem(self) -> StepRepr_MeasureRepresentationItem: ...
	def ProductCategory(self) -> StepBasic_ProductCategory: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionContext(self) -> StepBasic_ProductDefinitionContext: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def PropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def Representation(self) -> StepRepr_Representation: ...
	def RepresentationItem(self) -> StepRepr_RepresentationItem: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...

class StepAP214_ExternalIdentificationItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: ...
	def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment: ...
	def Approval(self) -> StepBasic_Approval: ...
	def ApprovalStatus(self) -> StepBasic_ApprovalStatus: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DateAndTimeAssignment(self) -> StepBasic_DateAndTimeAssignment: ...
	def DateAssignment(self) -> StepBasic_DateAssignment: ...
	def DocumentFile(self) -> StepBasic_DocumentFile: ...
	def ExternalSource(self) -> StepBasic_ExternalSource: ...
	def ExternallyDefinedClass(self) -> StepAP214_ExternallyDefinedClass: ...
	def ExternallyDefinedGeneralProperty(self) -> StepAP214_ExternallyDefinedGeneralProperty: ...
	def OrganizationalAddress(self) -> StepBasic_OrganizationalAddress: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
	def TrimmedCurve(self) -> StepGeom_TrimmedCurve: ...
	def VersionedActionRequest(self) -> StepBasic_VersionedActionRequest: ...

class StepAP214_ExternallyDefinedGeneralProperty(StepBasic_GeneralProperty):
	def __init__(self) -> None: ...
	def ExternallyDefinedItem(self) -> StepBasic_ExternallyDefinedItem: ...
	def Init(self, aGeneralProperty_Id: TCollection_HAsciiString, aGeneralProperty_Name: TCollection_HAsciiString, hasGeneralProperty_Description: bool, aGeneralProperty_Description: TCollection_HAsciiString, aExternallyDefinedItem_ItemId: StepBasic_SourceItem, aExternallyDefinedItem_Source: StepBasic_ExternalSource) -> None: ...
	def SetExternallyDefinedItem(self, ExternallyDefinedItem: StepBasic_ExternallyDefinedItem) -> None: ...

class StepAP214_GroupItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def GeometricRepresentationItem(self) -> StepGeom_GeometricRepresentationItem: ...
	def GroupRelationship(self) -> StepBasic_GroupRelationship: ...
	def MappedItem(self) -> StepRepr_MappedItem: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
	def PropertyDefinitionRepresentation(self) -> StepRepr_PropertyDefinitionRepresentation: ...
	def Representation(self) -> StepRepr_Representation: ...
	def RepresentationItem(self) -> StepRepr_RepresentationItem: ...
	def RepresentationRelationshipWithTransformation(self) -> StepRepr_RepresentationRelationshipWithTransformation: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...
	def ShapeRepresentationRelationship(self) -> StepRepr_ShapeRepresentationRelationship: ...
	def StyledItem(self) -> StepVisual_StyledItem: ...
	def TopologicalRepresentationItem(self) -> StepShape_TopologicalRepresentationItem: ...

class StepAP214_PresentedItemSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...

class StepAP214_Protocol(StepData_Protocol):
	def __init__(self) -> None: ...
	def NbResources(self) -> int: ...
	def Resource(self, num: int) -> Interface_Protocol: ...
	def SchemaName(self) -> str: ...
	def TypeNumber(self, atype: Standard_Type) -> int: ...

class StepAP214_RepItemGroup(StepBasic_Group):
	def __init__(self) -> None: ...
	def Init(self, aGroup_Name: TCollection_HAsciiString, hasGroup_Description: bool, aGroup_Description: TCollection_HAsciiString, aRepresentationItem_Name: TCollection_HAsciiString) -> None: ...
	def RepresentationItem(self) -> StepRepr_RepresentationItem: ...
	def SetRepresentationItem(self, RepresentationItem: StepRepr_RepresentationItem) -> None: ...

class StepAP214_AutoDesignOrganizationItem(StepAP214_AutoDesignGeneralOrgItem):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def Document(self) -> StepBasic_Document: ...
	def PhysicallyModeledProductDefinition(self) -> StepBasic_PhysicallyModeledProductDefinition: ...

class StepAP214_DateAndTimeItem(StepAP214_ApprovalItem):
	def __init__(self) -> None: ...
	def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: ...
	def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment: ...
	def ApprovalPersonOrganization(self) -> StepBasic_ApprovalPersonOrganization: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...

class StepAP214_DateItem(StepAP214_ApprovalItem):
	def __init__(self) -> None: ...
	def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: ...
	def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment: ...
	def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment: ...
	def ApprovalPersonOrganization(self) -> StepBasic_ApprovalPersonOrganization: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...

class StepAP214_ExternallyDefinedClass(StepAP214_Class):
	def __init__(self) -> None: ...
	def ExternallyDefinedItem(self) -> StepBasic_ExternallyDefinedItem: ...
	def Init(self, aGroup_Name: TCollection_HAsciiString, hasGroup_Description: bool, aGroup_Description: TCollection_HAsciiString, aExternallyDefinedItem_ItemId: StepBasic_SourceItem, aExternallyDefinedItem_Source: StepBasic_ExternalSource) -> None: ...
	def SetExternallyDefinedItem(self, ExternallyDefinedItem: StepBasic_ExternallyDefinedItem) -> None: ...

class StepAP214_OrganizationItem(StepAP214_ApprovalItem):
	def __init__(self) -> None: ...
	def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: ...
	def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment: ...
	def Approval(self) -> StepBasic_Approval: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...

class StepAP214_PersonAndOrganizationItem(StepAP214_ApprovalItem):
	def __init__(self) -> None: ...
	def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: ...
	def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment: ...
	def Approval(self) -> StepBasic_Approval: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...

class StepAP214_SecurityClassificationItem(StepAP214_ApprovalItem):
	def __init__(self) -> None: ...
	def Action(self) -> StepBasic_Action: ...
	def AssemblyComponentUsage(self) -> StepRepr_AssemblyComponentUsage: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ConfigurationDesign(self) -> StepRepr_ConfigurationDesign: ...
	def ConfigurationEffectivity(self) -> StepRepr_ConfigurationEffectivity: ...
	def DraughtingModel(self) -> StepVisual_DraughtingModel: ...
	def GeneralProperty(self) -> StepBasic_GeneralProperty: ...
	def MakeFromUsageOption(self) -> StepRepr_MakeFromUsageOption: ...
	def ProductConcept(self) -> StepRepr_ProductConcept: ...
	def ProductDefinitionUsage(self) -> StepRepr_ProductDefinitionUsage: ...
	def VersionedActionRequest(self) -> StepBasic_VersionedActionRequest: ...

# harray1 classes
class StepAP214_HArray1OfDateItem(StepAP214_Array1OfDateItem, Standard_Transient): ...

class StepAP214_HArray1OfSecurityClassificationItem(StepAP214_Array1OfSecurityClassificationItem, Standard_Transient): ...

class StepAP214_HArray1OfExternalIdentificationItem(StepAP214_Array1OfExternalIdentificationItem, Standard_Transient): ...

class StepAP214_HArray1OfAutoDesignDatedItem(StepAP214_Array1OfAutoDesignDatedItem, Standard_Transient): ...

class StepAP214_HArray1OfPersonAndOrganizationItem(StepAP214_Array1OfPersonAndOrganizationItem, Standard_Transient): ...

class StepAP214_HArray1OfAutoDesignDateAndPersonItem(StepAP214_Array1OfAutoDesignDateAndPersonItem, Standard_Transient): ...

class StepAP214_HArray1OfAutoDesignGroupedItem(StepAP214_Array1OfAutoDesignGroupedItem, Standard_Transient): ...

class StepAP214_HArray1OfPresentedItemSelect(StepAP214_Array1OfPresentedItemSelect, Standard_Transient): ...

class StepAP214_HArray1OfAutoDesignGeneralOrgItem(StepAP214_Array1OfAutoDesignGeneralOrgItem, Standard_Transient): ...

class StepAP214_HArray1OfAutoDesignDateAndTimeItem(StepAP214_Array1OfAutoDesignDateAndTimeItem, Standard_Transient): ...

class StepAP214_HArray1OfAutoDesignPresentedItemSelect(StepAP214_Array1OfAutoDesignPresentedItemSelect, Standard_Transient): ...

class StepAP214_HArray1OfAutoDesignReferencingItem(StepAP214_Array1OfAutoDesignReferencingItem, Standard_Transient): ...

class StepAP214_HArray1OfDocumentReferenceItem(StepAP214_Array1OfDocumentReferenceItem, Standard_Transient): ...

class StepAP214_HArray1OfOrganizationItem(StepAP214_Array1OfOrganizationItem, Standard_Transient): ...

class StepAP214_HArray1OfApprovalItem(StepAP214_Array1OfApprovalItem, Standard_Transient): ...

class StepAP214_HArray1OfGroupItem(StepAP214_Array1OfGroupItem, Standard_Transient): ...

class StepAP214_HArray1OfDateAndTimeItem(StepAP214_Array1OfDateAndTimeItem, Standard_Transient): ...

# harray2 classes
# harray2 classes

stepap214_Protocol = stepap214.Protocol
