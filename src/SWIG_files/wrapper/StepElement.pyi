from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.StepRepr import *
from OCC.Core.StepData import *
from OCC.Core.TColStd import *

#the following typedef cannot be wrapped as is
StepElement_Array1OfCurveElementEndReleasePacket = NewType('StepElement_Array1OfCurveElementEndReleasePacket', Any)
#the following typedef cannot be wrapped as is
StepElement_Array1OfCurveElementSectionDefinition = NewType('StepElement_Array1OfCurveElementSectionDefinition', Any)
#the following typedef cannot be wrapped as is
StepElement_Array1OfHSequenceOfCurveElementPurposeMember = NewType('StepElement_Array1OfHSequenceOfCurveElementPurposeMember', Any)
#the following typedef cannot be wrapped as is
StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember = NewType('StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember', Any)
#the following typedef cannot be wrapped as is
StepElement_Array1OfMeasureOrUnspecifiedValue = NewType('StepElement_Array1OfMeasureOrUnspecifiedValue', Any)
#the following typedef cannot be wrapped as is
StepElement_Array1OfSurfaceSection = NewType('StepElement_Array1OfSurfaceSection', Any)
#the following typedef cannot be wrapped as is
StepElement_Array1OfVolumeElementPurpose = NewType('StepElement_Array1OfVolumeElementPurpose', Any)
#the following typedef cannot be wrapped as is
StepElement_Array1OfVolumeElementPurposeMember = NewType('StepElement_Array1OfVolumeElementPurposeMember', Any)
#the following typedef cannot be wrapped as is
StepElement_Array2OfCurveElementPurposeMember = NewType('StepElement_Array2OfCurveElementPurposeMember', Any)
#the following typedef cannot be wrapped as is
StepElement_Array2OfSurfaceElementPurpose = NewType('StepElement_Array2OfSurfaceElementPurpose', Any)
#the following typedef cannot be wrapped as is
StepElement_Array2OfSurfaceElementPurposeMember = NewType('StepElement_Array2OfSurfaceElementPurposeMember', Any)
#the following typedef cannot be wrapped as is
StepElement_SequenceOfCurveElementPurposeMember = NewType('StepElement_SequenceOfCurveElementPurposeMember', Any)
#the following typedef cannot be wrapped as is
StepElement_SequenceOfCurveElementSectionDefinition = NewType('StepElement_SequenceOfCurveElementSectionDefinition', Any)
#the following typedef cannot be wrapped as is
StepElement_SequenceOfElementMaterial = NewType('StepElement_SequenceOfElementMaterial', Any)
#the following typedef cannot be wrapped as is
StepElement_SequenceOfSurfaceElementPurposeMember = NewType('StepElement_SequenceOfSurfaceElementPurposeMember', Any)

class StepElement_ElementVolume(IntEnum):
	StepElement_Volume: int = ...
StepElement_Volume = StepElement_ElementVolume.StepElement_Volume

class StepElement_CurveEdge(IntEnum):
	StepElement_ElementEdge: int = ...
StepElement_ElementEdge = StepElement_CurveEdge.StepElement_ElementEdge

class StepElement_Volume3dElementShape(IntEnum):
	StepElement_Hexahedron: int = ...
	StepElement_Wedge: int = ...
	StepElement_Tetrahedron: int = ...
	StepElement_Pyramid: int = ...
StepElement_Hexahedron = StepElement_Volume3dElementShape.StepElement_Hexahedron
StepElement_Wedge = StepElement_Volume3dElementShape.StepElement_Wedge
StepElement_Tetrahedron = StepElement_Volume3dElementShape.StepElement_Tetrahedron
StepElement_Pyramid = StepElement_Volume3dElementShape.StepElement_Pyramid

class StepElement_ElementOrder(IntEnum):
	StepElement_Linear: int = ...
	StepElement_Quadratic: int = ...
	StepElement_Cubic: int = ...
StepElement_Linear = StepElement_ElementOrder.StepElement_Linear
StepElement_Quadratic = StepElement_ElementOrder.StepElement_Quadratic
StepElement_Cubic = StepElement_ElementOrder.StepElement_Cubic

class StepElement_Element2dShape(IntEnum):
	StepElement_Quadrilateral: int = ...
	StepElement_Triangle: int = ...
StepElement_Quadrilateral = StepElement_Element2dShape.StepElement_Quadrilateral
StepElement_Triangle = StepElement_Element2dShape.StepElement_Triangle

class StepElement_EnumeratedCurveElementFreedom(IntEnum):
	StepElement_XTranslation: int = ...
	StepElement_YTranslation: int = ...
	StepElement_ZTranslation: int = ...
	StepElement_XRotation: int = ...
	StepElement_YRotation: int = ...
	StepElement_ZRotation: int = ...
	StepElement_Warp: int = ...
	StepElement_None: int = ...
StepElement_XTranslation = StepElement_EnumeratedCurveElementFreedom.StepElement_XTranslation
StepElement_YTranslation = StepElement_EnumeratedCurveElementFreedom.StepElement_YTranslation
StepElement_ZTranslation = StepElement_EnumeratedCurveElementFreedom.StepElement_ZTranslation
StepElement_XRotation = StepElement_EnumeratedCurveElementFreedom.StepElement_XRotation
StepElement_YRotation = StepElement_EnumeratedCurveElementFreedom.StepElement_YRotation
StepElement_ZRotation = StepElement_EnumeratedCurveElementFreedom.StepElement_ZRotation
StepElement_Warp = StepElement_EnumeratedCurveElementFreedom.StepElement_Warp
StepElement_None = StepElement_EnumeratedCurveElementFreedom.StepElement_None

class StepElement_EnumeratedVolumeElementPurpose(IntEnum):
	StepElement_StressDisplacement: int = ...
StepElement_StressDisplacement = StepElement_EnumeratedVolumeElementPurpose.StepElement_StressDisplacement

class StepElement_EnumeratedSurfaceElementPurpose(IntEnum):
	StepElement_MembraneDirect: int = ...
	StepElement_MembraneShear: int = ...
	StepElement_BendingDirect: int = ...
	StepElement_BendingTorsion: int = ...
	StepElement_NormalToPlaneShear: int = ...
StepElement_MembraneDirect = StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneDirect
StepElement_MembraneShear = StepElement_EnumeratedSurfaceElementPurpose.StepElement_MembraneShear
StepElement_BendingDirect = StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingDirect
StepElement_BendingTorsion = StepElement_EnumeratedSurfaceElementPurpose.StepElement_BendingTorsion
StepElement_NormalToPlaneShear = StepElement_EnumeratedSurfaceElementPurpose.StepElement_NormalToPlaneShear

class StepElement_UnspecifiedValue(IntEnum):
	StepElement_Unspecified: int = ...
StepElement_Unspecified = StepElement_UnspecifiedValue.StepElement_Unspecified

class StepElement_EnumeratedCurveElementPurpose(IntEnum):
	StepElement_Axial: int = ...
	StepElement_YYBending: int = ...
	StepElement_ZZBending: int = ...
	StepElement_Torsion: int = ...
	StepElement_XYShear: int = ...
	StepElement_XZShear: int = ...
	StepElement_Warping: int = ...
StepElement_Axial = StepElement_EnumeratedCurveElementPurpose.StepElement_Axial
StepElement_YYBending = StepElement_EnumeratedCurveElementPurpose.StepElement_YYBending
StepElement_ZZBending = StepElement_EnumeratedCurveElementPurpose.StepElement_ZZBending
StepElement_Torsion = StepElement_EnumeratedCurveElementPurpose.StepElement_Torsion
StepElement_XYShear = StepElement_EnumeratedCurveElementPurpose.StepElement_XYShear
StepElement_XZShear = StepElement_EnumeratedCurveElementPurpose.StepElement_XZShear
StepElement_Warping = StepElement_EnumeratedCurveElementPurpose.StepElement_Warping

class StepElement_AnalysisItemWithinRepresentation(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aItem: StepRepr_RepresentationItem, aRep: StepRepr_Representation) -> None: ...
	def Item(self) -> StepRepr_RepresentationItem: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def Rep(self) -> StepRepr_Representation: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetItem(self, Item: StepRepr_RepresentationItem) -> None: ...
	def SetName(self, Name: TCollection_HAsciiString) -> None: ...
	def SetRep(self, Rep: StepRepr_Representation) -> None: ...

class StepElement_CurveElementEndReleasePacket(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aReleaseFreedom: StepElement_CurveElementFreedom, aReleaseStiffness: float) -> None: ...
	def ReleaseFreedom(self) -> StepElement_CurveElementFreedom: ...
	def ReleaseStiffness(self) -> float: ...
	def SetReleaseFreedom(self, ReleaseFreedom: StepElement_CurveElementFreedom) -> None: ...
	def SetReleaseStiffness(self, ReleaseStiffness: float) -> None: ...

class StepElement_CurveElementFreedom(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApplicationDefinedDegreeOfFreedom(self) -> TCollection_HAsciiString: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def EnumeratedCurveElementFreedom(self) -> StepElement_EnumeratedCurveElementFreedom: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def SetApplicationDefinedDegreeOfFreedom(self, aVal: TCollection_HAsciiString) -> None: ...
	def SetEnumeratedCurveElementFreedom(self, aVal: StepElement_EnumeratedCurveElementFreedom) -> None: ...

class StepElement_CurveElementFreedomMember(StepData_SelectNamed):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepElement_CurveElementPurpose(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApplicationDefinedElementPurpose(self) -> TCollection_HAsciiString: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def EnumeratedCurveElementPurpose(self) -> StepElement_EnumeratedCurveElementPurpose: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def SetApplicationDefinedElementPurpose(self, aVal: TCollection_HAsciiString) -> None: ...
	def SetEnumeratedCurveElementPurpose(self, aVal: StepElement_EnumeratedCurveElementPurpose) -> None: ...

class StepElement_CurveElementPurposeMember(StepData_SelectNamed):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepElement_CurveElementSectionDefinition(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aDescription: TCollection_HAsciiString, aSectionAngle: float) -> None: ...
	def SectionAngle(self) -> float: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetSectionAngle(self, SectionAngle: float) -> None: ...

class StepElement_ElementAspect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CurveEdge(self) -> StepElement_CurveEdge: ...
	def ElementVolume(self) -> StepElement_ElementVolume: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def SetCurveEdge(self, aVal: StepElement_CurveEdge) -> None: ...
	def SetElementVolume(self, aVal: StepElement_ElementVolume) -> None: ...
	def SetSurface2dEdge(self, aVal: int) -> None: ...
	def SetSurface2dFace(self, aVal: int) -> None: ...
	def SetSurface3dEdge(self, aVal: int) -> None: ...
	def SetSurface3dFace(self, aVal: int) -> None: ...
	def SetVolume2dEdge(self, aVal: int) -> None: ...
	def SetVolume2dFace(self, aVal: int) -> None: ...
	def SetVolume3dEdge(self, aVal: int) -> None: ...
	def SetVolume3dFace(self, aVal: int) -> None: ...
	def Surface2dEdge(self) -> int: ...
	def Surface2dFace(self) -> int: ...
	def Surface3dEdge(self) -> int: ...
	def Surface3dFace(self) -> int: ...
	def Volume2dEdge(self) -> int: ...
	def Volume2dFace(self) -> int: ...
	def Volume3dEdge(self) -> int: ...
	def Volume3dFace(self) -> int: ...

class StepElement_ElementAspectMember(StepData_SelectNamed):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepElement_ElementDescriptor(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aTopologyOrder: StepElement_ElementOrder, aDescription: TCollection_HAsciiString) -> None: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetTopologyOrder(self, TopologyOrder: StepElement_ElementOrder) -> None: ...
	def TopologyOrder(self) -> StepElement_ElementOrder: ...

class StepElement_ElementMaterial(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aMaterialId: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aProperties: StepRepr_HArray1OfMaterialPropertyRepresentation) -> None: ...
	def MaterialId(self) -> TCollection_HAsciiString: ...
	def Properties(self) -> StepRepr_HArray1OfMaterialPropertyRepresentation: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetMaterialId(self, MaterialId: TCollection_HAsciiString) -> None: ...
	def SetProperties(self, Properties: StepRepr_HArray1OfMaterialPropertyRepresentation) -> None: ...

class StepElement_MeasureOrUnspecifiedValue(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ContextDependentMeasure(self) -> float: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def SetContextDependentMeasure(self, aVal: float) -> None: ...
	def SetUnspecifiedValue(self, aVal: StepElement_UnspecifiedValue) -> None: ...
	def UnspecifiedValue(self) -> StepElement_UnspecifiedValue: ...

class StepElement_MeasureOrUnspecifiedValueMember(StepData_SelectNamed):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepElement_SurfaceElementProperty(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aPropertyId: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aSection: StepElement_SurfaceSectionField) -> None: ...
	def PropertyId(self) -> TCollection_HAsciiString: ...
	def Section(self) -> StepElement_SurfaceSectionField: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetPropertyId(self, PropertyId: TCollection_HAsciiString) -> None: ...
	def SetSection(self, Section: StepElement_SurfaceSectionField) -> None: ...

class StepElement_SurfaceElementPurpose(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApplicationDefinedElementPurpose(self) -> TCollection_HAsciiString: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def EnumeratedSurfaceElementPurpose(self) -> StepElement_EnumeratedSurfaceElementPurpose: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def SetApplicationDefinedElementPurpose(self, aVal: TCollection_HAsciiString) -> None: ...
	def SetEnumeratedSurfaceElementPurpose(self, aVal: StepElement_EnumeratedSurfaceElementPurpose) -> None: ...

class StepElement_SurfaceElementPurposeMember(StepData_SelectNamed):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepElement_SurfaceSection(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aOffset: StepElement_MeasureOrUnspecifiedValue, aNonStructuralMass: StepElement_MeasureOrUnspecifiedValue, aNonStructuralMassOffset: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def NonStructuralMass(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def NonStructuralMassOffset(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def Offset(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def SetNonStructuralMass(self, NonStructuralMass: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetNonStructuralMassOffset(self, NonStructuralMassOffset: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetOffset(self, Offset: StepElement_MeasureOrUnspecifiedValue) -> None: ...

class StepElement_SurfaceSectionField(Standard_Transient):
	def __init__(self) -> None: ...

class StepElement_VolumeElementPurpose(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApplicationDefinedElementPurpose(self) -> TCollection_HAsciiString: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def EnumeratedVolumeElementPurpose(self) -> StepElement_EnumeratedVolumeElementPurpose: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def SetApplicationDefinedElementPurpose(self, aVal: TCollection_HAsciiString) -> None: ...
	def SetEnumeratedVolumeElementPurpose(self, aVal: StepElement_EnumeratedVolumeElementPurpose) -> None: ...

class StepElement_VolumeElementPurposeMember(StepData_SelectNamed):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepElement_Curve3dElementDescriptor(StepElement_ElementDescriptor):
	def __init__(self) -> None: ...
	def Init(self, aElementDescriptor_TopologyOrder: StepElement_ElementOrder, aElementDescriptor_Description: TCollection_HAsciiString, aPurpose: StepElement_HArray1OfHSequenceOfCurveElementPurposeMember) -> None: ...
	def Purpose(self) -> StepElement_HArray1OfHSequenceOfCurveElementPurposeMember: ...
	def SetPurpose(self, Purpose: StepElement_HArray1OfHSequenceOfCurveElementPurposeMember) -> None: ...

class StepElement_CurveElementSectionDerivedDefinitions(StepElement_CurveElementSectionDefinition):
	def __init__(self) -> None: ...
	def CrossSectionalArea(self) -> float: ...
	def Init(self, aCurveElementSectionDefinition_Description: TCollection_HAsciiString, aCurveElementSectionDefinition_SectionAngle: float, aCrossSectionalArea: float, aShearArea: StepElement_HArray1OfMeasureOrUnspecifiedValue, aSecondMomentOfArea: TColStd_HArray1OfReal, aTorsionalConstant: float, aWarpingConstant: StepElement_MeasureOrUnspecifiedValue, aLocationOfCentroid: StepElement_HArray1OfMeasureOrUnspecifiedValue, aLocationOfShearCentre: StepElement_HArray1OfMeasureOrUnspecifiedValue, aLocationOfNonStructuralMass: StepElement_HArray1OfMeasureOrUnspecifiedValue, aNonStructuralMass: StepElement_MeasureOrUnspecifiedValue, aPolarMoment: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def LocationOfCentroid(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: ...
	def LocationOfNonStructuralMass(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: ...
	def LocationOfShearCentre(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: ...
	def NonStructuralMass(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def PolarMoment(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def SecondMomentOfArea(self) -> TColStd_HArray1OfReal: ...
	def SetCrossSectionalArea(self, CrossSectionalArea: float) -> None: ...
	def SetLocationOfCentroid(self, LocationOfCentroid: StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: ...
	def SetLocationOfNonStructuralMass(self, LocationOfNonStructuralMass: StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: ...
	def SetLocationOfShearCentre(self, LocationOfShearCentre: StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: ...
	def SetNonStructuralMass(self, NonStructuralMass: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetPolarMoment(self, PolarMoment: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetSecondMomentOfArea(self, SecondMomentOfArea: TColStd_HArray1OfReal) -> None: ...
	def SetShearArea(self, ShearArea: StepElement_HArray1OfMeasureOrUnspecifiedValue) -> None: ...
	def SetTorsionalConstant(self, TorsionalConstant: float) -> None: ...
	def SetWarpingConstant(self, WarpingConstant: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def ShearArea(self) -> StepElement_HArray1OfMeasureOrUnspecifiedValue: ...
	def TorsionalConstant(self) -> float: ...
	def WarpingConstant(self) -> StepElement_MeasureOrUnspecifiedValue: ...

class StepElement_Surface3dElementDescriptor(StepElement_ElementDescriptor):
	def __init__(self) -> None: ...
	def Init(self, aElementDescriptor_TopologyOrder: StepElement_ElementOrder, aElementDescriptor_Description: TCollection_HAsciiString, aPurpose: StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember, aShape: StepElement_Element2dShape) -> None: ...
	def Purpose(self) -> StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember: ...
	def SetPurpose(self, Purpose: StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember) -> None: ...
	def SetShape(self, Shape: StepElement_Element2dShape) -> None: ...
	def Shape(self) -> StepElement_Element2dShape: ...

class StepElement_SurfaceSectionFieldConstant(StepElement_SurfaceSectionField):
	def __init__(self) -> None: ...
	def Definition(self) -> StepElement_SurfaceSection: ...
	def Init(self, aDefinition: StepElement_SurfaceSection) -> None: ...
	def SetDefinition(self, Definition: StepElement_SurfaceSection) -> None: ...

class StepElement_SurfaceSectionFieldVarying(StepElement_SurfaceSectionField):
	def __init__(self) -> None: ...
	def AdditionalNodeValues(self) -> bool: ...
	def Definitions(self) -> StepElement_HArray1OfSurfaceSection: ...
	def Init(self, aDefinitions: StepElement_HArray1OfSurfaceSection, aAdditionalNodeValues: bool) -> None: ...
	def SetAdditionalNodeValues(self, AdditionalNodeValues: bool) -> None: ...
	def SetDefinitions(self, Definitions: StepElement_HArray1OfSurfaceSection) -> None: ...

class StepElement_UniformSurfaceSection(StepElement_SurfaceSection):
	def __init__(self) -> None: ...
	def BendingThickness(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def Init(self, aSurfaceSection_Offset: StepElement_MeasureOrUnspecifiedValue, aSurfaceSection_NonStructuralMass: StepElement_MeasureOrUnspecifiedValue, aSurfaceSection_NonStructuralMassOffset: StepElement_MeasureOrUnspecifiedValue, aThickness: float, aBendingThickness: StepElement_MeasureOrUnspecifiedValue, aShearThickness: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetBendingThickness(self, BendingThickness: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetShearThickness(self, ShearThickness: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetThickness(self, Thickness: float) -> None: ...
	def ShearThickness(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def Thickness(self) -> float: ...

class StepElement_Volume3dElementDescriptor(StepElement_ElementDescriptor):
	def __init__(self) -> None: ...
	def Init(self, aElementDescriptor_TopologyOrder: StepElement_ElementOrder, aElementDescriptor_Description: TCollection_HAsciiString, aPurpose: StepElement_HArray1OfVolumeElementPurposeMember, aShape: StepElement_Volume3dElementShape) -> None: ...
	def Purpose(self) -> StepElement_HArray1OfVolumeElementPurposeMember: ...
	def SetPurpose(self, Purpose: StepElement_HArray1OfVolumeElementPurposeMember) -> None: ...
	def SetShape(self, Shape: StepElement_Volume3dElementShape) -> None: ...
	def Shape(self) -> StepElement_Volume3dElementShape: ...

# harray1 classes
class StepElement_HArray1OfVolumeElementPurpose(StepElement_Array1OfVolumeElementPurpose, Standard_Transient): ...

class StepElement_HArray1OfHSequenceOfCurveElementPurposeMember(StepElement_Array1OfHSequenceOfCurveElementPurposeMember, Standard_Transient): ...

class StepElement_HArray1OfSurfaceSection(StepElement_Array1OfSurfaceSection, Standard_Transient): ...

class StepElement_HArray1OfCurveElementSectionDefinition(StepElement_Array1OfCurveElementSectionDefinition, Standard_Transient): ...

class StepElement_HArray1OfMeasureOrUnspecifiedValue(StepElement_Array1OfMeasureOrUnspecifiedValue, Standard_Transient): ...

class StepElement_HArray1OfHSequenceOfSurfaceElementPurposeMember(StepElement_Array1OfHSequenceOfSurfaceElementPurposeMember, Standard_Transient): ...

class StepElement_HArray1OfVolumeElementPurposeMember(StepElement_Array1OfVolumeElementPurposeMember, Standard_Transient): ...

class StepElement_HArray1OfCurveElementEndReleasePacket(StepElement_Array1OfCurveElementEndReleasePacket, Standard_Transient): ...

# harray2 classes

class StepElement_HArray2OfSurfaceElementPurposeMember(StepElement_Array2OfSurfaceElementPurposeMember, Standard_Transient): ...


class StepElement_HArray2OfSurfaceElementPurpose(StepElement_Array2OfSurfaceElementPurpose, Standard_Transient): ...


class StepElement_HArray2OfCurveElementPurposeMember(StepElement_Array2OfCurveElementPurposeMember, Standard_Transient): ...

# harray2 classes

class StepElement_HSequenceOfCurveElementSectionDefinition(StepElement_SequenceOfCurveElementSectionDefinition, Standard_Transient): ...


class StepElement_HSequenceOfCurveElementPurposeMember(StepElement_SequenceOfCurveElementPurposeMember, Standard_Transient): ...


class StepElement_HSequenceOfElementMaterial(StepElement_SequenceOfElementMaterial, Standard_Transient): ...


class StepElement_HSequenceOfSurfaceElementPurposeMember(StepElement_SequenceOfSurfaceElementPurposeMember, Standard_Transient): ...


