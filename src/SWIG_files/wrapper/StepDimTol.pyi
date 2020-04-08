from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepRepr import *
from OCC.Core.TCollection import *
from OCC.Core.StepData import *
from OCC.Core.StepBasic import *
from OCC.Core.StepShape import *


class StepDimTol_LimitCondition(IntEnum):
	StepDimTol_MaximumMaterialCondition: int = ...
	StepDimTol_LeastMaterialCondition: int = ...
	StepDimTol_RegardlessOfFeatureSize: int = ...
StepDimTol_MaximumMaterialCondition = StepDimTol_LimitCondition.StepDimTol_MaximumMaterialCondition
StepDimTol_LeastMaterialCondition = StepDimTol_LimitCondition.StepDimTol_LeastMaterialCondition
StepDimTol_RegardlessOfFeatureSize = StepDimTol_LimitCondition.StepDimTol_RegardlessOfFeatureSize

class StepDimTol_GeometricToleranceType(IntEnum):
	StepDimTol_GTTAngularityTolerance: int = ...
	StepDimTol_GTTCircularRunoutTolerance: int = ...
	StepDimTol_GTTCoaxialityTolerance: int = ...
	StepDimTol_GTTConcentricityTolerance: int = ...
	StepDimTol_GTTCylindricityTolerance: int = ...
	StepDimTol_GTTFlatnessTolerance: int = ...
	StepDimTol_GTTLineProfileTolerance: int = ...
	StepDimTol_GTTParallelismTolerance: int = ...
	StepDimTol_GTTPerpendicularityTolerance: int = ...
	StepDimTol_GTTPositionTolerance: int = ...
	StepDimTol_GTTRoundnessTolerance: int = ...
	StepDimTol_GTTStraightnessTolerance: int = ...
	StepDimTol_GTTSurfaceProfileTolerance: int = ...
	StepDimTol_GTTSymmetryTolerance: int = ...
	StepDimTol_GTTTotalRunoutTolerance: int = ...
StepDimTol_GTTAngularityTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTAngularityTolerance
StepDimTol_GTTCircularRunoutTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTCircularRunoutTolerance
StepDimTol_GTTCoaxialityTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTCoaxialityTolerance
StepDimTol_GTTConcentricityTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTConcentricityTolerance
StepDimTol_GTTCylindricityTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTCylindricityTolerance
StepDimTol_GTTFlatnessTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTFlatnessTolerance
StepDimTol_GTTLineProfileTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTLineProfileTolerance
StepDimTol_GTTParallelismTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTParallelismTolerance
StepDimTol_GTTPerpendicularityTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTPerpendicularityTolerance
StepDimTol_GTTPositionTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTPositionTolerance
StepDimTol_GTTRoundnessTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTRoundnessTolerance
StepDimTol_GTTStraightnessTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTStraightnessTolerance
StepDimTol_GTTSurfaceProfileTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTSurfaceProfileTolerance
StepDimTol_GTTSymmetryTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTSymmetryTolerance
StepDimTol_GTTTotalRunoutTolerance = StepDimTol_GeometricToleranceType.StepDimTol_GTTTotalRunoutTolerance

class StepDimTol_DatumReferenceModifierType(IntEnum):
	StepDimTol_CircularOrCylindrical: int = ...
	StepDimTol_Distance: int = ...
	StepDimTol_Projected: int = ...
	StepDimTol_Spherical: int = ...
StepDimTol_CircularOrCylindrical = StepDimTol_DatumReferenceModifierType.StepDimTol_CircularOrCylindrical
StepDimTol_Distance = StepDimTol_DatumReferenceModifierType.StepDimTol_Distance
StepDimTol_Projected = StepDimTol_DatumReferenceModifierType.StepDimTol_Projected
StepDimTol_Spherical = StepDimTol_DatumReferenceModifierType.StepDimTol_Spherical

class StepDimTol_SimpleDatumReferenceModifier(IntEnum):
	StepDimTol_SDRMAnyCrossSection: int = ...
	StepDimTol_SDRMAnyLongitudinalSection: int = ...
	StepDimTol_SDRMBasic: int = ...
	StepDimTol_SDRMContactingFeature: int = ...
	StepDimTol_SDRMDegreeOfFreedomConstraintU: int = ...
	StepDimTol_SDRMDegreeOfFreedomConstraintV: int = ...
	StepDimTol_SDRMDegreeOfFreedomConstraintW: int = ...
	StepDimTol_SDRMDegreeOfFreedomConstraintX: int = ...
	StepDimTol_SDRMDegreeOfFreedomConstraintY: int = ...
	StepDimTol_SDRMDegreeOfFreedomConstraintZ: int = ...
	StepDimTol_SDRMDistanceVariable: int = ...
	StepDimTol_SDRMFreeState: int = ...
	StepDimTol_SDRMLeastMaterialRequirement: int = ...
	StepDimTol_SDRMLine: int = ...
	StepDimTol_SDRMMajorDiameter: int = ...
	StepDimTol_SDRMMaximumMaterialRequirement: int = ...
	StepDimTol_SDRMMinorDiameter: int = ...
	StepDimTol_SDRMOrientation: int = ...
	StepDimTol_SDRMPitchDiameter: int = ...
	StepDimTol_SDRMPlane: int = ...
	StepDimTol_SDRMPoint: int = ...
	StepDimTol_SDRMTranslation: int = ...
StepDimTol_SDRMAnyCrossSection = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyCrossSection
StepDimTol_SDRMAnyLongitudinalSection = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMAnyLongitudinalSection
StepDimTol_SDRMBasic = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMBasic
StepDimTol_SDRMContactingFeature = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMContactingFeature
StepDimTol_SDRMDegreeOfFreedomConstraintU = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintU
StepDimTol_SDRMDegreeOfFreedomConstraintV = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintV
StepDimTol_SDRMDegreeOfFreedomConstraintW = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintW
StepDimTol_SDRMDegreeOfFreedomConstraintX = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintX
StepDimTol_SDRMDegreeOfFreedomConstraintY = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintY
StepDimTol_SDRMDegreeOfFreedomConstraintZ = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDegreeOfFreedomConstraintZ
StepDimTol_SDRMDistanceVariable = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMDistanceVariable
StepDimTol_SDRMFreeState = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMFreeState
StepDimTol_SDRMLeastMaterialRequirement = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLeastMaterialRequirement
StepDimTol_SDRMLine = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMLine
StepDimTol_SDRMMajorDiameter = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMajorDiameter
StepDimTol_SDRMMaximumMaterialRequirement = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMaximumMaterialRequirement
StepDimTol_SDRMMinorDiameter = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMMinorDiameter
StepDimTol_SDRMOrientation = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMOrientation
StepDimTol_SDRMPitchDiameter = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPitchDiameter
StepDimTol_SDRMPlane = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPlane
StepDimTol_SDRMPoint = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMPoint
StepDimTol_SDRMTranslation = StepDimTol_SimpleDatumReferenceModifier.StepDimTol_SDRMTranslation

class StepDimTol_AreaUnitType(IntEnum):
	StepDimTol_Circular: int = ...
	StepDimTol_Rectangular: int = ...
	StepDimTol_Square: int = ...
StepDimTol_Circular = StepDimTol_AreaUnitType.StepDimTol_Circular
StepDimTol_Rectangular = StepDimTol_AreaUnitType.StepDimTol_Rectangular
StepDimTol_Square = StepDimTol_AreaUnitType.StepDimTol_Square

class StepDimTol_GeometricToleranceModifier(IntEnum):
	StepDimTol_GTMAnyCrossSection: int = ...
	StepDimTol_GTMCommonZone: int = ...
	StepDimTol_GTMEachRadialElement: int = ...
	StepDimTol_GTMFreeState: int = ...
	StepDimTol_GTMLeastMaterialRequirement: int = ...
	StepDimTol_GTMLineElement: int = ...
	StepDimTol_GTMMajorDiameter: int = ...
	StepDimTol_GTMMaximumMaterialRequirement: int = ...
	StepDimTol_GTMMinorDiameter: int = ...
	StepDimTol_GTMNotConvex: int = ...
	StepDimTol_GTMPitchDiameter: int = ...
	StepDimTol_GTMReciprocityRequirement: int = ...
	StepDimTol_GTMSeparateRequirement: int = ...
	StepDimTol_GTMStatisticalTolerance: int = ...
	StepDimTol_GTMTangentPlane: int = ...
StepDimTol_GTMAnyCrossSection = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMAnyCrossSection
StepDimTol_GTMCommonZone = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMCommonZone
StepDimTol_GTMEachRadialElement = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMEachRadialElement
StepDimTol_GTMFreeState = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMFreeState
StepDimTol_GTMLeastMaterialRequirement = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLeastMaterialRequirement
StepDimTol_GTMLineElement = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMLineElement
StepDimTol_GTMMajorDiameter = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMajorDiameter
StepDimTol_GTMMaximumMaterialRequirement = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMaximumMaterialRequirement
StepDimTol_GTMMinorDiameter = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMMinorDiameter
StepDimTol_GTMNotConvex = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMNotConvex
StepDimTol_GTMPitchDiameter = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMPitchDiameter
StepDimTol_GTMReciprocityRequirement = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMReciprocityRequirement
StepDimTol_GTMSeparateRequirement = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMSeparateRequirement
StepDimTol_GTMStatisticalTolerance = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMStatisticalTolerance
StepDimTol_GTMTangentPlane = StepDimTol_GeometricToleranceModifier.StepDimTol_GTMTangentPlane

class StepDimTol_CommonDatum(StepRepr_CompositeShapeAspect):
	def __init__(self) -> None: ...
	def Datum(self) -> StepDimTol_Datum: ...
	def Init(self, theShapeAspect_Name: TCollection_HAsciiString, theShapeAspect_Description: TCollection_HAsciiString, theShapeAspect_OfShape: StepRepr_ProductDefinitionShape, theShapeAspect_ProductDefinitional: StepData_Logical, theDatum_Name: TCollection_HAsciiString, theDatum_Description: TCollection_HAsciiString, theDatum_OfShape: StepRepr_ProductDefinitionShape, theDatum_ProductDefinitional: StepData_Logical, theDatum_Identification: TCollection_HAsciiString) -> None: ...
	def SetDatum(self, theDatum: StepDimTol_Datum) -> None: ...

class StepDimTol_Datum(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...
	def Identification(self) -> TCollection_HAsciiString: ...
	def Init(self, theShapeAspect_Name: TCollection_HAsciiString, theShapeAspect_Description: TCollection_HAsciiString, theShapeAspect_OfShape: StepRepr_ProductDefinitionShape, theShapeAspect_ProductDefinitional: StepData_Logical, theIdentification: TCollection_HAsciiString) -> None: ...
	def SetIdentification(self, theIdentification: TCollection_HAsciiString) -> None: ...

class StepDimTol_DatumFeature(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...

class StepDimTol_DatumOrCommonDatum(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def CommonDatumList(self) -> StepDimTol_HArray1OfDatumReferenceElement: ...
	def Datum(self) -> StepDimTol_Datum: ...

class StepDimTol_DatumReference(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, thePrecedence: int, theReferencedDatum: StepDimTol_Datum) -> None: ...
	def Precedence(self) -> int: ...
	def ReferencedDatum(self) -> StepDimTol_Datum: ...
	def SetPrecedence(self, thePrecedence: int) -> None: ...
	def SetReferencedDatum(self, theReferencedDatum: StepDimTol_Datum) -> None: ...

class StepDimTol_DatumReferenceModifier(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DatumReferenceModifierWithValue(self) -> StepDimTol_DatumReferenceModifierWithValue: ...
	def SimpleDatumReferenceModifierMember(self) -> StepDimTol_SimpleDatumReferenceModifierMember: ...

class StepDimTol_DatumReferenceModifierWithValue(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, theModifierType: StepDimTol_DatumReferenceModifierType, theModifierValue: StepBasic_LengthMeasureWithUnit) -> None: ...
	def ModifierType(self) -> StepDimTol_DatumReferenceModifierType: ...
	def ModifierValue(self) -> StepBasic_LengthMeasureWithUnit: ...
	def SetModifierType(self, theModifierType: StepDimTol_DatumReferenceModifierType) -> None: ...
	def SetModifierValue(self, theModifierValue: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepDimTol_DatumSystem(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...
	def Constituents(self) -> StepDimTol_HArray1OfDatumReferenceCompartment: ...
	@overload
	def ConstituentsValue(self, num: int) -> StepDimTol_DatumReferenceCompartment: ...
	@overload
	def ConstituentsValue(self, num: int, theItem: StepDimTol_DatumReferenceCompartment) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theOfShape: StepRepr_ProductDefinitionShape, theProductDefinitional: StepData_Logical, theConstituents: StepDimTol_HArray1OfDatumReferenceCompartment) -> None: ...
	def NbConstituents(self) -> int: ...
	def SetConstituents(self, theConstituents: StepDimTol_HArray1OfDatumReferenceCompartment) -> None: ...

class StepDimTol_DatumSystemOrReference(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DatumReference(self) -> StepDimTol_DatumReference: ...
	def DatumSystem(self) -> StepDimTol_DatumSystem: ...

class StepDimTol_DatumTarget(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...
	def Init(self, theShapeAspect_Name: TCollection_HAsciiString, theShapeAspect_Description: TCollection_HAsciiString, theShapeAspect_OfShape: StepRepr_ProductDefinitionShape, theShapeAspect_ProductDefinitional: StepData_Logical, theTargetId: TCollection_HAsciiString) -> None: ...
	def SetTargetId(self, theTargetId: TCollection_HAsciiString) -> None: ...
	def TargetId(self) -> TCollection_HAsciiString: ...

class StepDimTol_GeneralDatumReference(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...
	def Base(self) -> StepDimTol_DatumOrCommonDatum: ...
	def HasModifiers(self) -> bool: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theOfShape: StepRepr_ProductDefinitionShape, theProductDefinitional: StepData_Logical, theBase: StepDimTol_DatumOrCommonDatum, theHasModifiers: bool, theModifiers: StepDimTol_HArray1OfDatumReferenceModifier) -> None: ...
	def Modifiers(self) -> StepDimTol_HArray1OfDatumReferenceModifier: ...
	@overload
	def ModifiersValue(self, theNum: int) -> StepDimTol_DatumReferenceModifier: ...
	@overload
	def ModifiersValue(self, theNum: int, theItem: StepDimTol_DatumReferenceModifier) -> None: ...
	def NbModifiers(self) -> int: ...
	def SetBase(self, theBase: StepDimTol_DatumOrCommonDatum) -> None: ...
	def SetModifiers(self, theModifiers: StepDimTol_HArray1OfDatumReferenceModifier) -> None: ...

class StepDimTol_GeometricTolerance(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect) -> None: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget) -> None: ...
	def Magnitude(self) -> StepBasic_MeasureWithUnit: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetDescription(self, theDescription: TCollection_HAsciiString) -> None: ...
	def SetMagnitude(self, theMagnitude: StepBasic_MeasureWithUnit) -> None: ...
	def SetName(self, theName: TCollection_HAsciiString) -> None: ...
	@overload
	def SetTolerancedShapeAspect(self, theTolerancedShapeAspect: StepRepr_ShapeAspect) -> None: ...
	@overload
	def SetTolerancedShapeAspect(self, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget) -> None: ...
	def TolerancedShapeAspect(self) -> StepDimTol_GeometricToleranceTarget: ...

class StepDimTol_GeometricToleranceRelationship(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theRelatingGeometricTolerance: StepDimTol_GeometricTolerance, theRelatedGeometricTolerance: StepDimTol_GeometricTolerance) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def RelatedGeometricTolerance(self) -> StepDimTol_GeometricTolerance: ...
	def RelatingGeometricTolerance(self) -> StepDimTol_GeometricTolerance: ...
	def SetDescription(self, theDescription: TCollection_HAsciiString) -> None: ...
	def SetName(self, theName: TCollection_HAsciiString) -> None: ...
	def SetRelatedGeometricTolerance(self, theRelatedGeometricTolerance: StepDimTol_GeometricTolerance) -> None: ...
	def SetRelatingGeometricTolerance(self, theRelatingGeometricTolerance: StepDimTol_GeometricTolerance) -> None: ...

class StepDimTol_GeometricToleranceTarget(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DimensionalLocation(self) -> StepShape_DimensionalLocation: ...
	def DimensionalSize(self) -> StepShape_DimensionalSize: ...
	def ProductDefinitionShape(self) -> StepRepr_ProductDefinitionShape: ...
	def ShapeAspect(self) -> StepRepr_ShapeAspect: ...

class StepDimTol_RunoutZoneOrientation(Standard_Transient):
	def __init__(self) -> None: ...
	def Angle(self) -> StepBasic_PlaneAngleMeasureWithUnit: ...
	def Init(self, theAngle: StepBasic_PlaneAngleMeasureWithUnit) -> None: ...
	def SetAngle(self, theAngle: StepBasic_PlaneAngleMeasureWithUnit) -> None: ...

class StepDimTol_ShapeToleranceSelect(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def GeometricTolerance(self) -> StepDimTol_GeometricTolerance: ...
	def PlusMinusTolerance(self) -> StepShape_PlusMinusTolerance: ...

class StepDimTol_SimpleDatumReferenceModifierMember(StepData_SelectInt):
	def __init__(self) -> None: ...
	def EnumText(self) -> str: ...
	def HasName(self) -> bool: ...
	def Kind(self) -> int: ...
	def Name(self) -> str: ...
	def SetEnumText(self, theValue: int, theText: str) -> None: ...
	def SetValue(self, theValue: StepDimTol_SimpleDatumReferenceModifier) -> None: ...
	def Value(self) -> StepDimTol_SimpleDatumReferenceModifier: ...

class StepDimTol_ToleranceZone(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...
	def DefiningTolerance(self) -> StepDimTol_HArray1OfToleranceZoneTarget: ...
	def DefiningToleranceValue(self, theNum: int) -> StepDimTol_ToleranceZoneTarget: ...
	def Form(self) -> StepDimTol_ToleranceZoneForm: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theOfShape: StepRepr_ProductDefinitionShape, theProductDefinitional: StepData_Logical, theDefiningTolerance: StepDimTol_HArray1OfToleranceZoneTarget, theForm: StepDimTol_ToleranceZoneForm) -> None: ...
	def NbDefiningTolerances(self) -> int: ...
	def SetDefiningTolerance(self, theDefiningTolerance: StepDimTol_HArray1OfToleranceZoneTarget) -> None: ...
	def SetDefiningToleranceValue(self, theNum: int, theItem: StepDimTol_ToleranceZoneTarget) -> None: ...
	def SetForm(self, theForm: StepDimTol_ToleranceZoneForm) -> None: ...

class StepDimTol_ToleranceZoneDefinition(Standard_Transient):
	def __init__(self) -> None: ...
	def Boundaries(self) -> StepRepr_HArray1OfShapeAspect: ...
	def BoundariesValue(self, theNum: int) -> StepRepr_ShapeAspect: ...
	def Init(self, theZone: StepDimTol_ToleranceZone, theBoundaries: StepRepr_HArray1OfShapeAspect) -> None: ...
	def NbBoundaries(self) -> int: ...
	def SetBoundaries(self, theBoundaries: StepRepr_HArray1OfShapeAspect) -> None: ...
	def SetBoundariesValue(self, theNum: int, theItem: StepRepr_ShapeAspect) -> None: ...
	def SetZone(self, theZone: StepDimTol_ToleranceZone) -> None: ...
	def Zone(self) -> StepDimTol_ToleranceZone: ...

class StepDimTol_ToleranceZoneForm(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString) -> None: ...
	def Name(self) -> TCollection_HAsciiString: ...
	def SetName(self, theName: TCollection_HAsciiString) -> None: ...

class StepDimTol_ToleranceZoneTarget(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def DimensionalLocation(self) -> StepShape_DimensionalLocation: ...
	def DimensionalSize(self) -> StepShape_DimensionalSize: ...
	def GeneralDatumReference(self) -> StepDimTol_GeneralDatumReference: ...
	def GeometricTolerance(self) -> StepDimTol_GeometricTolerance: ...

class StepDimTol_CylindricityTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...

class StepDimTol_DatumReferenceCompartment(StepDimTol_GeneralDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_DatumReferenceElement(StepDimTol_GeneralDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_FlatnessTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...

class StepDimTol_GeoTolAndGeoTolWthDatRef(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: ...
	def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference, theType: StepDimTol_GeometricToleranceType) -> None: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetGeometricToleranceType(self, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetGeometricToleranceWithDatumReference(self, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference) -> None: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: ...
	def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: ...
	def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference, theGTWM: StepDimTol_GeometricToleranceWithModifiers, theType: StepDimTol_GeometricToleranceType) -> None: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference, aGTWM: StepDimTol_GeometricToleranceWithModifiers, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetGeometricToleranceType(self, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetGeometricToleranceWithDatumReference(self, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference) -> None: ...
	def SetGeometricToleranceWithModifiers(self, theGTWM: StepDimTol_GeometricToleranceWithModifiers) -> None: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	def GetGeometricToleranceWithDatumReference(self) -> StepDimTol_GeometricToleranceWithDatumReference: ...
	def GetModifiedGeometricTolerance(self) -> StepDimTol_ModifiedGeometricTolerance: ...
	def GetPositionTolerance(self) -> StepDimTol_PositionTolerance: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepRepr_ShapeAspect, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference, aMGT: StepDimTol_ModifiedGeometricTolerance) -> None: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference, aMGT: StepDimTol_ModifiedGeometricTolerance) -> None: ...
	def SetGeometricToleranceWithDatumReference(self, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference) -> None: ...
	def SetModifiedGeometricTolerance(self, aMGT: StepDimTol_ModifiedGeometricTolerance) -> None: ...
	def SetPositionTolerance(self, aPT: StepDimTol_PositionTolerance) -> None: ...

class StepDimTol_GeoTolAndGeoTolWthMod(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	def GetGeometricToleranceWithModifiers(self) -> StepDimTol_GeometricToleranceWithModifiers: ...
	def GetToleranceType(self) -> StepDimTol_GeometricToleranceType: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect, theGTWM: StepDimTol_GeometricToleranceWithModifiers, theType: StepDimTol_GeometricToleranceType) -> None: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWM: StepDimTol_GeometricToleranceWithModifiers, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetGeometricToleranceType(self, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetGeometricToleranceWithModifiers(self, theGTWM: StepDimTol_GeometricToleranceWithModifiers) -> None: ...

class StepDimTol_GeometricToleranceWithDatumReference(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	def DatumSystem(self) -> StepDimTol_HArray1OfDatumReference: ...
	def DatumSystemAP242(self) -> StepDimTol_HArray1OfDatumSystemOrReference: ...
	@overload
	def Init(self, theGeometricTolerance_Name: TCollection_HAsciiString, theGeometricTolerance_Description: TCollection_HAsciiString, theGeometricTolerance_Magnitude: StepBasic_MeasureWithUnit, theGeometricTolerance_TolerancedShapeAspect: StepRepr_ShapeAspect, theDatumSystem: StepDimTol_HArray1OfDatumReference) -> None: ...
	@overload
	def Init(self, theGeometricTolerance_Name: TCollection_HAsciiString, theGeometricTolerance_Description: TCollection_HAsciiString, theGeometricTolerance_Magnitude: StepBasic_MeasureWithUnit, theGeometricTolerance_TolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theDatumSystem: StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...
	@overload
	def SetDatumSystem(self, theDatumSystem: StepDimTol_HArray1OfDatumReference) -> None: ...
	@overload
	def SetDatumSystem(self, theDatumSystem: StepDimTol_HArray1OfDatumSystemOrReference) -> None: ...

class StepDimTol_GeometricToleranceWithDefinedUnit(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect, theUnitSize: StepBasic_LengthMeasureWithUnit) -> None: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theUnitSize: StepBasic_LengthMeasureWithUnit) -> None: ...
	def SetUnitSize(self, theUnitSize: StepBasic_LengthMeasureWithUnit) -> None: ...
	def UnitSize(self) -> StepBasic_LengthMeasureWithUnit: ...

class StepDimTol_GeometricToleranceWithModifiers(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theModifiers: StepDimTol_HArray1OfGeometricToleranceModifier) -> None: ...
	def ModifierValue(self, theNum: int) -> StepDimTol_GeometricToleranceModifier: ...
	def Modifiers(self) -> StepDimTol_HArray1OfGeometricToleranceModifier: ...
	def NbModifiers(self) -> int: ...
	def SetModifierValue(self, theNum: int, theItem: StepDimTol_GeometricToleranceModifier) -> None: ...
	def SetModifiers(self, theModifiers: StepDimTol_HArray1OfGeometricToleranceModifier) -> None: ...

class StepDimTol_LineProfileTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...

class StepDimTol_ModifiedGeometricTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	@overload
	def Init(self, theGeometricTolerance_Name: TCollection_HAsciiString, theGeometricTolerance_Description: TCollection_HAsciiString, theGeometricTolerance_Magnitude: StepBasic_MeasureWithUnit, theGeometricTolerance_TolerancedShapeAspect: StepRepr_ShapeAspect, theModifier: StepDimTol_LimitCondition) -> None: ...
	@overload
	def Init(self, theGeometricTolerance_Name: TCollection_HAsciiString, theGeometricTolerance_Description: TCollection_HAsciiString, theGeometricTolerance_Magnitude: StepBasic_MeasureWithUnit, theGeometricTolerance_TolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theModifier: StepDimTol_LimitCondition) -> None: ...
	def Modifier(self) -> StepDimTol_LimitCondition: ...
	def SetModifier(self, theModifier: StepDimTol_LimitCondition) -> None: ...

class StepDimTol_NonUniformZoneDefinition(StepDimTol_ToleranceZoneDefinition):
	def __init__(self) -> None: ...

class StepDimTol_PlacedDatumTargetFeature(StepDimTol_DatumTarget):
	def __init__(self) -> None: ...

class StepDimTol_PositionTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...

class StepDimTol_ProjectedZoneDefinition(StepDimTol_ToleranceZoneDefinition):
	def __init__(self) -> None: ...
	def Init(self, theZone: StepDimTol_ToleranceZone, theBoundaries: StepRepr_HArray1OfShapeAspect, theProjectionEnd: StepRepr_ShapeAspect, theProjectionLength: StepBasic_LengthMeasureWithUnit) -> None: ...
	def ProjectionEnd(self) -> StepRepr_ShapeAspect: ...
	def ProjectionLength(self) -> StepBasic_LengthMeasureWithUnit: ...
	def SetProjectionEnd(self, theProjectionEnd: StepRepr_ShapeAspect) -> None: ...
	def SetProjectionLength(self, theProjectionLength: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepDimTol_RoundnessTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...

class StepDimTol_RunoutZoneDefinition(StepDimTol_ToleranceZoneDefinition):
	def __init__(self) -> None: ...
	def Init(self, theZone: StepDimTol_ToleranceZone, theBoundaries: StepRepr_HArray1OfShapeAspect, theOrientation: StepDimTol_RunoutZoneOrientation) -> None: ...
	def Orientation(self) -> StepDimTol_RunoutZoneOrientation: ...
	def SetOrientation(self, theOrientation: StepDimTol_RunoutZoneOrientation) -> None: ...

class StepDimTol_StraightnessTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...

class StepDimTol_SurfaceProfileTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...

class StepDimTol_UnequallyDisposedGeometricTolerance(StepDimTol_GeometricTolerance):
	def __init__(self) -> None: ...
	def Displacement(self) -> StepBasic_LengthMeasureWithUnit: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theDisplacement: StepBasic_LengthMeasureWithUnit) -> None: ...
	def SetDisplacement(self, theDisplacement: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepDimTol_AngularityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_CircularRunoutTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_CoaxialityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_ConcentricityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol(StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod):
	def __init__(self) -> None: ...
	def GetMaxTolerance(self) -> StepBasic_LengthMeasureWithUnit: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference, theGTWM: StepDimTol_GeometricToleranceWithModifiers, theMaxTol: StepBasic_LengthMeasureWithUnit, theType: StepDimTol_GeometricToleranceType) -> None: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference, aGTWM: StepDimTol_GeometricToleranceWithModifiers, theMaxTol: StepBasic_LengthMeasureWithUnit, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetMaxTolerance(self, theMaxTol: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol(StepDimTol_GeoTolAndGeoTolWthDatRef):
	def __init__(self) -> None: ...
	def GetUnequallyDisposedGeometricTolerance(self) -> StepDimTol_UnequallyDisposedGeometricTolerance: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect, theGTWDR: StepDimTol_GeometricToleranceWithDatumReference, theType: StepDimTol_GeometricToleranceType, theUDGT: StepDimTol_UnequallyDisposedGeometricTolerance) -> None: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWDR: StepDimTol_GeometricToleranceWithDatumReference, theType: StepDimTol_GeometricToleranceType, theUDGT: StepDimTol_UnequallyDisposedGeometricTolerance) -> None: ...
	def SetUnequallyDisposedGeometricTolerance(self, theUDGT: StepDimTol_UnequallyDisposedGeometricTolerance) -> None: ...

class StepDimTol_GeoTolAndGeoTolWthMaxTol(StepDimTol_GeoTolAndGeoTolWthMod):
	def __init__(self) -> None: ...
	def GetMaxTolerance(self) -> StepBasic_LengthMeasureWithUnit: ...
	@overload
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepRepr_ShapeAspect, theGTWM: StepDimTol_GeometricToleranceWithModifiers, theMaxTol: StepBasic_LengthMeasureWithUnit, theType: StepDimTol_GeometricToleranceType) -> None: ...
	@overload
	def Init(self, aName: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aMagnitude: StepBasic_MeasureWithUnit, aTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, aGTWM: StepDimTol_GeometricToleranceWithModifiers, theMaxTol: StepBasic_LengthMeasureWithUnit, theType: StepDimTol_GeometricToleranceType) -> None: ...
	def SetMaxTolerance(self, theMaxTol: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepDimTol_GeometricToleranceWithDefinedAreaUnit(StepDimTol_GeometricToleranceWithDefinedUnit):
	def __init__(self) -> None: ...
	def AreaType(self) -> StepDimTol_AreaUnitType: ...
	def HasSecondUnitSize(self) -> bool: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theUnitSize: StepBasic_LengthMeasureWithUnit, theAreaType: StepDimTol_AreaUnitType, theHasSecondUnitSize: bool, theSecondUnitSize: StepBasic_LengthMeasureWithUnit) -> None: ...
	def SecondUnitSize(self) -> StepBasic_LengthMeasureWithUnit: ...
	def SetAreaType(self, theAreaType: StepDimTol_AreaUnitType) -> None: ...
	def SetSecondUnitSize(self, theSecondUnitSize: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepDimTol_GeometricToleranceWithMaximumTolerance(StepDimTol_GeometricToleranceWithModifiers):
	def __init__(self) -> None: ...
	def Init(self, theName: TCollection_HAsciiString, theDescription: TCollection_HAsciiString, theMagnitude: StepBasic_MeasureWithUnit, theTolerancedShapeAspect: StepDimTol_GeometricToleranceTarget, theModifiers: StepDimTol_HArray1OfGeometricToleranceModifier, theUnitSize: StepBasic_LengthMeasureWithUnit) -> None: ...
	def MaximumUpperTolerance(self) -> StepBasic_LengthMeasureWithUnit: ...
	def SetMaximumUpperTolerance(self, theMaximumUpperTolerance: StepBasic_LengthMeasureWithUnit) -> None: ...

class StepDimTol_ParallelismTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_PerpendicularityTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_SymmetryTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...

class StepDimTol_TotalRunoutTolerance(StepDimTol_GeometricToleranceWithDatumReference):
	def __init__(self) -> None: ...
