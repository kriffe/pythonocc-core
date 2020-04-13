from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.GProp import *
from OCC.Core.gp import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColgp import *
from OCC.Core.math import *


class brepgprop:
	@staticmethod
	def LinearProperties(self, S: TopoDS_Shape, LProps: GProp_GProps, SkipShared: Optional[bool], UseTriangulation: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def SurfaceProperties(self, S: TopoDS_Shape, SProps: GProp_GProps, SkipShared: Optional[bool], UseTriangulation: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def SurfaceProperties(self, S: TopoDS_Shape, SProps: GProp_GProps, Eps: float, SkipShared: Optional[bool]) -> float: ...
	@overload
	@staticmethod
	def VolumeProperties(self, S: TopoDS_Shape, VProps: GProp_GProps, OnlyClosed: Optional[bool], SkipShared: Optional[bool], UseTriangulation: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def VolumeProperties(self, S: TopoDS_Shape, VProps: GProp_GProps, Eps: float, OnlyClosed: Optional[bool], SkipShared: Optional[bool]) -> float: ...
	@overload
	@staticmethod
	def VolumePropertiesGK(self, S: TopoDS_Shape, VProps: GProp_GProps, Eps: Optional[float], OnlyClosed: Optional[bool], IsUseSpan: Optional[bool], CGFlag: Optional[bool], IFlag: Optional[bool], SkipShared: Optional[bool]) -> float: ...
	@overload
	@staticmethod
	def VolumePropertiesGK(self, S: TopoDS_Shape, VProps: GProp_GProps, thePln: gp_Pln, Eps: Optional[float], OnlyClosed: Optional[bool], IsUseSpan: Optional[bool], CGFlag: Optional[bool], IFlag: Optional[bool], SkipShared: Optional[bool]) -> float: ...

class BRepGProp_Cinert(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: BRepAdaptor_Curve, CLocation: gp_Pnt) -> None: ...
	def Perform(self, C: BRepAdaptor_Curve) -> None: ...
	def SetLocation(self, CLocation: gp_Pnt) -> None: ...

class BRepGProp_Domain:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face) -> None: ...
	@overload
	def Init(self, F: TopoDS_Face) -> None: ...
	@overload
	def Init(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Value(self) -> TopoDS_Edge: ...

class BRepGProp_EdgeTool:
	@staticmethod
	def D1(self, C: BRepAdaptor_Curve, U: float, P: gp_Pnt, V1: gp_Vec) -> None: ...
	@staticmethod
	def FirstParameter(self, C: BRepAdaptor_Curve) -> float: ...
	@staticmethod
	def IntegrationOrder(self, C: BRepAdaptor_Curve) -> int: ...
	@staticmethod
	def Intervals(self, C: BRepAdaptor_Curve, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	@staticmethod
	def LastParameter(self, C: BRepAdaptor_Curve) -> float: ...
	@staticmethod
	def NbIntervals(self, C: BRepAdaptor_Curve, S: GeomAbs_Shape) -> int: ...
	@staticmethod
	def Value(self, C: BRepAdaptor_Curve, U: float) -> gp_Pnt: ...

class BRepGProp_Face:
	@overload
	def __init__(self, IsUseSpan: Optional[bool]) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face, IsUseSpan: Optional[bool]) -> None: ...
	def Bounds(self) -> Tuple[float, float, float, float]: ...
	def D12d(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d) -> None: ...
	def FirstParameter(self) -> float: ...
	def GetFace(self) -> TopoDS_Face: ...
	def GetTKnots(self, theTMin: float, theTMax: float, theTKnots: TColStd_HArray1OfReal) -> None: ...
	def GetUKnots(self, theUMin: float, theUMax: float, theUKnots: TColStd_HArray1OfReal) -> None: ...
	def IntegrationOrder(self) -> int: ...
	def LIntOrder(self, Eps: float) -> int: ...
	def LIntSubs(self) -> int: ...
	def LKnots(self, Knots: TColStd_Array1OfReal) -> None: ...
	def LastParameter(self) -> float: ...
	@overload
	def Load(self, F: TopoDS_Face) -> None: ...
	@overload
	def Load(self, E: TopoDS_Edge) -> False: ...
	@overload
	def Load(self, IsFirstParam: bool, theIsoType: GeomAbs_IsoType) -> None: ...
	def NaturalRestriction(self) -> bool: ...
	def Normal(self, U: float, V: float, P: gp_Pnt, VNor: gp_Vec) -> None: ...
	def SIntOrder(self, Eps: float) -> int: ...
	def SUIntSubs(self) -> int: ...
	def SVIntSubs(self) -> int: ...
	def UIntegrationOrder(self) -> int: ...
	def UKnots(self, Knots: TColStd_Array1OfReal) -> None: ...
	def VIntegrationOrder(self) -> int: ...
	def VKnots(self, Knots: TColStd_Array1OfReal) -> None: ...
	def Value2d(self, U: float) -> gp_Pnt2d: ...

class BRepGProp_Gauss:
	def __init__(self, theType: BRepGProp_GaussType) -> None: ...

class BRepGProp_MeshCinert(GProp_GProps):
	def __init__(self) -> None: ...
	def Perform(self, theNodes: TColgp_Array1OfPnt) -> None: ...
	@staticmethod
	def PreparePolygon(self, theE: TopoDS_Edge, thePolyg: TColgp_HArray1OfPnt) -> None: ...
	def SetLocation(self, CLocation: gp_Pnt) -> None: ...

class BRepGProp_Sinert(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, SLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, SLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, SLocation: gp_Pnt, Eps: float) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, SLocation: gp_Pnt, Eps: float) -> None: ...
	def GetEpsilon(self) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, Eps: float) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Eps: float) -> float: ...
	def SetLocation(self, SLocation: gp_Pnt) -> None: ...

class BRepGProp_TFunction(math_Function):
	def __init__(self, theSurface: BRepGProp_Face, theVertex: gp_Pnt, IsByPoint: bool, theCoeffs: None, theUMin: float, theTolerance: float) -> None: ...
	def AbsolutError(self) -> float: ...
	def ErrorReached(self) -> float: ...
	def GetStateNumber(self) -> int: ...
	def Init(self) -> None: ...
	def SetNbKronrodPoints(self, theNbPoints: int) -> None: ...
	def SetTolerance(self, aTol: float) -> None: ...
	def SetValueType(self, aType: GProp_ValueType) -> None: ...
	def Value(self, X: float) -> Tuple[bool, float]: ...

class BRepGProp_UFunction(math_Function):
	def __init__(self, theSurface: BRepGProp_Face, theVertex: gp_Pnt, IsByPoint: bool, theCoeffs: None) -> None: ...
	def SetVParam(self, theVParam: float) -> None: ...
	def SetValueType(self, theType: GProp_ValueType) -> None: ...
	def Value(self, X: float) -> Tuple[bool, float]: ...

class BRepGProp_Vinert(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, VLocation: gp_Pnt, Eps: float) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, O: gp_Pnt, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, O: gp_Pnt, VLocation: gp_Pnt, Eps: float) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, Pl: gp_Pln, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, Pl: gp_Pln, VLocation: gp_Pnt, Eps: float) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, VLocation: gp_Pnt, Eps: float) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: gp_Pnt, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: gp_Pnt, VLocation: gp_Pnt, Eps: float) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: gp_Pln, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: gp_Pln, VLocation: gp_Pnt, Eps: float) -> None: ...
	def GetEpsilon(self) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, Eps: float) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face, O: gp_Pnt) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, O: gp_Pnt, Eps: float) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face, Pl: gp_Pln) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, Pl: gp_Pln, Eps: float) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Eps: float) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: gp_Pnt) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, O: gp_Pnt, Eps: float) -> float: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: gp_Pln) -> None: ...
	@overload
	def Perform(self, S: BRepGProp_Face, D: BRepGProp_Domain, Pl: gp_Pln, Eps: float) -> float: ...
	def SetLocation(self, VLocation: gp_Pnt) -> None: ...

class BRepGProp_VinertGK(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theSurface: BRepGProp_Face, theLocation: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theSurface: BRepGProp_Face, thePoint: gp_Pnt, theLocation: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, theLocation: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePoint: gp_Pnt, theLocation: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theSurface: BRepGProp_Face, thePlane: gp_Pln, theLocation: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePlane: gp_Pln, theLocation: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> None: ...
	def GetErrorReached(self) -> float: ...
	@overload
	def Perform(self, theSurface: BRepGProp_Face, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> float: ...
	@overload
	def Perform(self, theSurface: BRepGProp_Face, thePoint: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> float: ...
	@overload
	def Perform(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> float: ...
	@overload
	def Perform(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePoint: gp_Pnt, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> float: ...
	@overload
	def Perform(self, theSurface: BRepGProp_Face, thePlane: gp_Pln, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> float: ...
	@overload
	def Perform(self, theSurface: BRepGProp_Face, theDomain: BRepGProp_Domain, thePlane: gp_Pln, theTolerance: Optional[float], theCGFlag: Optional[bool], theIFlag: Optional[bool]) -> float: ...
	def SetLocation(self, theLocation: gp_Pnt) -> None: ...

#classnotwrapped
class BRepGProp_MeshProps: ...

# harray1 classes
# harray2 classes
# hsequence classes

brepgprop_LinearProperties = brepgprop.LinearProperties
brepgprop_SurfaceProperties = brepgprop.SurfaceProperties
brepgprop_SurfaceProperties = brepgprop.SurfaceProperties
brepgprop_VolumeProperties = brepgprop.VolumeProperties
brepgprop_VolumeProperties = brepgprop.VolumeProperties
brepgprop_VolumePropertiesGK = brepgprop.VolumePropertiesGK
brepgprop_VolumePropertiesGK = brepgprop.VolumePropertiesGK
BRepGProp_EdgeTool_D1 = BRepGProp_EdgeTool.D1
BRepGProp_EdgeTool_FirstParameter = BRepGProp_EdgeTool.FirstParameter
BRepGProp_EdgeTool_IntegrationOrder = BRepGProp_EdgeTool.IntegrationOrder
BRepGProp_EdgeTool_Intervals = BRepGProp_EdgeTool.Intervals
BRepGProp_EdgeTool_LastParameter = BRepGProp_EdgeTool.LastParameter
BRepGProp_EdgeTool_NbIntervals = BRepGProp_EdgeTool.NbIntervals
BRepGProp_EdgeTool_Value = BRepGProp_EdgeTool.Value
BRepGProp_MeshCinert_PreparePolygon = BRepGProp_MeshCinert.PreparePolygon
