from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Transfer import *
from OCC.Core.StepShape import *
from OCC.Core.TopoDS import *
from OCC.Core.StepRepr import *
from OCC.Core.TopLoc import *
from OCC.Core.StepBasic import *
from OCC.Core.StepAP203 import *
from OCC.Core.Interface import *
from OCC.Core.StepGeom import *
from OCC.Core.StepData import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *
from OCC.Core.gp import *
from OCC.Core.XSControl import *
from OCC.Core.StepVisual import *
from OCC.Core.Quantity import *

#the following typedef cannot be wrapped as is
STEPConstruct_DataMapIteratorOfDataMapOfAsciiStringTransient = NewType('STEPConstruct_DataMapIteratorOfDataMapOfAsciiStringTransient', Any)
#the following typedef cannot be wrapped as is
STEPConstruct_DataMapIteratorOfDataMapOfPointTransient = NewType('STEPConstruct_DataMapIteratorOfDataMapOfPointTransient', Any)
#the following typedef cannot be wrapped as is
STEPConstruct_DataMapOfAsciiStringTransient = NewType('STEPConstruct_DataMapOfAsciiStringTransient', Any)
#the following typedef cannot be wrapped as is
STEPConstruct_DataMapOfPointTransient = NewType('STEPConstruct_DataMapOfPointTransient', Any)

class stepconstruct:
	@staticmethod
	def FindCDSR(ComponentBinder: Transfer_Binder, AssemblySDR: StepShape_ShapeDefinitionRepresentation, ComponentCDSR: StepShape_ContextDependentShapeRepresentation) -> bool: ...
	@overload
	@staticmethod
	def FindEntity(FinderProcess: Transfer_FinderProcess, Shape: TopoDS_Shape) -> StepRepr_RepresentationItem: ...
	@overload
	@staticmethod
	def FindEntity(FinderProcess: Transfer_FinderProcess, Shape: TopoDS_Shape, Loc: TopLoc_Location) -> StepRepr_RepresentationItem: ...
	@staticmethod
	def FindShape(TransientProcess: Transfer_TransientProcess, item: StepRepr_RepresentationItem) -> TopoDS_Shape: ...

class STEPConstruct_AP203Context:
	def __init__(self) -> None: ...
	def Clear(self) -> None: ...
	def DefaultApproval(self) -> StepBasic_Approval: ...
	def DefaultDateAndTime(self) -> StepBasic_DateAndTime: ...
	def DefaultPersonAndOrganization(self) -> StepBasic_PersonAndOrganization: ...
	def DefaultSecurityClassificationLevel(self) -> StepBasic_SecurityClassificationLevel: ...
	def GetApproval(self) -> StepAP203_CcDesignApproval: ...
	def GetApprovalDateTime(self) -> StepBasic_ApprovalDateTime: ...
	def GetApprover(self) -> StepBasic_ApprovalPersonOrganization: ...
	def GetClassificationDate(self) -> StepAP203_CcDesignDateAndTimeAssignment: ...
	def GetClassificationOfficer(self) -> StepAP203_CcDesignPersonAndOrganizationAssignment: ...
	def GetCreationDate(self) -> StepAP203_CcDesignDateAndTimeAssignment: ...
	def GetCreator(self) -> StepAP203_CcDesignPersonAndOrganizationAssignment: ...
	def GetDesignOwner(self) -> StepAP203_CcDesignPersonAndOrganizationAssignment: ...
	def GetDesignSupplier(self) -> StepAP203_CcDesignPersonAndOrganizationAssignment: ...
	def GetProductCategoryRelationship(self) -> StepBasic_ProductCategoryRelationship: ...
	def GetSecurity(self) -> StepAP203_CcDesignSecurityClassification: ...
	@overload
	def Init(self, sdr: StepShape_ShapeDefinitionRepresentation) -> None: ...
	@overload
	def Init(self, SDRTool: STEPConstruct_Part) -> None: ...
	@overload
	def Init(self, nauo: StepRepr_NextAssemblyUsageOccurrence) -> None: ...
	def InitApprovalRequisites(self) -> None: ...
	def InitAssembly(self, nauo: StepRepr_NextAssemblyUsageOccurrence) -> None: ...
	def InitRoles(self) -> None: ...
	def InitSecurityRequisites(self) -> None: ...
	def RoleApprover(self) -> StepBasic_ApprovalRole: ...
	def RoleClassificationDate(self) -> StepBasic_DateTimeRole: ...
	def RoleClassificationOfficer(self) -> StepBasic_PersonAndOrganizationRole: ...
	def RoleCreationDate(self) -> StepBasic_DateTimeRole: ...
	def RoleCreator(self) -> StepBasic_PersonAndOrganizationRole: ...
	def RoleDesignOwner(self) -> StepBasic_PersonAndOrganizationRole: ...
	def RoleDesignSupplier(self) -> StepBasic_PersonAndOrganizationRole: ...
	def SetDefaultApproval(self, app: StepBasic_Approval) -> None: ...
	def SetDefaultDateAndTime(self, dt: StepBasic_DateAndTime) -> None: ...
	def SetDefaultPersonAndOrganization(self, po: StepBasic_PersonAndOrganization) -> None: ...
	def SetDefaultSecurityClassificationLevel(self, sc: StepBasic_SecurityClassificationLevel) -> None: ...

class STEPConstruct_Assembly:
	def __init__(self) -> None: ...
	@staticmethod
	def CheckSRRReversesNAUO(theGraph: Interface_Graph, CDSR: StepShape_ContextDependentShapeRepresentation) -> bool: ...
	def GetNAUO(self) -> StepRepr_NextAssemblyUsageOccurrence: ...
	def Init(self, aSR: StepShape_ShapeDefinitionRepresentation, SDR0: StepShape_ShapeDefinitionRepresentation, Ax0: StepGeom_Axis2Placement3d, Loc: StepGeom_Axis2Placement3d) -> None: ...
	def ItemLocation(self) -> StepGeom_Axis2Placement3d: ...
	def ItemValue(self) -> Standard_Transient: ...
	def MakeRelationship(self) -> None: ...

class STEPConstruct_ContextTool:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aStepModel: StepData_StepModel) -> None: ...
	def AP203Context(self) -> STEPConstruct_AP203Context: ...
	def AddAPD(self, enforce: Optional[bool]) -> None: ...
	def GetACname(self) -> TCollection_HAsciiString: ...
	def GetACschemaName(self) -> TCollection_HAsciiString: ...
	def GetACstatus(self) -> TCollection_HAsciiString: ...
	def GetACyear(self) -> int: ...
	def GetAPD(self) -> StepBasic_ApplicationProtocolDefinition: ...
	def GetDefaultAxis(self) -> StepGeom_Axis2Placement3d: ...
	def GetProductName(self) -> TCollection_HAsciiString: ...
	def GetRootsForAssemblyLink(self, assembly: STEPConstruct_Assembly) -> TColStd_HSequenceOfTransient: ...
	def GetRootsForPart(self, SDRTool: STEPConstruct_Part) -> TColStd_HSequenceOfTransient: ...
	def Index(self) -> int: ...
	def IsAP203(self) -> bool: ...
	def IsAP214(self) -> bool: ...
	def IsAP242(self) -> bool: ...
	def Level(self) -> int: ...
	def NextIndex(self) -> None: ...
	def NextLevel(self) -> None: ...
	def PrevIndex(self) -> None: ...
	def PrevLevel(self) -> None: ...
	def SetACname(self, name: TCollection_HAsciiString) -> None: ...
	def SetACschemaName(self, schemaName: TCollection_HAsciiString) -> None: ...
	def SetACstatus(self, status: TCollection_HAsciiString) -> None: ...
	def SetACyear(self, year: int) -> None: ...
	def SetIndex(self, ind: int) -> None: ...
	def SetLevel(self, lev: int) -> None: ...
	def SetModel(self, aStepModel: StepData_StepModel) -> None: ...

class STEPConstruct_Part:
	def __init__(self) -> None: ...
	def AC(self) -> StepBasic_ApplicationContext: ...
	def ACapplication(self) -> TCollection_HAsciiString: ...
	def IsDone(self) -> bool: ...
	def MakeSDR(self, aShape: StepShape_ShapeRepresentation, aName: TCollection_HAsciiString, AC: StepBasic_ApplicationContext) -> None: ...
	def PC(self) -> StepBasic_ProductContext: ...
	def PCdisciplineType(self) -> TCollection_HAsciiString: ...
	def PCname(self) -> TCollection_HAsciiString: ...
	def PD(self) -> StepBasic_ProductDefinition: ...
	def PDC(self) -> StepBasic_ProductDefinitionContext: ...
	def PDCname(self) -> TCollection_HAsciiString: ...
	def PDCstage(self) -> TCollection_HAsciiString: ...
	def PDF(self) -> StepBasic_ProductDefinitionFormation: ...
	def PDFdescription(self) -> TCollection_HAsciiString: ...
	def PDFid(self) -> TCollection_HAsciiString: ...
	def PDS(self) -> StepRepr_ProductDefinitionShape: ...
	def PDSdescription(self) -> TCollection_HAsciiString: ...
	def PDSname(self) -> TCollection_HAsciiString: ...
	def PDdescription(self) -> TCollection_HAsciiString: ...
	def PRPC(self) -> StepBasic_ProductRelatedProductCategory: ...
	def PRPCdescription(self) -> TCollection_HAsciiString: ...
	def PRPCname(self) -> TCollection_HAsciiString: ...
	def Pdescription(self) -> TCollection_HAsciiString: ...
	def Pid(self) -> TCollection_HAsciiString: ...
	def Pname(self) -> TCollection_HAsciiString: ...
	def Product(self) -> StepBasic_Product: ...
	def ReadSDR(self, aShape: StepShape_ShapeDefinitionRepresentation) -> None: ...
	def SDRValue(self) -> StepShape_ShapeDefinitionRepresentation: ...
	def SRValue(self) -> StepShape_ShapeRepresentation: ...
	def SetACapplication(self, text: TCollection_HAsciiString) -> None: ...
	def SetPCdisciplineType(self, label: TCollection_HAsciiString) -> None: ...
	def SetPCname(self, name: TCollection_HAsciiString) -> None: ...
	def SetPDCname(self, label: TCollection_HAsciiString) -> None: ...
	def SetPDCstage(self, label: TCollection_HAsciiString) -> None: ...
	def SetPDFdescription(self, text: TCollection_HAsciiString) -> None: ...
	def SetPDFid(self, id: TCollection_HAsciiString) -> None: ...
	def SetPDSdescription(self, text: TCollection_HAsciiString) -> None: ...
	def SetPDSname(self, label: TCollection_HAsciiString) -> None: ...
	def SetPDdescription(self, text: TCollection_HAsciiString) -> None: ...
	def SetPRPCdescription(self, text: TCollection_HAsciiString) -> None: ...
	def SetPRPCname(self, label: TCollection_HAsciiString) -> None: ...
	def SetPdescription(self, text: TCollection_HAsciiString) -> None: ...
	def SetPid(self, id: TCollection_HAsciiString) -> None: ...
	def SetPname(self, label: TCollection_HAsciiString) -> None: ...

class STEPConstruct_PointHasher:
	@staticmethod
	def HashCode(thePoint: gp_Pnt, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(Point1: gp_Pnt, Point2: gp_Pnt) -> bool: ...

class STEPConstruct_Tool:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, WS: XSControl_WorkSession) -> None: ...
	def FinderProcess(self) -> Transfer_FinderProcess: ...
	def Graph(self, recompute: Optional[bool]) -> Interface_Graph: ...
	def Model(self) -> Interface_InterfaceModel: ...
	def TransientProcess(self) -> Transfer_TransientProcess: ...
	def WS(self) -> XSControl_WorkSession: ...

class STEPConstruct_UnitContext:
	def __init__(self) -> None: ...
	def AreaDone(self) -> bool: ...
	def AreaFactor(self) -> float: ...
	@overload
	def ComputeFactors(self, aContext: StepRepr_GlobalUnitAssignedContext) -> int: ...
	@overload
	def ComputeFactors(self, aUnit: StepBasic_NamedUnit) -> int: ...
	def ComputeTolerance(self, aContext: StepRepr_GlobalUncertaintyAssignedContext) -> int: ...
	@staticmethod
	def ConvertSiPrefix(aPrefix: StepBasic_SiPrefix) -> float: ...
	def HasUncertainty(self) -> bool: ...
	def Init(self, Tol3d: float) -> None: ...
	def IsDone(self) -> bool: ...
	def LengthDone(self) -> bool: ...
	def LengthFactor(self) -> float: ...
	def PlaneAngleDone(self) -> bool: ...
	def PlaneAngleFactor(self) -> float: ...
	def SolidAngleDone(self) -> bool: ...
	def SolidAngleFactor(self) -> float: ...
	def StatusMessage(self, status: int) -> str: ...
	def Uncertainty(self) -> float: ...
	def Value(self) -> StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx: ...
	def VolumeDone(self) -> bool: ...
	def VolumeFactor(self) -> float: ...

class STEPConstruct_ExternRefs(STEPConstruct_Tool):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, WS: XSControl_WorkSession) -> None: ...
	def AddExternRef(self, filename: str, PD: StepBasic_ProductDefinition, format: str) -> int: ...
	def Clear(self) -> None: ...
	def FileName(self, num: int) -> str: ...
	def Format(self, num: int) -> TCollection_HAsciiString: ...
	def GetAP214APD(self) -> StepBasic_ApplicationProtocolDefinition: ...
	def Init(self, WS: XSControl_WorkSession) -> bool: ...
	def LoadExternRefs(self) -> bool: ...
	def NbExternRefs(self) -> int: ...
	def ProdDef(self, num: int) -> StepBasic_ProductDefinition: ...
	def SetAP214APD(self, APD: StepBasic_ApplicationProtocolDefinition) -> None: ...
	def WriteExternRefs(self, num: int) -> int: ...
	def checkAP214Shared(self) -> None: ...

class STEPConstruct_Styles(STEPConstruct_Tool):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, WS: XSControl_WorkSession) -> None: ...
	@overload
	def AddStyle(self, style: StepVisual_StyledItem) -> None: ...
	@overload
	def AddStyle(self, item: StepRepr_RepresentationItem, PSA: StepVisual_PresentationStyleAssignment, Override: StepVisual_StyledItem) -> StepVisual_StyledItem: ...
	@overload
	def AddStyle(self, Shape: TopoDS_Shape, PSA: StepVisual_PresentationStyleAssignment, Override: StepVisual_StyledItem) -> StepVisual_StyledItem: ...
	def ClearStyles(self) -> None: ...
	def CreateMDGPR(self, Context: StepRepr_RepresentationContext, MDGPR: StepVisual_MechanicalDesignGeometricPresentationRepresentation) -> bool: ...
	def CreateNAUOSRD(self, Context: StepRepr_RepresentationContext, CDSR: StepShape_ContextDependentShapeRepresentation, initPDS: StepRepr_ProductDefinitionShape) -> bool: ...
	@staticmethod
	def DecodeColor(Colour: StepVisual_Colour, Col: Quantity_Color) -> bool: ...
	@overload
	@staticmethod
	def EncodeColor(Col: Quantity_Color) -> StepVisual_Colour: ...
	@overload
	@staticmethod
	def EncodeColor(Col: Quantity_Color, DPDCs: STEPConstruct_DataMapOfAsciiStringTransient, ColRGBs: STEPConstruct_DataMapOfPointTransient) -> StepVisual_Colour: ...
	def FindContext(self, Shape: TopoDS_Shape) -> StepRepr_RepresentationContext: ...
	def GetColorPSA(self, item: StepRepr_RepresentationItem, Col: StepVisual_Colour) -> StepVisual_PresentationStyleAssignment: ...
	def GetColors(self, style: StepVisual_StyledItem, SurfCol: StepVisual_Colour, BoundCol: StepVisual_Colour, CurveCol: StepVisual_Colour) -> Tuple[bool, bool]: ...
	def Init(self, WS: XSControl_WorkSession) -> bool: ...
	def LoadInvisStyles(self, InvSyles: TColStd_HSequenceOfTransient) -> bool: ...
	def LoadStyles(self) -> bool: ...
	def MakeColorPSA(self, item: StepRepr_RepresentationItem, SurfCol: StepVisual_Colour, CurveCol: StepVisual_Colour, isForNAUO: Optional[bool]) -> StepVisual_PresentationStyleAssignment: ...
	def NbStyles(self) -> int: ...
	def Style(self, i: int) -> StepVisual_StyledItem: ...

class STEPConstruct_ValidationProps(STEPConstruct_Tool):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, WS: XSControl_WorkSession) -> None: ...
	def AddArea(self, Shape: TopoDS_Shape, Area: float) -> bool: ...
	def AddCentroid(self, Shape: TopoDS_Shape, Pnt: gp_Pnt, instance: Optional[bool]) -> bool: ...
	@overload
	def AddProp(self, Shape: TopoDS_Shape, Prop: StepRepr_RepresentationItem, Descr: str, instance: Optional[bool]) -> bool: ...
	@overload
	def AddProp(self, target: StepRepr_CharacterizedDefinition, Context: StepRepr_RepresentationContext, Prop: StepRepr_RepresentationItem, Descr: str) -> bool: ...
	def AddVolume(self, Shape: TopoDS_Shape, Vol: float) -> bool: ...
	def FindTarget(self, S: TopoDS_Shape, target: StepRepr_CharacterizedDefinition, Context: StepRepr_RepresentationContext, instance: Optional[bool]) -> bool: ...
	def GetPropNAUO(self, PD: StepRepr_PropertyDefinition) -> StepRepr_NextAssemblyUsageOccurrence: ...
	def GetPropPD(self, PD: StepRepr_PropertyDefinition) -> StepBasic_ProductDefinition: ...
	def GetPropPnt(self, item: StepRepr_RepresentationItem, Context: StepRepr_RepresentationContext, Pnt: gp_Pnt) -> bool: ...
	def GetPropReal(self, item: StepRepr_RepresentationItem) -> Tuple[bool, float, bool]: ...
	@overload
	def GetPropShape(self, ProdDef: StepBasic_ProductDefinition) -> TopoDS_Shape: ...
	@overload
	def GetPropShape(self, PD: StepRepr_PropertyDefinition) -> TopoDS_Shape: ...
	def Init(self, WS: XSControl_WorkSession) -> bool: ...
	def LoadProps(self, seq: TColStd_SequenceOfTransient) -> bool: ...
	def SetAssemblyShape(self, shape: TopoDS_Shape) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

stepconstruct_FindCDSR = stepconstruct.FindCDSR
stepconstruct_FindEntity = stepconstruct.FindEntity
stepconstruct_FindEntity = stepconstruct.FindEntity
stepconstruct_FindShape = stepconstruct.FindShape
STEPConstruct_Assembly_CheckSRRReversesNAUO = STEPConstruct_Assembly.CheckSRRReversesNAUO
STEPConstruct_PointHasher_HashCode = STEPConstruct_PointHasher.HashCode
STEPConstruct_PointHasher_IsEqual = STEPConstruct_PointHasher.IsEqual
STEPConstruct_UnitContext_ConvertSiPrefix = STEPConstruct_UnitContext.ConvertSiPrefix
STEPConstruct_Styles_DecodeColor = STEPConstruct_Styles.DecodeColor
STEPConstruct_Styles_EncodeColor = STEPConstruct_Styles.EncodeColor
STEPConstruct_Styles_EncodeColor = STEPConstruct_Styles.EncodeColor
