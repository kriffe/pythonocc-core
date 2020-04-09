from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.math import *
from OCC.Core.gp import *
from OCC.Core.IntSurf import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Adaptor2d import *
from OCC.Core.GeomAbs import *
from OCC.Core.Geom2d import *
from OCC.Core.TColStd import *

#the following typedef cannot be wrapped as is
Contap_SequenceOfIWLineOfTheIWalking = NewType('Contap_SequenceOfIWLineOfTheIWalking', Any)
#the following typedef cannot be wrapped as is
Contap_SequenceOfPathPointOfTheSearch = NewType('Contap_SequenceOfPathPointOfTheSearch', Any)
#the following typedef cannot be wrapped as is
Contap_SequenceOfSegmentOfTheSearch = NewType('Contap_SequenceOfSegmentOfTheSearch', Any)
#the following typedef cannot be wrapped as is
Contap_TheSequenceOfLine = NewType('Contap_TheSequenceOfLine', Any)
#the following typedef cannot be wrapped as is
Contap_TheSequenceOfPoint = NewType('Contap_TheSequenceOfPoint', Any)

class Contap_IType(IntEnum):
	Contap_Lin: int = ...
	Contap_Circle: int = ...
	Contap_Walking: int = ...
	Contap_Restriction: int = ...
Contap_Lin = Contap_IType.Contap_Lin
Contap_Circle = Contap_IType.Contap_Circle
Contap_Walking = Contap_IType.Contap_Walking
Contap_Restriction = Contap_IType.Contap_Restriction

class Contap_TFunction(IntEnum):
	Contap_ContourStd: int = ...
	Contap_ContourPrs: int = ...
	Contap_DraftStd: int = ...
	Contap_DraftPrs: int = ...
Contap_ContourStd = Contap_TFunction.Contap_ContourStd
Contap_ContourPrs = Contap_TFunction.Contap_ContourPrs
Contap_DraftStd = Contap_TFunction.Contap_DraftStd
Contap_DraftPrs = Contap_TFunction.Contap_DraftPrs

class Contap_ArcFunction(math_FunctionWithDerivative):
	def __init__(self) -> None: ...
	def Derivative(self, X: float) -> Tuple[bool, float]: ...
	def GetStateNumber(self) -> int: ...
	def LastComputedPoint(self) -> gp_Pnt: ...
	def NbSamples(self) -> int: ...
	def Quadric(self) -> IntSurf_Quadric: ...
	@overload
	def Set(self, S: Adaptor3d_HSurface) -> None: ...
	@overload
	def Set(self, Direction: gp_Dir) -> None: ...
	@overload
	def Set(self, Direction: gp_Dir, Angle: float) -> None: ...
	@overload
	def Set(self, Eye: gp_Pnt) -> None: ...
	@overload
	def Set(self, Eye: gp_Pnt, Angle: float) -> None: ...
	@overload
	def Set(self, A: Adaptor2d_HCurve2d) -> None: ...
	def Surface(self) -> Adaptor3d_HSurface: ...
	def Valpoint(self, Index: int) -> gp_Pnt: ...
	def Value(self, X: float) -> Tuple[bool, float]: ...
	def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Contap_ContAna:
	def __init__(self) -> None: ...
	def Circle(self) -> gp_Circ: ...
	def IsDone(self) -> bool: ...
	def Line(self, Index: int) -> gp_Lin: ...
	def NbContours(self) -> int: ...
	@overload
	def Perform(self, S: gp_Sphere, D: gp_Dir) -> None: ...
	@overload
	def Perform(self, S: gp_Sphere, D: gp_Dir, Ang: float) -> None: ...
	@overload
	def Perform(self, S: gp_Sphere, Eye: gp_Pnt) -> None: ...
	@overload
	def Perform(self, C: gp_Cylinder, D: gp_Dir) -> None: ...
	@overload
	def Perform(self, C: gp_Cylinder, D: gp_Dir, Ang: float) -> None: ...
	@overload
	def Perform(self, C: gp_Cylinder, Eye: gp_Pnt) -> None: ...
	@overload
	def Perform(self, C: gp_Cone, D: gp_Dir) -> None: ...
	@overload
	def Perform(self, C: gp_Cone, D: gp_Dir, Ang: float) -> None: ...
	@overload
	def Perform(self, C: gp_Cone, Eye: gp_Pnt) -> None: ...
	def TypeContour(self) -> GeomAbs_CurveType: ...

class Contap_Contour:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Direction: gp_Vec) -> None: ...
	@overload
	def __init__(self, Direction: gp_Vec, Angle: float) -> None: ...
	@overload
	def __init__(self, Eye: gp_Pnt) -> None: ...
	@overload
	def __init__(self, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool, Direction: gp_Vec) -> None: ...
	@overload
	def __init__(self, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool, Direction: gp_Vec, Angle: float) -> None: ...
	@overload
	def __init__(self, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool, Eye: gp_Pnt) -> None: ...
	@overload
	def Init(self, Direction: gp_Vec) -> None: ...
	@overload
	def Init(self, Direction: gp_Vec, Angle: float) -> None: ...
	@overload
	def Init(self, Eye: gp_Pnt) -> None: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def Line(self, Index: int) -> Contap_Line: ...
	def NbLines(self) -> int: ...
	@overload
	def Perform(self, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool) -> None: ...
	@overload
	def Perform(self, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool, Direction: gp_Vec) -> None: ...
	@overload
	def Perform(self, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool, Direction: gp_Vec, Angle: float) -> None: ...
	@overload
	def Perform(self, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool, Eye: gp_Pnt) -> None: ...
	def SurfaceFunction(self) -> Contap_SurfFunction: ...

class Contap_HContTool:
	@staticmethod
	def Bounds(self, C: Adaptor2d_HCurve2d) -> Tuple[float, float]: ...
	@staticmethod
	def HasBeenSeen(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def HasFirstPoint(self, C: Adaptor2d_HCurve2d, Index: int) -> Tuple[bool, int]: ...
	@staticmethod
	def HasLastPoint(self, C: Adaptor2d_HCurve2d, Index: int) -> Tuple[bool, int]: ...
	@staticmethod
	def IsAllSolution(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def IsVertex(self, C: Adaptor2d_HCurve2d, Index: int) -> bool: ...
	@staticmethod
	def NbPoints(self, C: Adaptor2d_HCurve2d) -> int: ...
	@staticmethod
	def NbSamplePoints(self, S: Adaptor3d_HSurface) -> int: ...
	@staticmethod
	def NbSamplesOnArc(self, A: Adaptor2d_HCurve2d) -> int: ...
	@staticmethod
	def NbSamplesU(self, S: Adaptor3d_HSurface, u1: float, u2: float) -> int: ...
	@staticmethod
	def NbSamplesV(self, S: Adaptor3d_HSurface, v1: float, v2: float) -> int: ...
	@staticmethod
	def NbSegments(self, C: Adaptor2d_HCurve2d) -> int: ...
	@staticmethod
	def Parameter(self, V: Adaptor3d_HVertex, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Project(self, C: Adaptor2d_HCurve2d, P: gp_Pnt2d, Ptproj: gp_Pnt2d) -> Tuple[bool, float]: ...
	@staticmethod
	def SamplePoint(self, S: Adaptor3d_HSurface, Index: int) -> Tuple[float, float]: ...
	@staticmethod
	def Tolerance(self, V: Adaptor3d_HVertex, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Value(self, C: Adaptor2d_HCurve2d, Index: int, Pt: gp_Pnt) -> Tuple[float, float]: ...
	@staticmethod
	def Vertex(self, C: Adaptor2d_HCurve2d, Index: int, V: Adaptor3d_HVertex) -> None: ...

class Contap_HCurve2dTool:
	@staticmethod
	def BSpline(self, C: Adaptor2d_HCurve2d) -> Geom2d_BSplineCurve: ...
	@staticmethod
	def Bezier(self, C: Adaptor2d_HCurve2d) -> Geom2d_BezierCurve: ...
	@staticmethod
	def Circle(self, C: Adaptor2d_HCurve2d) -> gp_Circ2d: ...
	@staticmethod
	def Continuity(self, C: Adaptor2d_HCurve2d) -> GeomAbs_Shape: ...
	@staticmethod
	def D0(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d) -> None: ...
	@staticmethod
	def D1(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	@staticmethod
	def D2(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	@staticmethod
	def D3(self, C: Adaptor2d_HCurve2d, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	@staticmethod
	def DN(self, C: Adaptor2d_HCurve2d, U: float, N: int) -> gp_Vec2d: ...
	@staticmethod
	def Ellipse(self, C: Adaptor2d_HCurve2d) -> gp_Elips2d: ...
	@staticmethod
	def FirstParameter(self, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def GetType(self, C: Adaptor2d_HCurve2d) -> GeomAbs_CurveType: ...
	@staticmethod
	def Hyperbola(self, C: Adaptor2d_HCurve2d) -> gp_Hypr2d: ...
	@staticmethod
	def Intervals(self, C: Adaptor2d_HCurve2d, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	@staticmethod
	def IsClosed(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def IsPeriodic(self, C: Adaptor2d_HCurve2d) -> bool: ...
	@staticmethod
	def LastParameter(self, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Line(self, C: Adaptor2d_HCurve2d) -> gp_Lin2d: ...
	@staticmethod
	def NbIntervals(self, C: Adaptor2d_HCurve2d, S: GeomAbs_Shape) -> int: ...
	@staticmethod
	def NbSamples(self, C: Adaptor2d_HCurve2d, U0: float, U1: float) -> int: ...
	@staticmethod
	def Parabola(self, C: Adaptor2d_HCurve2d) -> gp_Parab2d: ...
	@staticmethod
	def Period(self, C: Adaptor2d_HCurve2d) -> float: ...
	@staticmethod
	def Resolution(self, C: Adaptor2d_HCurve2d, R3d: float) -> float: ...
	@staticmethod
	def Value(self, C: Adaptor2d_HCurve2d, U: float) -> gp_Pnt2d: ...

class Contap_Line:
	def __init__(self) -> None: ...
	@overload
	def Add(self, P: IntSurf_PntOn2S) -> None: ...
	@overload
	def Add(self, P: Contap_Point) -> None: ...
	def Arc(self) -> Adaptor2d_HCurve2d: ...
	def Circle(self) -> gp_Circ: ...
	def Clear(self) -> None: ...
	def Line(self) -> gp_Lin: ...
	def LineOn2S(self) -> IntSurf_LineOn2S: ...
	def NbPnts(self) -> int: ...
	def NbVertex(self) -> int: ...
	def Point(self, Index: int) -> IntSurf_PntOn2S: ...
	def ResetSeqOfVertex(self) -> None: ...
	def SetLineOn2S(self, L: IntSurf_LineOn2S) -> None: ...
	def SetTransitionOnS(self, T: IntSurf_TypeTrans) -> None: ...
	@overload
	def SetValue(self, L: gp_Lin) -> None: ...
	@overload
	def SetValue(self, C: gp_Circ) -> None: ...
	@overload
	def SetValue(self, A: Adaptor2d_HCurve2d) -> None: ...
	def TransitionOnS(self) -> IntSurf_TypeTrans: ...
	def TypeContour(self) -> Contap_IType: ...
	def Vertex(self, Index: int) -> Contap_Point: ...

class Contap_Point:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Pt: gp_Pnt, U: float, V: float) -> None: ...
	def Arc(self) -> Adaptor2d_HCurve2d: ...
	def IsInternal(self) -> bool: ...
	def IsMultiple(self) -> bool: ...
	def IsOnArc(self) -> bool: ...
	def IsVertex(self) -> bool: ...
	def ParameterOnArc(self) -> float: ...
	def ParameterOnLine(self) -> float: ...
	def Parameters(self) -> Tuple[float, float]: ...
	def SetArc(self, A: Adaptor2d_HCurve2d, Param: float, TLine: IntSurf_Transition, TArc: IntSurf_Transition) -> None: ...
	def SetInternal(self) -> None: ...
	def SetMultiple(self) -> None: ...
	def SetParameter(self, Para: float) -> None: ...
	def SetValue(self, Pt: gp_Pnt, U: float, V: float) -> None: ...
	def SetVertex(self, V: Adaptor3d_HVertex) -> None: ...
	def TransitionOnArc(self) -> IntSurf_Transition: ...
	def TransitionOnLine(self) -> IntSurf_Transition: ...
	def Value(self) -> gp_Pnt: ...
	def Vertex(self) -> Adaptor3d_HVertex: ...

class Contap_SurfFunction(math_FunctionSetWithDerivatives):
	def __init__(self) -> None: ...
	def Angle(self) -> float: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def Direction(self) -> gp_Dir: ...
	def Direction2d(self) -> gp_Dir2d: ...
	def Direction3d(self) -> gp_Vec: ...
	def Eye(self) -> gp_Pnt: ...
	def FunctionType(self) -> Contap_TFunction: ...
	def IsTangent(self) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def PSurface(self) -> Adaptor3d_HSurface: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	@overload
	def Set(self, S: Adaptor3d_HSurface) -> None: ...
	@overload
	def Set(self, Eye: gp_Pnt) -> None: ...
	@overload
	def Set(self, Dir: gp_Dir) -> None: ...
	@overload
	def Set(self, Dir: gp_Dir, Angle: float) -> None: ...
	@overload
	def Set(self, Eye: gp_Pnt, Angle: float) -> None: ...
	@overload
	def Set(self, Tolerance: float) -> None: ...
	def Surface(self) -> Adaptor3d_HSurface: ...
	def Tolerance(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Contap_SurfProps:
	@staticmethod
	def DerivAndNorm(self, S: Adaptor3d_HSurface, U: float, V: float, P: gp_Pnt, d1u: gp_Vec, d1v: gp_Vec, N: gp_Vec) -> None: ...
	@staticmethod
	def NormAndDn(self, S: Adaptor3d_HSurface, U: float, V: float, P: gp_Pnt, N: gp_Vec, Dnu: gp_Vec, Dnv: gp_Vec) -> None: ...
	@staticmethod
	def Normale(self, S: Adaptor3d_HSurface, U: float, V: float, P: gp_Pnt, N: gp_Vec) -> None: ...

class Contap_TheIWLineOfTheIWalking(Standard_Transient):
	def __init__(self, theAllocator: Optional[IntSurf_Allocator]) -> None: ...
	def AddIndexPassing(self, Index: int) -> None: ...
	def AddPoint(self, P: IntSurf_PntOn2S) -> None: ...
	@overload
	def AddStatusFirst(self, Closed: bool, HasFirst: bool) -> None: ...
	@overload
	def AddStatusFirst(self, Closed: bool, HasLast: bool, Index: int, P: IntSurf_PathPoint) -> None: ...
	def AddStatusFirstLast(self, Closed: bool, HasFirst: bool, HasLast: bool) -> None: ...
	@overload
	def AddStatusLast(self, HasLast: bool) -> None: ...
	@overload
	def AddStatusLast(self, HasLast: bool, Index: int, P: IntSurf_PathPoint) -> None: ...
	def Cut(self, Index: int) -> None: ...
	def FirstPoint(self) -> IntSurf_PathPoint: ...
	def FirstPointIndex(self) -> int: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def IsClosed(self) -> bool: ...
	def IsTangentAtBegining(self) -> bool: ...
	def IsTangentAtEnd(self) -> bool: ...
	def LastPoint(self) -> IntSurf_PathPoint: ...
	def LastPointIndex(self) -> int: ...
	def Line(self) -> IntSurf_LineOn2S: ...
	def NbPassingPoint(self) -> int: ...
	def NbPoints(self) -> int: ...
	def PassingPoint(self, Index: int) -> Tuple[int, int]: ...
	def Reverse(self) -> None: ...
	def SetTangencyAtBegining(self, IsTangent: bool) -> None: ...
	def SetTangencyAtEnd(self, IsTangent: bool) -> None: ...
	def SetTangentVector(self, V: gp_Vec, Index: int) -> None: ...
	def TangentVector(self) -> Tuple[gp_Vec, int]: ...
	def Value(self, Index: int) -> IntSurf_PntOn2S: ...

class Contap_TheIWalking:
	def __init__(self, Epsilon: float, Deflection: float, Step: float, theToFillHoles: Optional[bool]) -> None: ...
	def IsDone(self) -> bool: ...
	def NbLines(self) -> int: ...
	def NbSinglePnts(self) -> int: ...
	@overload
	def Perform(self, Pnts1: IntSurf_SequenceOfPathPoint, Pnts2: IntSurf_SequenceOfInteriorPoint, Func: Contap_SurfFunction, S: Adaptor3d_HSurface, Reversed: Optional[bool]) -> None: ...
	@overload
	def Perform(self, Pnts1: IntSurf_SequenceOfPathPoint, Func: Contap_SurfFunction, S: Adaptor3d_HSurface, Reversed: Optional[bool]) -> None: ...
	def SetTolerance(self, Epsilon: float, Deflection: float, Step: float) -> None: ...
	def SinglePnt(self, Index: int) -> IntSurf_PathPoint: ...
	def Value(self, Index: int) -> Contap_TheIWLineOfTheIWalking: ...

class Contap_ThePathPointOfTheSearch:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P: gp_Pnt, Tol: float, V: Adaptor3d_HVertex, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	@overload
	def __init__(self, P: gp_Pnt, Tol: float, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	def Arc(self) -> Adaptor2d_HCurve2d: ...
	def IsNew(self) -> bool: ...
	def Parameter(self) -> float: ...
	@overload
	def SetValue(self, P: gp_Pnt, Tol: float, V: Adaptor3d_HVertex, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	@overload
	def SetValue(self, P: gp_Pnt, Tol: float, A: Adaptor2d_HCurve2d, Parameter: float) -> None: ...
	def Tolerance(self) -> float: ...
	def Value(self) -> gp_Pnt: ...
	def Vertex(self) -> Adaptor3d_HVertex: ...

class Contap_TheSearch:
	def __init__(self) -> None: ...
	def AllArcSolution(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def NbSegments(self) -> int: ...
	def Perform(self, F: Contap_ArcFunction, Domain: Adaptor3d_TopolTool, TolBoundary: float, TolTangency: float, RecheckOnRegularity: Optional[bool]) -> None: ...
	def Point(self, Index: int) -> Contap_ThePathPointOfTheSearch: ...
	def Segment(self, Index: int) -> Contap_TheSegmentOfTheSearch: ...

class Contap_TheSearchInside:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: Contap_SurfFunction, Surf: Adaptor3d_HSurface, T: Adaptor3d_TopolTool, Epsilon: float) -> None: ...
	def IsDone(self) -> bool: ...
	def NbPoints(self) -> int: ...
	@overload
	def Perform(self, F: Contap_SurfFunction, Surf: Adaptor3d_HSurface, T: Adaptor3d_TopolTool, Epsilon: float) -> None: ...
	@overload
	def Perform(self, F: Contap_SurfFunction, Surf: Adaptor3d_HSurface, UStart: float, VStart: float) -> None: ...
	def Value(self, Index: int) -> IntSurf_InteriorPoint: ...

class Contap_TheSegmentOfTheSearch:
	def __init__(self) -> None: ...
	def Curve(self) -> Adaptor2d_HCurve2d: ...
	def FirstPoint(self) -> Contap_ThePathPointOfTheSearch: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def LastPoint(self) -> Contap_ThePathPointOfTheSearch: ...
	def SetLimitPoint(self, V: Contap_ThePathPointOfTheSearch, First: bool) -> None: ...
	def SetValue(self, A: Adaptor2d_HCurve2d) -> None: ...

# harray1 classes
# harray2 classes
# harray2 classes

class Contap_TheHSequenceOfPoint(Contap_TheSequenceOfPoint, Standard_Transient): ...


Contap_HContTool_Bounds = Contap_HContTool.Bounds
Contap_HContTool_HasBeenSeen = Contap_HContTool.HasBeenSeen
Contap_HContTool_HasFirstPoint = Contap_HContTool.HasFirstPoint
Contap_HContTool_HasLastPoint = Contap_HContTool.HasLastPoint
Contap_HContTool_IsAllSolution = Contap_HContTool.IsAllSolution
Contap_HContTool_IsVertex = Contap_HContTool.IsVertex
Contap_HContTool_NbPoints = Contap_HContTool.NbPoints
Contap_HContTool_NbSamplePoints = Contap_HContTool.NbSamplePoints
Contap_HContTool_NbSamplesOnArc = Contap_HContTool.NbSamplesOnArc
Contap_HContTool_NbSamplesU = Contap_HContTool.NbSamplesU
Contap_HContTool_NbSamplesV = Contap_HContTool.NbSamplesV
Contap_HContTool_NbSegments = Contap_HContTool.NbSegments
Contap_HContTool_Parameter = Contap_HContTool.Parameter
Contap_HContTool_Project = Contap_HContTool.Project
Contap_HContTool_SamplePoint = Contap_HContTool.SamplePoint
Contap_HContTool_Tolerance = Contap_HContTool.Tolerance
Contap_HContTool_Value = Contap_HContTool.Value
Contap_HContTool_Vertex = Contap_HContTool.Vertex
Contap_HCurve2dTool_BSpline = Contap_HCurve2dTool.BSpline
Contap_HCurve2dTool_Bezier = Contap_HCurve2dTool.Bezier
Contap_HCurve2dTool_Circle = Contap_HCurve2dTool.Circle
Contap_HCurve2dTool_Continuity = Contap_HCurve2dTool.Continuity
Contap_HCurve2dTool_D0 = Contap_HCurve2dTool.D0
Contap_HCurve2dTool_D1 = Contap_HCurve2dTool.D1
Contap_HCurve2dTool_D2 = Contap_HCurve2dTool.D2
Contap_HCurve2dTool_D3 = Contap_HCurve2dTool.D3
Contap_HCurve2dTool_DN = Contap_HCurve2dTool.DN
Contap_HCurve2dTool_Ellipse = Contap_HCurve2dTool.Ellipse
Contap_HCurve2dTool_FirstParameter = Contap_HCurve2dTool.FirstParameter
Contap_HCurve2dTool_GetType = Contap_HCurve2dTool.GetType
Contap_HCurve2dTool_Hyperbola = Contap_HCurve2dTool.Hyperbola
Contap_HCurve2dTool_Intervals = Contap_HCurve2dTool.Intervals
Contap_HCurve2dTool_IsClosed = Contap_HCurve2dTool.IsClosed
Contap_HCurve2dTool_IsPeriodic = Contap_HCurve2dTool.IsPeriodic
Contap_HCurve2dTool_LastParameter = Contap_HCurve2dTool.LastParameter
Contap_HCurve2dTool_Line = Contap_HCurve2dTool.Line
Contap_HCurve2dTool_NbIntervals = Contap_HCurve2dTool.NbIntervals
Contap_HCurve2dTool_NbSamples = Contap_HCurve2dTool.NbSamples
Contap_HCurve2dTool_Parabola = Contap_HCurve2dTool.Parabola
Contap_HCurve2dTool_Period = Contap_HCurve2dTool.Period
Contap_HCurve2dTool_Resolution = Contap_HCurve2dTool.Resolution
Contap_HCurve2dTool_Value = Contap_HCurve2dTool.Value
Contap_SurfProps_DerivAndNorm = Contap_SurfProps.DerivAndNorm
Contap_SurfProps_NormAndDn = Contap_SurfProps.NormAndDn
Contap_SurfProps_Normale = Contap_SurfProps.Normale
