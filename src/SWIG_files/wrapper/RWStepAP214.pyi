from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.TCollection import *
from OCC.Core.StepAP214 import *
from OCC.Core.TColStd import *


class RWStepAP214:
	@staticmethod
	def Init(self) -> None: ...

class RWStepAP214_GeneralModule(StepData_GeneralModule):
	def __init__(self) -> None: ...
	def CategoryNumber(self, CN: int, ent: Standard_Transient, shares: Interface_ShareTool) -> int: ...
	def CheckCase(self, CN: int, ent: Standard_Transient, shares: Interface_ShareTool, ach: Interface_Check) -> None: ...
	def CopyCase(self, CN: int, entfrom: Standard_Transient, entto: Standard_Transient, TC: Interface_CopyTool) -> None: ...
	def FillSharedCase(self, CN: int, ent: Standard_Transient, iter: Interface_EntityIterator) -> None: ...
	def Name(self, CN: int, ent: Standard_Transient, shares: Interface_ShareTool) -> TCollection_HAsciiString: ...
	def NewVoid(self, CN: int, ent: Standard_Transient) -> bool: ...

class RWStepAP214_RWAppliedApprovalAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedApprovalAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedApprovalAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedApprovalAssignment) -> None: ...

class RWStepAP214_RWAppliedDateAndTimeAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedDateAndTimeAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedDateAndTimeAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedDateAndTimeAssignment) -> None: ...

class RWStepAP214_RWAppliedDateAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedDateAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedDateAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedDateAssignment) -> None: ...

class RWStepAP214_RWAppliedDocumentReference:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedDocumentReference) -> None: ...
	def Share(self, ent: StepAP214_AppliedDocumentReference, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedDocumentReference) -> None: ...

class RWStepAP214_RWAppliedExternalIdentificationAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedExternalIdentificationAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedExternalIdentificationAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedExternalIdentificationAssignment) -> None: ...

class RWStepAP214_RWAppliedGroupAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedGroupAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedGroupAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedGroupAssignment) -> None: ...

class RWStepAP214_RWAppliedOrganizationAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedOrganizationAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedOrganizationAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedOrganizationAssignment) -> None: ...

class RWStepAP214_RWAppliedPersonAndOrganizationAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedPersonAndOrganizationAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedPersonAndOrganizationAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedPersonAndOrganizationAssignment) -> None: ...

class RWStepAP214_RWAppliedPresentedItem:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedPresentedItem) -> None: ...
	def Share(self, ent: StepAP214_AppliedPresentedItem, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedPresentedItem) -> None: ...

class RWStepAP214_RWAppliedSecurityClassificationAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AppliedSecurityClassificationAssignment) -> None: ...
	def Share(self, ent: StepAP214_AppliedSecurityClassificationAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AppliedSecurityClassificationAssignment) -> None: ...

class RWStepAP214_RWAutoDesignActualDateAndTimeAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignActualDateAndTimeAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignActualDateAndTimeAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignActualDateAndTimeAssignment) -> None: ...

class RWStepAP214_RWAutoDesignActualDateAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignActualDateAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignActualDateAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignActualDateAssignment) -> None: ...

class RWStepAP214_RWAutoDesignApprovalAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignApprovalAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignApprovalAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignApprovalAssignment) -> None: ...

class RWStepAP214_RWAutoDesignDateAndPersonAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignDateAndPersonAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignDateAndPersonAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignDateAndPersonAssignment) -> None: ...

class RWStepAP214_RWAutoDesignDocumentReference:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignDocumentReference) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignDocumentReference, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignDocumentReference) -> None: ...

class RWStepAP214_RWAutoDesignGroupAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignGroupAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignGroupAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignGroupAssignment) -> None: ...

class RWStepAP214_RWAutoDesignNominalDateAndTimeAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignNominalDateAndTimeAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignNominalDateAndTimeAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignNominalDateAndTimeAssignment) -> None: ...

class RWStepAP214_RWAutoDesignNominalDateAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignNominalDateAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignNominalDateAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignNominalDateAssignment) -> None: ...

class RWStepAP214_RWAutoDesignOrganizationAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignOrganizationAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignOrganizationAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignOrganizationAssignment) -> None: ...

class RWStepAP214_RWAutoDesignPersonAndOrganizationAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignPersonAndOrganizationAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignPersonAndOrganizationAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignPersonAndOrganizationAssignment) -> None: ...

class RWStepAP214_RWAutoDesignPresentedItem:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignPresentedItem) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignPresentedItem, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignPresentedItem) -> None: ...

class RWStepAP214_RWAutoDesignSecurityClassificationAssignment:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_AutoDesignSecurityClassificationAssignment) -> None: ...
	def Share(self, ent: StepAP214_AutoDesignSecurityClassificationAssignment, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_AutoDesignSecurityClassificationAssignment) -> None: ...

class RWStepAP214_RWClass:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_Class) -> None: ...
	def Share(self, ent: StepAP214_Class, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_Class) -> None: ...

class RWStepAP214_RWExternallyDefinedClass:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_ExternallyDefinedClass) -> None: ...
	def Share(self, ent: StepAP214_ExternallyDefinedClass, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_ExternallyDefinedClass) -> None: ...

class RWStepAP214_RWExternallyDefinedGeneralProperty:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_ExternallyDefinedGeneralProperty) -> None: ...
	def Share(self, ent: StepAP214_ExternallyDefinedGeneralProperty, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_ExternallyDefinedGeneralProperty) -> None: ...

class RWStepAP214_RWRepItemGroup:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepAP214_RepItemGroup) -> None: ...
	def Share(self, ent: StepAP214_RepItemGroup, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepAP214_RepItemGroup) -> None: ...

class RWStepAP214_ReadWriteModule(StepData_ReadWriteModule):
	def __init__(self) -> None: ...
	@overload
	def CaseStep(self, atype: TCollection_AsciiString) -> int: ...
	@overload
	def CaseStep(self, types: TColStd_SequenceOfAsciiString) -> int: ...
	def ComplexType(self, CN: int, types: TColStd_SequenceOfAsciiString) -> bool: ...
	def IsComplex(self, CN: int) -> bool: ...
	def ReadStep(self, CN: int, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: Standard_Transient) -> None: ...
	def StepType(self, CN: int) -> TCollection_AsciiString: ...
	def WriteStep(self, CN: int, SW: StepData_StepWriter, ent: Standard_Transient) -> None: ...
