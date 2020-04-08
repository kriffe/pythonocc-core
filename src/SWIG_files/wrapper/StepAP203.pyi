from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.StepBasic import *
from OCC.Core.StepRepr import *
from OCC.Core.TCollection import *

#the following typedef cannot be wrapped as is
StepAP203_Array1OfApprovedItem = NewType('StepAP203_Array1OfApprovedItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfCertifiedItem = NewType('StepAP203_Array1OfCertifiedItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfChangeRequestItem = NewType('StepAP203_Array1OfChangeRequestItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfClassifiedItem = NewType('StepAP203_Array1OfClassifiedItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfContractedItem = NewType('StepAP203_Array1OfContractedItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfDateTimeItem = NewType('StepAP203_Array1OfDateTimeItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfPersonOrganizationItem = NewType('StepAP203_Array1OfPersonOrganizationItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfSpecifiedItem = NewType('StepAP203_Array1OfSpecifiedItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfStartRequestItem = NewType('StepAP203_Array1OfStartRequestItem', Any)
#the following typedef cannot be wrapped as is
StepAP203_Array1OfWorkItem = NewType('StepAP203_Array1OfWorkItem', Any)

class StepAP203_ApprovedItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def Certification(self) -> StepBasic_Certification: ...
	def Change(self) -> StepAP203_Change: ...
	def ChangeRequest(self) -> StepAP203_ChangeRequest: ...
	def ConfigurationEffectivity(self) -> StepRepr_ConfigurationEffectivity: ...
	def ConfigurationItem(self) -> StepRepr_ConfigurationItem: ...
	def Contract(self) -> StepBasic_Contract: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
	def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
	def StartRequest(self) -> StepAP203_StartRequest: ...
	def StartWork(self) -> StepAP203_StartWork: ...

class StepAP203_CcDesignApproval(StepBasic_ApprovalAssignment):
	def __init__(self) -> None: ...
	def Init(self, aApprovalAssignment_AssignedApproval: StepBasic_Approval, aItems: StepAP203_HArray1OfApprovedItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfApprovedItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfApprovedItem) -> None: ...

class StepAP203_CcDesignCertification(StepBasic_CertificationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aCertificationAssignment_AssignedCertification: StepBasic_Certification, aItems: StepAP203_HArray1OfCertifiedItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfCertifiedItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfCertifiedItem) -> None: ...

class StepAP203_CcDesignContract(StepBasic_ContractAssignment):
	def __init__(self) -> None: ...
	def Init(self, aContractAssignment_AssignedContract: StepBasic_Contract, aItems: StepAP203_HArray1OfContractedItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfContractedItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfContractedItem) -> None: ...

class StepAP203_CcDesignDateAndTimeAssignment(StepBasic_DateAndTimeAssignment):
	def __init__(self) -> None: ...
	def Init(self, aDateAndTimeAssignment_AssignedDateAndTime: StepBasic_DateAndTime, aDateAndTimeAssignment_Role: StepBasic_DateTimeRole, aItems: StepAP203_HArray1OfDateTimeItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfDateTimeItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfDateTimeItem) -> None: ...

class StepAP203_CcDesignPersonAndOrganizationAssignment(StepBasic_PersonAndOrganizationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aPersonAndOrganizationAssignment_AssignedPersonAndOrganization: StepBasic_PersonAndOrganization, aPersonAndOrganizationAssignment_Role: StepBasic_PersonAndOrganizationRole, aItems: StepAP203_HArray1OfPersonOrganizationItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfPersonOrganizationItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfPersonOrganizationItem) -> None: ...

class StepAP203_CcDesignSecurityClassification(StepBasic_SecurityClassificationAssignment):
	def __init__(self) -> None: ...
	def Init(self, aSecurityClassificationAssignment_AssignedSecurityClassification: StepBasic_SecurityClassification, aItems: StepAP203_HArray1OfClassifiedItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfClassifiedItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfClassifiedItem) -> None: ...

class StepAP203_CcDesignSpecificationReference(StepBasic_DocumentReference):
	def __init__(self) -> None: ...
	def Init(self, aDocumentReference_AssignedDocument: StepBasic_Document, aDocumentReference_Source: TCollection_HAsciiString, aItems: StepAP203_HArray1OfSpecifiedItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfSpecifiedItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfSpecifiedItem) -> None: ...

class StepAP203_CertifiedItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def SuppliedPartRelationship(self) -> StepRepr_SuppliedPartRelationship: ...

class StepAP203_Change(StepBasic_ActionAssignment):
	def __init__(self) -> None: ...
	def Init(self, aActionAssignment_AssignedAction: StepBasic_Action, aItems: StepAP203_HArray1OfWorkItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfWorkItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfWorkItem) -> None: ...

class StepAP203_ChangeRequest(StepBasic_ActionRequestAssignment):
	def __init__(self) -> None: ...
	def Init(self, aActionRequestAssignment_AssignedActionRequest: StepBasic_VersionedActionRequest, aItems: StepAP203_HArray1OfChangeRequestItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfChangeRequestItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfChangeRequestItem) -> None: ...

class StepAP203_ChangeRequestItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_ClassifiedItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AssemblyComponentUsage(self) -> StepRepr_AssemblyComponentUsage: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_ContractedItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_DateTimeItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApprovalPersonOrganization(self) -> StepBasic_ApprovalPersonOrganization: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def Certification(self) -> StepBasic_Certification: ...
	def Change(self) -> StepAP203_Change: ...
	def ChangeRequest(self) -> StepAP203_ChangeRequest: ...
	def Contract(self) -> StepBasic_Contract: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
	def StartRequest(self) -> StepAP203_StartRequest: ...
	def StartWork(self) -> StepAP203_StartWork: ...

class StepAP203_PersonOrganizationItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def Change(self) -> StepAP203_Change: ...
	def ChangeRequest(self) -> StepAP203_ChangeRequest: ...
	def ConfigurationItem(self) -> StepRepr_ConfigurationItem: ...
	def Contract(self) -> StepBasic_Contract: ...
	def Product(self) -> StepBasic_Product: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
	def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
	def StartRequest(self) -> StepAP203_StartRequest: ...
	def StartWork(self) -> StepAP203_StartWork: ...

class StepAP203_SpecifiedItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...

class StepAP203_StartRequest(StepBasic_ActionRequestAssignment):
	def __init__(self) -> None: ...
	def Init(self, aActionRequestAssignment_AssignedActionRequest: StepBasic_VersionedActionRequest, aItems: StepAP203_HArray1OfStartRequestItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfStartRequestItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfStartRequestItem) -> None: ...

class StepAP203_StartRequestItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_StartWork(StepBasic_ActionAssignment):
	def __init__(self) -> None: ...
	def Init(self, aActionAssignment_AssignedAction: StepBasic_Action, aItems: StepAP203_HArray1OfWorkItem) -> None: ...
	def Items(self) -> StepAP203_HArray1OfWorkItem: ...
	def SetItems(self, Items: StepAP203_HArray1OfWorkItem) -> None: ...

class StepAP203_WorkItem(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
