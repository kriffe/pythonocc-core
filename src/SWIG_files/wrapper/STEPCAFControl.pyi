from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepShape import *
from OCC.Core.StepBasic import *
from OCC.Core.STEPControl import *
from OCC.Core.TopoDS import *
from OCC.Core.TDF import *
from OCC.Core.IFSelect import *
from OCC.Core.TCollection import *
from OCC.Core.XSControl import *
from OCC.Core.XCAFDimTolObjects import *
from OCC.Core.StepDimTol import *
from OCC.Core.StepRepr import *
from OCC.Core.StepVisual import *
from OCC.Core.XCAFDoc import *
from OCC.Core.STEPConstruct import *
from OCC.Core.TDocStd import *
from OCC.Core.Resource import *

#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapIteratorOfDataMapOfLabelExternFile = NewType('STEPCAFControl_DataMapIteratorOfDataMapOfLabelExternFile', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapIteratorOfDataMapOfLabelShape = NewType('STEPCAFControl_DataMapIteratorOfDataMapOfLabelShape', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapIteratorOfDataMapOfPDExternFile = NewType('STEPCAFControl_DataMapIteratorOfDataMapOfPDExternFile', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapIteratorOfDataMapOfSDRExternFile = NewType('STEPCAFControl_DataMapIteratorOfDataMapOfSDRExternFile', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapIteratorOfDataMapOfShapePD = NewType('STEPCAFControl_DataMapIteratorOfDataMapOfShapePD', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapIteratorOfDataMapOfShapeSDR = NewType('STEPCAFControl_DataMapIteratorOfDataMapOfShapeSDR', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapOfLabelExternFile = NewType('STEPCAFControl_DataMapOfLabelExternFile', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapOfLabelShape = NewType('STEPCAFControl_DataMapOfLabelShape', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapOfPDExternFile = NewType('STEPCAFControl_DataMapOfPDExternFile', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapOfSDRExternFile = NewType('STEPCAFControl_DataMapOfSDRExternFile', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapOfShapePD = NewType('STEPCAFControl_DataMapOfShapePD', Any)
#the following typedef cannot be wrapped as is
STEPCAFControl_DataMapOfShapeSDR = NewType('STEPCAFControl_DataMapOfShapeSDR', Any)

class STEPCAFControl_ActorWrite(STEPControl_ActorWrite):
	def __init__(self) -> None: ...
	def ClearMap(self) -> None: ...
	def IsAssembly(self, S: TopoDS_Shape) -> bool: ...
	def RegisterAssembly(self, S: TopoDS_Shape) -> None: ...
	def SetStdMode(self, stdmode: Optional[bool]) -> None: ...

class STEPCAFControl_Controller(STEPControl_Controller):
	def __init__(self) -> None: ...
	@staticmethod
	def Init() -> bool: ...

class STEPCAFControl_ExternFile(Standard_Transient):
	def __init__(self) -> None: ...
	def GetLabel(self) -> TDF_Label: ...
	def GetLoadStatus(self) -> IFSelect_ReturnStatus: ...
	def GetName(self) -> TCollection_HAsciiString: ...
	def GetTransferStatus(self) -> bool: ...
	def GetWS(self) -> XSControl_WorkSession: ...
	def GetWriteStatus(self) -> IFSelect_ReturnStatus: ...
	def SetLabel(self, L: TDF_Label) -> None: ...
	def SetLoadStatus(self, stat: IFSelect_ReturnStatus) -> None: ...
	def SetName(self, name: TCollection_HAsciiString) -> None: ...
	def SetTransferStatus(self, isok: bool) -> None: ...
	def SetWS(self, WS: XSControl_WorkSession) -> None: ...
	def SetWriteStatus(self, stat: IFSelect_ReturnStatus) -> None: ...

class STEPCAFControl_GDTProperty:
	def __init__(self) -> None: ...
	@staticmethod
	def GetDatumRefModifiers(theModifiers: XCAFDimTolObjects_DatumModifiersSequence, theModifWithVal: XCAFDimTolObjects_DatumModifWithValue, theValue: float, theUnit: StepBasic_Unit) -> StepDimTol_HArray1OfDatumReferenceModifier: ...
	@staticmethod
	def GetDatumTargetName(theDatumType: XCAFDimTolObjects_DatumTargetType) -> TCollection_HAsciiString: ...
	@staticmethod
	def GetDatumTargetType(theDescription: TCollection_HAsciiString, theType: XCAFDimTolObjects_DatumTargetType) -> bool: ...
	@staticmethod
	def GetDimClassOfTolerance(theLAF: StepShape_LimitsAndFits, theFV: XCAFDimTolObjects_DimensionFormVariance, theG: XCAFDimTolObjects_DimensionGrade) -> bool: ...
	@staticmethod
	def GetDimModifierName(theModifier: XCAFDimTolObjects_DimensionModif) -> TCollection_HAsciiString: ...
	@staticmethod
	def GetDimModifiers(theCRI: StepRepr_CompoundRepresentationItem, theModifiers: XCAFDimTolObjects_DimensionModifiersSequence) -> None: ...
	@staticmethod
	def GetDimQualifierName(theQualifier: XCAFDimTolObjects_DimensionQualifier) -> TCollection_HAsciiString: ...
	@staticmethod
	def GetDimQualifierType(theDescription: TCollection_HAsciiString, theType: XCAFDimTolObjects_DimensionQualifier) -> bool: ...
	@staticmethod
	def GetDimType(theName: TCollection_HAsciiString, theType: XCAFDimTolObjects_DimensionType) -> bool: ...
	@staticmethod
	def GetDimTypeName(theType: XCAFDimTolObjects_DimensionType) -> TCollection_HAsciiString: ...
	@staticmethod
	def GetGeomTolerance(theType: XCAFDimTolObjects_GeomToleranceType) -> StepDimTol_GeometricTolerance: ...
	@staticmethod
	def GetGeomToleranceModifier(theModifier: XCAFDimTolObjects_GeomToleranceModif) -> StepDimTol_GeometricToleranceModifier: ...
	@overload
	@staticmethod
	def GetGeomToleranceType(theType: XCAFDimTolObjects_GeomToleranceType) -> StepDimTol_GeometricToleranceType: ...
	@overload
	@staticmethod
	def GetGeomToleranceType(theType: StepDimTol_GeometricToleranceType) -> XCAFDimTolObjects_GeomToleranceType: ...
	@staticmethod
	def GetLimitsAndFits(theHole: bool, theFormVariance: XCAFDimTolObjects_DimensionFormVariance, theGrade: XCAFDimTolObjects_DimensionGrade) -> StepShape_LimitsAndFits: ...
	@staticmethod
	def GetTessellation(theShape: TopoDS_Shape) -> StepVisual_TessellatedGeometricSet: ...
	@overload
	@staticmethod
	def GetTolValueType(theDescription: TCollection_HAsciiString, theType: XCAFDimTolObjects_GeomToleranceTypeValue) -> bool: ...
	@overload
	@staticmethod
	def GetTolValueType(theType: XCAFDimTolObjects_GeomToleranceTypeValue) -> TCollection_HAsciiString: ...
	@staticmethod
	def IsDimensionalLocation(theType: XCAFDimTolObjects_DimensionType) -> bool: ...
	@staticmethod
	def IsDimensionalSize(theType: XCAFDimTolObjects_DimensionType) -> bool: ...

class STEPCAFControl_Reader:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, WS: XSControl_WorkSession, scratch: Optional[bool]) -> None: ...
	def ChangeReader(self) -> STEPControl_Reader: ...
	def ExternFile(self, name: str, ef: STEPCAFControl_ExternFile) -> bool: ...
	def ExternFiles(self) -> False: ...
	@staticmethod
	def FindInstance(NAUO: StepRepr_NextAssemblyUsageOccurrence, STool: XCAFDoc_ShapeTool, Tool: STEPConstruct_Tool, ShapeLabelMap: XCAFDoc_DataMapOfShapeLabel) -> TDF_Label: ...
	def GetColorMode(self) -> bool: ...
	def GetGDTMode(self) -> bool: ...
	def GetLayerMode(self) -> bool: ...
	def GetMatMode(self) -> bool: ...
	def GetNameMode(self) -> bool: ...
	def GetPropsMode(self) -> bool: ...
	def GetSHUOMode(self) -> bool: ...
	def GetViewMode(self) -> bool: ...
	def Init(self, WS: XSControl_WorkSession, scratch: Optional[bool]) -> None: ...
	def NbRootsForTransfer(self) -> int: ...
	@overload
	def Perform(self, filename: TCollection_AsciiString, doc: TDocStd_Document) -> bool: ...
	@overload
	def Perform(self, filename: str, doc: TDocStd_Document) -> bool: ...
	def ReadFile(self, filename: str) -> IFSelect_ReturnStatus: ...
	def Reader(self) -> STEPControl_Reader: ...
	def SetColorMode(self, colormode: bool) -> None: ...
	def SetGDTMode(self, gdtmode: bool) -> None: ...
	def SetLayerMode(self, layermode: bool) -> None: ...
	def SetMatMode(self, matmode: bool) -> None: ...
	def SetNameMode(self, namemode: bool) -> None: ...
	def SetPropsMode(self, propsmode: bool) -> None: ...
	def SetSHUOMode(self, shuomode: bool) -> None: ...
	def SetSourceCodePage(self, theCode: Resource_FormatType) -> None: ...
	def SetViewMode(self, viewmode: bool) -> None: ...
	def SourceCodePage(self) -> Resource_FormatType: ...
	def Transfer(self, doc: TDocStd_Document) -> bool: ...
	def TransferOneRoot(self, num: int, doc: TDocStd_Document) -> bool: ...

class STEPCAFControl_Writer:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, WS: XSControl_WorkSession, scratch: Optional[bool]) -> None: ...
	def ChangeWriter(self) -> STEPControl_Writer: ...
	@overload
	def ExternFile(self, L: TDF_Label, ef: STEPCAFControl_ExternFile) -> bool: ...
	@overload
	def ExternFile(self, name: str, ef: STEPCAFControl_ExternFile) -> bool: ...
	def ExternFiles(self) -> False: ...
	def GetColorMode(self) -> bool: ...
	def GetDimTolMode(self) -> bool: ...
	def GetLayerMode(self) -> bool: ...
	def GetMaterialMode(self) -> bool: ...
	def GetNameMode(self) -> bool: ...
	def GetPropsMode(self) -> bool: ...
	def GetSHUOMode(self) -> bool: ...
	def Init(self, WS: XSControl_WorkSession, scratch: Optional[bool]) -> None: ...
	@overload
	def Perform(self, doc: TDocStd_Document, filename: TCollection_AsciiString) -> bool: ...
	@overload
	def Perform(self, doc: TDocStd_Document, filename: str) -> bool: ...
	def SetColorMode(self, colormode: bool) -> None: ...
	def SetDimTolMode(self, dimtolmode: bool) -> None: ...
	def SetLayerMode(self, layermode: bool) -> None: ...
	def SetMaterialMode(self, matmode: bool) -> None: ...
	def SetNameMode(self, namemode: bool) -> None: ...
	def SetPropsMode(self, propsmode: bool) -> None: ...
	def SetSHUOMode(self, shuomode: bool) -> None: ...
	@overload
	def Transfer(self, doc: TDocStd_Document, mode: Optional[STEPControl_StepModelType], multi: Optional[str]) -> bool: ...
	@overload
	def Transfer(self, L: TDF_Label, mode: Optional[STEPControl_StepModelType], multi: Optional[str]) -> bool: ...
	def Write(self, filename: str) -> IFSelect_ReturnStatus: ...
	def Writer(self) -> STEPControl_Writer: ...

# harray1 classes
# harray2 classes
# hsequence classes

STEPCAFControl_Controller_Init = STEPCAFControl_Controller.Init
STEPCAFControl_GDTProperty_GetDatumRefModifiers = STEPCAFControl_GDTProperty.GetDatumRefModifiers
STEPCAFControl_GDTProperty_GetDatumTargetName = STEPCAFControl_GDTProperty.GetDatumTargetName
STEPCAFControl_GDTProperty_GetDatumTargetType = STEPCAFControl_GDTProperty.GetDatumTargetType
STEPCAFControl_GDTProperty_GetDimClassOfTolerance = STEPCAFControl_GDTProperty.GetDimClassOfTolerance
STEPCAFControl_GDTProperty_GetDimModifierName = STEPCAFControl_GDTProperty.GetDimModifierName
STEPCAFControl_GDTProperty_GetDimModifiers = STEPCAFControl_GDTProperty.GetDimModifiers
STEPCAFControl_GDTProperty_GetDimQualifierName = STEPCAFControl_GDTProperty.GetDimQualifierName
STEPCAFControl_GDTProperty_GetDimQualifierType = STEPCAFControl_GDTProperty.GetDimQualifierType
STEPCAFControl_GDTProperty_GetDimType = STEPCAFControl_GDTProperty.GetDimType
STEPCAFControl_GDTProperty_GetDimTypeName = STEPCAFControl_GDTProperty.GetDimTypeName
STEPCAFControl_GDTProperty_GetGeomTolerance = STEPCAFControl_GDTProperty.GetGeomTolerance
STEPCAFControl_GDTProperty_GetGeomToleranceModifier = STEPCAFControl_GDTProperty.GetGeomToleranceModifier
STEPCAFControl_GDTProperty_GetGeomToleranceType = STEPCAFControl_GDTProperty.GetGeomToleranceType
STEPCAFControl_GDTProperty_GetGeomToleranceType = STEPCAFControl_GDTProperty.GetGeomToleranceType
STEPCAFControl_GDTProperty_GetLimitsAndFits = STEPCAFControl_GDTProperty.GetLimitsAndFits
STEPCAFControl_GDTProperty_GetTessellation = STEPCAFControl_GDTProperty.GetTessellation
STEPCAFControl_GDTProperty_GetTolValueType = STEPCAFControl_GDTProperty.GetTolValueType
STEPCAFControl_GDTProperty_GetTolValueType = STEPCAFControl_GDTProperty.GetTolValueType
STEPCAFControl_GDTProperty_IsDimensionalLocation = STEPCAFControl_GDTProperty.IsDimensionalLocation
STEPCAFControl_GDTProperty_IsDimensionalSize = STEPCAFControl_GDTProperty.IsDimensionalSize
STEPCAFControl_Reader_FindInstance = STEPCAFControl_Reader.FindInstance
