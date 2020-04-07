from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.StepData import *
from OCC.Core.StepBasic import *
from OCC.Core.StepShape import *
from OCC.Core.StepDimTol import *
from OCC.Core.StepRepr import *
from OCC.Core.StepAP214 import *


class StepAP242_IdAttribute(Standard_Transient):
	def __init__(self) -> None: ...
	def AttributeValue(self) -> TCollection_HAsciiString: ...
	def IdentifiedItem(self) -> StepAP242_IdAttributeSelect: ...
	def Init(self, theAttributeValue: TCollection_HAsciiString, theIdentifiedItem: StepAP242_IdAttributeSelect) -> None: ...
	def SetAttributeValue(self, theAttributeValue: TCollection_HAsciiString) -> None: ...
	def SetIdentifiedItem(self, theIdentifiedItem: StepAP242_IdAttributeSelect) -> None: ...

class StepAP242_IdAttributeSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def Action(self) -> StepBasic_Action: ...
	def Address(self) -> StepBasic_Address: ...
	def ApplicationContext(self) -> StepBasic_ApplicationContext: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DimensionalSize(self) -> StepShape_DimensionalSize: ...
	def GeometricTolerance(self) -> StepDimTol_GeometricTolerance: ...
	def Group(self) -> StepBasic_Group: ...
	def ProductCategory(self) -> StepBasic_ProductCategory: ...
	def PropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def Representation(self) -> StepRepr_Representation: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...

class StepAP242_ItemIdentifiedRepresentationUsage(Standard_Transient):
	def __init__(self) -> None: ...
	def Definition(self) -> StepAP242_ItemIdentifiedRepresentationUsageDefinition: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def IdentifiedItem(self) -> StepRepr_HArray1OfRepresentationItem: ...
	def IdentifiedItemValue(self, num: int) -> StepRepr_RepresentationItem: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theDefinition: StepAP242_ItemIdentifiedRepresentationUsageDefinition, theUsedRepresentation: StepRepr_Representation, theIdentifiedItem: StepRepr_HArray1OfRepresentationItem) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def NbIdentifiedItem(self) -> int: ...
	def SetDefinition(self, theDefinition: StepAP242_ItemIdentifiedRepresentationUsageDefinition) -> None: ...
	def SetDescription(self, theDescription: TCollection_HAsciiString) -> None: ...
	def SetIdentifiedItem(self, theIdentifiedItem: StepRepr_HArray1OfRepresentationItem) -> None: ...
	def SetIdentifiedItemValue(self, num: int, theItem: StepRepr_RepresentationItem) -> None: ...
	def SetName(self, theName: TCollection_HAsciiString) -> None: ...
	def SetUsedRepresentation(self, theUsedRepresentation: StepRepr_Representation) -> None: ...
	def UsedRepresentation(self) -> StepRepr_Representation: ...

class StepAP242_ItemIdentifiedRepresentationUsageDefinition(StepData_SelectType):
	def __init__(self) -> None: ...
	def AppliedApprovalAssignment(self) -> StepAP214_AppliedApprovalAssignment: ...
	def AppliedDateAndTimeAssignment(self) -> StepAP214_AppliedDateAndTimeAssignment: ...
	def AppliedDateAssignment(self) -> StepAP214_AppliedDateAssignment: ...
	def AppliedDocumentReference(self) -> StepAP214_AppliedDocumentReference: ...
	def AppliedExternalIdentificationAssignment(self) -> StepAP214_AppliedExternalIdentificationAssignment: ...
	def AppliedGroupAssignment(self) -> StepAP214_AppliedGroupAssignment: ...
	def AppliedOrganizationAssignment(self) -> StepAP214_AppliedOrganizationAssignment: ...
	def AppliedPersonAndOrganizationAssignment(self) -> StepAP214_AppliedPersonAndOrganizationAssignment: ...
	def AppliedSecurityClassificationAssignment(self) -> StepAP214_AppliedSecurityClassificationAssignment: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DimensionalSize(self) -> StepShape_DimensionalSize: ...
	def GeneralProperty(self) -> StepBasic_GeneralProperty: ...
	def GeometricTolerance(self) -> StepDimTol_GeometricTolerance: ...
	def ProductDefinitionRelationship(self) -> StepBasic_ProductDefinitionRelationship: ...
	def PropertyDefinition(self) -> StepRepr_PropertyDefinition: ...
	def PropertyDefinitionRelationship(self) -> StepRepr_PropertyDefinitionRelationship: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...
	def ShapeAspectRelationship(self) -> StepRepr_ShapeAspectRelationship: ...

class StepAP242_DraughtingModelItemAssociation(StepAP242_ItemIdentifiedRepresentationUsage):
	def __init__(self) -> None: ...

class StepAP242_GeometricItemSpecificUsage(StepAP242_ItemIdentifiedRepresentationUsage):
	def __init__(self) -> None: ...
