from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Geom import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.Geom2d import *
from OCC.Core.TopTools import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.Law import *

#the following typedef cannot be wrapped as is
ChFiDS_IndexedDataMapOfVertexListOfStripe = NewType('ChFiDS_IndexedDataMapOfVertexListOfStripe', Any)
#the following typedef cannot be wrapped as is
ChFiDS_ListIteratorOfListOfHElSpine = NewType('ChFiDS_ListIteratorOfListOfHElSpine', Any)
#the following typedef cannot be wrapped as is
ChFiDS_ListIteratorOfListOfStripe = NewType('ChFiDS_ListIteratorOfListOfStripe', Any)
#the following typedef cannot be wrapped as is
ChFiDS_ListIteratorOfRegularities = NewType('ChFiDS_ListIteratorOfRegularities', Any)
#the following typedef cannot be wrapped as is
ChFiDS_ListOfHElSpine = NewType('ChFiDS_ListOfHElSpine', Any)
#the following typedef cannot be wrapped as is
ChFiDS_ListOfStripe = NewType('ChFiDS_ListOfStripe', Any)
#the following typedef cannot be wrapped as is
ChFiDS_Regularities = NewType('ChFiDS_Regularities', Any)
#the following typedef cannot be wrapped as is
ChFiDS_SequenceOfSpine = NewType('ChFiDS_SequenceOfSpine', Any)
#the following typedef cannot be wrapped as is
ChFiDS_SequenceOfSurfData = NewType('ChFiDS_SequenceOfSurfData', Any)

class ChFiDS_SecArray1:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> ChFiDS_CircSection: ...
    def __setitem__(self, index: int, value: ChFiDS_CircSection) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[ChFiDS_CircSection]:
    def next(self) -> ChFiDS_CircSection: ...
    __next__ = next

class ChFiDS_StripeArray1:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]:
    def next(self) -> False: ...
    __next__ = next

class ChFiDS_State(IntEnum):
	ChFiDS_OnSame: int = ...
	ChFiDS_OnDiff: int = ...
	ChFiDS_AllSame: int = ...
	ChFiDS_BreakPoint: int = ...
	ChFiDS_FreeBoundary: int = ...
	ChFiDS_Closed: int = ...
	ChFiDS_Tangent: int = ...
ChFiDS_OnSame = ChFiDS_State.ChFiDS_OnSame
ChFiDS_OnDiff = ChFiDS_State.ChFiDS_OnDiff
ChFiDS_AllSame = ChFiDS_State.ChFiDS_AllSame
ChFiDS_BreakPoint = ChFiDS_State.ChFiDS_BreakPoint
ChFiDS_FreeBoundary = ChFiDS_State.ChFiDS_FreeBoundary
ChFiDS_Closed = ChFiDS_State.ChFiDS_Closed
ChFiDS_Tangent = ChFiDS_State.ChFiDS_Tangent

class ChFiDS_ChamfMethod(IntEnum):
	ChFiDS_Sym: int = ...
	ChFiDS_TwoDist: int = ...
	ChFiDS_DistAngle: int = ...
ChFiDS_Sym = ChFiDS_ChamfMethod.ChFiDS_Sym
ChFiDS_TwoDist = ChFiDS_ChamfMethod.ChFiDS_TwoDist
ChFiDS_DistAngle = ChFiDS_ChamfMethod.ChFiDS_DistAngle

class ChFiDS_ChamfMode(IntEnum):
	ChFiDS_ClassicChamfer: int = ...
	ChFiDS_ConstThroatChamfer: int = ...
	ChFiDS_ConstThroatWithPenetrationChamfer: int = ...
ChFiDS_ClassicChamfer = ChFiDS_ChamfMode.ChFiDS_ClassicChamfer
ChFiDS_ConstThroatChamfer = ChFiDS_ChamfMode.ChFiDS_ConstThroatChamfer
ChFiDS_ConstThroatWithPenetrationChamfer = ChFiDS_ChamfMode.ChFiDS_ConstThroatWithPenetrationChamfer

class ChFiDS_ErrorStatus(IntEnum):
	ChFiDS_Ok: int = ...
	ChFiDS_Error: int = ...
	ChFiDS_WalkingFailure: int = ...
	ChFiDS_StartsolFailure: int = ...
	ChFiDS_TwistedSurface: int = ...
ChFiDS_Ok = ChFiDS_ErrorStatus.ChFiDS_Ok
ChFiDS_Error = ChFiDS_ErrorStatus.ChFiDS_Error
ChFiDS_WalkingFailure = ChFiDS_ErrorStatus.ChFiDS_WalkingFailure
ChFiDS_StartsolFailure = ChFiDS_ErrorStatus.ChFiDS_StartsolFailure
ChFiDS_TwistedSurface = ChFiDS_ErrorStatus.ChFiDS_TwistedSurface

class ChFiDS_CircSection:
	def __init__(self) -> None: ...
	@overload
	def Get(self, C: gp_Circ) -> Tuple[float, float]: ...
	@overload
	def Get(self, C: gp_Lin) -> Tuple[float, float]: ...
	@overload
	def Set(self, C: gp_Circ, F: float, L: float) -> None: ...
	@overload
	def Set(self, C: gp_Lin, F: float, L: float) -> None: ...

class ChFiDS_CommonPoint:
	def __init__(self) -> None: ...
	def Arc(self) -> TopoDS_Edge: ...
	def HasVector(self) -> bool: ...
	def IsOnArc(self) -> bool: ...
	def IsVertex(self) -> bool: ...
	def Parameter(self) -> float: ...
	def ParameterOnArc(self) -> float: ...
	def Point(self) -> gp_Pnt: ...
	def Reset(self) -> None: ...
	def SetArc(self, Tol: float, A: TopoDS_Edge, Param: float, TArc: TopAbs_Orientation) -> None: ...
	def SetParameter(self, Param: float) -> None: ...
	def SetPoint(self, thePoint: gp_Pnt) -> None: ...
	def SetTolerance(self, Tol: float) -> None: ...
	def SetVector(self, theVector: gp_Vec) -> None: ...
	def SetVertex(self, theVertex: TopoDS_Vertex) -> None: ...
	def Tolerance(self) -> float: ...
	def TransitionOnArc(self) -> TopAbs_Orientation: ...
	def Vector(self) -> gp_Vec: ...
	def Vertex(self) -> TopoDS_Vertex: ...

class ChFiDS_ElSpine(Adaptor3d_Curve):
	def __init__(self) -> None: ...
	def AddVertexWithTangent(self, anAx1: gp_Ax1) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def Bezier(self) -> Geom_BezierCurve: ...
	def ChangeNext(self) -> ChFiDS_SurfData: ...
	def ChangePrevious(self) -> ChFiDS_SurfData: ...
	def Circle(self) -> gp_Circ: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, AbsC: float, P: gp_Pnt) -> None: ...
	def D1(self, AbsC: float, P: gp_Pnt, V1: gp_Vec) -> None: ...
	def D2(self, AbsC: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def D3(self, AbsC: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def Ellipse(self) -> gp_Elips: ...
	@overload
	def FirstParameter(self) -> float: ...
	@overload
	def FirstParameter(self, P: float) -> None: ...
	def FirstPointAndTgt(self, P: gp_Pnt, T: gp_Vec) -> None: ...
	def GetSavedFirstParameter(self) -> float: ...
	def GetSavedLastParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsPeriodic(self) -> bool: ...
	@overload
	def LastParameter(self) -> float: ...
	@overload
	def LastParameter(self, P: float) -> None: ...
	def LastPointAndTgt(self, P: gp_Pnt, T: gp_Vec) -> None: ...
	def Line(self) -> gp_Lin: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVertices(self) -> int: ...
	def Next(self) -> ChFiDS_SurfData: ...
	def Parabola(self) -> gp_Parab: ...
	def Period(self) -> float: ...
	def Previous(self) -> ChFiDS_SurfData: ...
	def Resolution(self, R3d: float) -> float: ...
	def SaveFirstParameter(self) -> None: ...
	def SaveLastParameter(self) -> None: ...
	def SetCurve(self, C: Geom_Curve) -> None: ...
	def SetFirstPointAndTgt(self, P: gp_Pnt, T: gp_Vec) -> None: ...
	def SetLastPointAndTgt(self, P: gp_Pnt, T: gp_Vec) -> None: ...
	def SetOrigin(self, O: float) -> None: ...
	def SetPeriodic(self, I: bool) -> None: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
	def Value(self, AbsC: float) -> gp_Pnt: ...
	def VertexWithTangent(self, Index: int) -> gp_Ax1: ...

class ChFiDS_FaceInterference:
	def __init__(self) -> None: ...
	def ChangePCurveOnFace(self) -> Geom2d_Curve: ...
	def ChangePCurveOnSurf(self) -> Geom2d_Curve: ...
	def FirstParameter(self) -> float: ...
	def LastParameter(self) -> float: ...
	def LineIndex(self) -> int: ...
	def PCurveOnFace(self) -> Geom2d_Curve: ...
	def PCurveOnSurf(self) -> Geom2d_Curve: ...
	def Parameter(self, IsFirst: bool) -> float: ...
	def SetFirstParameter(self, U1: float) -> None: ...
	def SetInterference(self, LineIndex: int, Trans: TopAbs_Orientation, PCurv1: Geom2d_Curve, PCurv2: Geom2d_Curve) -> None: ...
	def SetLastParameter(self, U1: float) -> None: ...
	def SetLineIndex(self, I: int) -> None: ...
	def SetParameter(self, U1: float, IsFirst: bool) -> None: ...
	def SetTransition(self, Trans: TopAbs_Orientation) -> None: ...
	def Transition(self) -> TopAbs_Orientation: ...

class ChFiDS_HElSpine(Adaptor3d_HCurve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: ChFiDS_ElSpine) -> None: ...
	def ChangeCurve(self) -> ChFiDS_ElSpine: ...
	def Curve(self) -> Adaptor3d_Curve: ...
	def GetCurve(self) -> Adaptor3d_Curve: ...
	def Set(self, C: ChFiDS_ElSpine) -> None: ...

class ChFiDS_Map:
	def __init__(self) -> None: ...
	def Contains(self, S: TopoDS_Shape) -> bool: ...
	def Fill(self, S: TopoDS_Shape, T1: TopAbs_ShapeEnum, T2: TopAbs_ShapeEnum) -> None: ...
	def FindFromIndex(self, I: int) -> TopTools_ListOfShape: ...
	def FindFromKey(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...

class ChFiDS_Regul:
	def __init__(self) -> None: ...
	def Curve(self) -> int: ...
	def IsSurface1(self) -> bool: ...
	def IsSurface2(self) -> bool: ...
	def S1(self) -> int: ...
	def S2(self) -> int: ...
	def SetCurve(self, IC: int) -> None: ...
	def SetS1(self, IS1: int, IsFace: Optional[bool]) -> None: ...
	def SetS2(self, IS2: int, IsFace: Optional[bool]) -> None: ...

class ChFiDS_Spine(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Tol: float) -> None: ...
	@overload
	def Absc(self, U: float) -> float: ...
	@overload
	def Absc(self, U: float, I: int) -> float: ...
	@overload
	def Absc(self, V: TopoDS_Vertex) -> float: ...
	def AppendElSpine(self, Els: ChFiDS_HElSpine) -> None: ...
	def AppendOffsetElSpine(self, Els: ChFiDS_HElSpine) -> None: ...
	def ChangeElSpines(self) -> ChFiDS_ListOfHElSpine: ...
	def ChangeOffsetElSpines(self) -> ChFiDS_ListOfHElSpine: ...
	def Circle(self) -> gp_Circ: ...
	def CurrentElementarySpine(self, Index: int) -> BRepAdaptor_Curve: ...
	def CurrentIndexOfElementarySpine(self) -> int: ...
	def D0(self, AbsC: float, P: gp_Pnt) -> None: ...
	def D1(self, AbsC: float, P: gp_Pnt, V1: gp_Vec) -> None: ...
	def D2(self, AbsC: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def Edges(self, I: int) -> TopoDS_Edge: ...
	@overload
	def ElSpine(self, IE: int) -> ChFiDS_HElSpine: ...
	@overload
	def ElSpine(self, E: TopoDS_Edge) -> ChFiDS_HElSpine: ...
	@overload
	def ElSpine(self, W: float) -> ChFiDS_HElSpine: ...
	def ErrorStatus(self) -> ChFiDS_ErrorStatus: ...
	@overload
	def FirstParameter(self) -> float: ...
	@overload
	def FirstParameter(self, IndexSpine: int) -> float: ...
	def FirstStatus(self) -> ChFiDS_State: ...
	def FirstVertex(self) -> TopoDS_Vertex: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def HasFirstTgt(self) -> bool: ...
	def HasLastTgt(self) -> bool: ...
	@overload
	def Index(self, W: float, Forward: Optional[bool]) -> int: ...
	@overload
	def Index(self, E: TopoDS_Edge) -> int: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsTangencyExtremity(self, IsFirst: bool) -> bool: ...
	@overload
	def LastParameter(self) -> float: ...
	@overload
	def LastParameter(self, IndexSpine: int) -> float: ...
	def LastStatus(self) -> ChFiDS_State: ...
	def LastVertex(self) -> TopoDS_Vertex: ...
	def Length(self, IndexSpine: int) -> float: ...
	def Line(self) -> gp_Lin: ...
	def Load(self) -> None: ...
	def Mode(self) -> ChFiDS_ChamfMode: ...
	def NbEdges(self) -> int: ...
	def OffsetEdges(self, I: int) -> TopoDS_Edge: ...
	@overload
	def Parameter(self, AbsC: float, Oriented: Optional[bool]) -> float: ...
	@overload
	def Parameter(self, Index: int, AbsC: float, Oriented: Optional[bool]) -> float: ...
	def Period(self) -> float: ...
	def PutInFirst(self, E: TopoDS_Edge) -> None: ...
	def PutInFirstOffset(self, E: TopoDS_Edge) -> None: ...
	def Reset(self, AllData: Optional[bool]) -> None: ...
	def Resolution(self, R3d: float) -> float: ...
	def SetCurrent(self, Index: int) -> None: ...
	def SetEdges(self, E: TopoDS_Edge) -> None: ...
	def SetErrorStatus(self, state: ChFiDS_ErrorStatus) -> None: ...
	def SetFirstParameter(self, Par: float) -> None: ...
	def SetFirstStatus(self, S: ChFiDS_State) -> None: ...
	def SetFirstTgt(self, W: float) -> None: ...
	def SetLastParameter(self, Par: float) -> None: ...
	def SetLastStatus(self, S: ChFiDS_State) -> None: ...
	def SetLastTgt(self, W: float) -> None: ...
	def SetOffsetEdges(self, E: TopoDS_Edge) -> None: ...
	@overload
	def SetReference(self, W: float) -> None: ...
	@overload
	def SetReference(self, I: int) -> None: ...
	def SetStatus(self, S: ChFiDS_State, IsFirst: bool) -> None: ...
	def SetTangencyExtremity(self, IsTangency: bool, IsFirst: bool) -> None: ...
	@overload
	def SplitDone(self) -> bool: ...
	@overload
	def SplitDone(self, B: bool) -> None: ...
	def Status(self, IsFirst: bool) -> ChFiDS_State: ...
	def UnsetReference(self) -> None: ...
	def Value(self, AbsC: float) -> gp_Pnt: ...

class ChFiDS_Stripe(Standard_Transient):
	def __init__(self) -> None: ...
	def ChangeFirstCurve(self, Index: int) -> None: ...
	def ChangeFirstPCurve(self) -> Geom2d_Curve: ...
	def ChangeFirstParameters(self, Pdeb: float, Pfin: float) -> None: ...
	def ChangeIndexFirstPointOnS1(self, Index: int) -> None: ...
	def ChangeIndexFirstPointOnS2(self, Index: int) -> None: ...
	def ChangeIndexLastPointOnS1(self, Index: int) -> None: ...
	def ChangeIndexLastPointOnS2(self, Index: int) -> None: ...
	def ChangeLastCurve(self, Index: int) -> None: ...
	def ChangeLastPCurve(self) -> Geom2d_Curve: ...
	def ChangeLastParameters(self, Pdeb: float, Pfin: float) -> None: ...
	def ChangePCurve(self, First: bool) -> Geom2d_Curve: ...
	def ChangeSetOfSurfData(self) -> ChFiDS_HData: ...
	def ChangeSpine(self) -> ChFiDS_Spine: ...
	@overload
	def Choix(self) -> int: ...
	@overload
	def Choix(self, C: int) -> None: ...
	def Curve(self, First: bool) -> int: ...
	def FirstCurve(self) -> int: ...
	def FirstPCurve(self) -> Geom2d_Curve: ...
	@overload
	def FirstPCurveOrientation(self) -> TopAbs_Orientation: ...
	@overload
	def FirstPCurveOrientation(self, O: TopAbs_Orientation) -> None: ...
	def FirstParameters(self) -> Tuple[float, float]: ...
	def InDS(self, First: bool, Nb: Optional[int]) -> None: ...
	def IndexFirstPointOnS1(self) -> int: ...
	def IndexFirstPointOnS2(self) -> int: ...
	def IndexLastPointOnS1(self) -> int: ...
	def IndexLastPointOnS2(self) -> int: ...
	def IndexPoint(self, First: bool, OnS: int) -> int: ...
	def IsInDS(self, First: bool) -> int: ...
	def LastCurve(self) -> int: ...
	def LastPCurve(self) -> Geom2d_Curve: ...
	@overload
	def LastPCurveOrientation(self) -> TopAbs_Orientation: ...
	@overload
	def LastPCurveOrientation(self, O: TopAbs_Orientation) -> None: ...
	def LastParameters(self) -> Tuple[float, float]: ...
	@overload
	def Orientation(self, OnS: int) -> TopAbs_Orientation: ...
	@overload
	def Orientation(self, First: bool) -> TopAbs_Orientation: ...
	@overload
	def OrientationOnFace1(self) -> TopAbs_Orientation: ...
	@overload
	def OrientationOnFace1(self, Or1: TopAbs_Orientation) -> None: ...
	@overload
	def OrientationOnFace2(self) -> TopAbs_Orientation: ...
	@overload
	def OrientationOnFace2(self, Or2: TopAbs_Orientation) -> None: ...
	def PCurve(self, First: bool) -> Geom2d_Curve: ...
	def Parameters(self, First: bool) -> Tuple[float, float]: ...
	def Reset(self) -> None: ...
	def SetCurve(self, Index: int, First: bool) -> None: ...
	def SetIndexPoint(self, Index: int, First: bool, OnS: int) -> None: ...
	def SetOfSurfData(self) -> ChFiDS_HData: ...
	@overload
	def SetOrientation(self, Or: TopAbs_Orientation, OnS: int) -> None: ...
	@overload
	def SetOrientation(self, Or: TopAbs_Orientation, First: bool) -> None: ...
	def SetParameters(self, First: bool, Pdeb: float, Pfin: float) -> None: ...
	def SetSolidIndex(self, Index: int) -> None: ...
	def SolidIndex(self) -> int: ...
	def Spine(self) -> ChFiDS_Spine: ...

class ChFiDS_StripeMap:
	def __init__(self) -> None: ...
	def Add(self, V: TopoDS_Vertex, F: ChFiDS_Stripe) -> None: ...
	def Clear(self) -> None: ...
	def Extent(self) -> int: ...
	def FindFromIndex(self, I: int) -> ChFiDS_ListOfStripe: ...
	def FindFromKey(self, V: TopoDS_Vertex) -> ChFiDS_ListOfStripe: ...
	def FindKey(self, I: int) -> TopoDS_Vertex: ...

class ChFiDS_SurfData(Standard_Transient):
	def __init__(self) -> None: ...
	def ChangeIndexOfS1(self, Index: int) -> None: ...
	def ChangeIndexOfS2(self, Index: int) -> None: ...
	def ChangeInterference(self, OnS: int) -> ChFiDS_FaceInterference: ...
	def ChangeInterferenceOnS1(self) -> ChFiDS_FaceInterference: ...
	def ChangeInterferenceOnS2(self) -> ChFiDS_FaceInterference: ...
	def ChangeOrientation(self) -> TopAbs_Orientation: ...
	def ChangeSurf(self, Index: int) -> None: ...
	def ChangeVertex(self, First: bool, OnS: int) -> ChFiDS_CommonPoint: ...
	def ChangeVertexFirstOnS1(self) -> ChFiDS_CommonPoint: ...
	def ChangeVertexFirstOnS2(self) -> ChFiDS_CommonPoint: ...
	def ChangeVertexLastOnS1(self) -> ChFiDS_CommonPoint: ...
	def ChangeVertexLastOnS2(self) -> ChFiDS_CommonPoint: ...
	def Copy(self, Other: ChFiDS_SurfData) -> None: ...
	@overload
	def FirstExtensionValue(self) -> float: ...
	@overload
	def FirstExtensionValue(self, Extend: float) -> None: ...
	@overload
	def FirstSpineParam(self) -> float: ...
	@overload
	def FirstSpineParam(self, Par: float) -> None: ...
	@overload
	def Get2dPoints(self, First: bool, OnS: int) -> gp_Pnt2d: ...
	@overload
	def Get2dPoints(self, P2df1: gp_Pnt2d, P2dl1: gp_Pnt2d, P2df2: gp_Pnt2d, P2dl2: gp_Pnt2d) -> None: ...
	def Index(self, OfS: int) -> int: ...
	def IndexOfC(self, OnS: int) -> int: ...
	def IndexOfC1(self) -> int: ...
	def IndexOfC2(self) -> int: ...
	def IndexOfS1(self) -> int: ...
	def IndexOfS2(self) -> int: ...
	def Interference(self, OnS: int) -> ChFiDS_FaceInterference: ...
	def InterferenceOnS1(self) -> ChFiDS_FaceInterference: ...
	def InterferenceOnS2(self) -> ChFiDS_FaceInterference: ...
	def IsOnCurve(self, OnS: int) -> bool: ...
	def IsOnCurve1(self) -> bool: ...
	def IsOnCurve2(self) -> bool: ...
	@overload
	def LastExtensionValue(self) -> float: ...
	@overload
	def LastExtensionValue(self, Extend: float) -> None: ...
	@overload
	def LastSpineParam(self) -> float: ...
	@overload
	def LastSpineParam(self, Par: float) -> None: ...
	def Orientation(self) -> TopAbs_Orientation: ...
	def ResetSimul(self) -> None: ...
	def Set2dPoints(self, P2df1: gp_Pnt2d, P2dl1: gp_Pnt2d, P2df2: gp_Pnt2d, P2dl2: gp_Pnt2d) -> None: ...
	def SetIndexOfC1(self, Index: int) -> None: ...
	def SetIndexOfC2(self, Index: int) -> None: ...
	def SetSimul(self, S: Standard_Transient) -> None: ...
	def Simul(self) -> Standard_Transient: ...
	def Surf(self) -> int: ...
	@overload
	def TwistOnS1(self) -> bool: ...
	@overload
	def TwistOnS1(self, T: bool) -> None: ...
	@overload
	def TwistOnS2(self) -> bool: ...
	@overload
	def TwistOnS2(self, T: bool) -> None: ...
	def Vertex(self, First: bool, OnS: int) -> ChFiDS_CommonPoint: ...
	def VertexFirstOnS1(self) -> ChFiDS_CommonPoint: ...
	def VertexFirstOnS2(self) -> ChFiDS_CommonPoint: ...
	def VertexLastOnS1(self) -> ChFiDS_CommonPoint: ...
	def VertexLastOnS2(self) -> ChFiDS_CommonPoint: ...

class ChFiDS_ChamfSpine(ChFiDS_Spine):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Tol: float) -> None: ...
	def Dists(self) -> Tuple[float, float]: ...
	def GetDist(self) -> float: ...
	def GetDistAngle(self) -> Tuple[float, float]: ...
	def IsChamfer(self) -> ChFiDS_ChamfMethod: ...
	def SetDist(self, Dis: float) -> None: ...
	def SetDistAngle(self, Dis: float, Angle: float) -> None: ...
	def SetDists(self, Dis1: float, Dis2: float) -> None: ...
	def SetMode(self, theMode: ChFiDS_ChamfMode) -> None: ...

class ChFiDS_FilSpine(ChFiDS_Spine):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Tol: float) -> None: ...
	def AppendElSpine(self, Els: ChFiDS_HElSpine) -> None: ...
	def ChangeLaw(self, E: TopoDS_Edge) -> Law_Function: ...
	@overload
	def IsConstant(self) -> bool: ...
	@overload
	def IsConstant(self, IE: int) -> bool: ...
	def Law(self, Els: ChFiDS_HElSpine) -> Law_Composite: ...
	def MaxRadFromSeqAndLaws(self) -> float: ...
	@overload
	def Radius(self) -> float: ...
	@overload
	def Radius(self, IE: int) -> float: ...
	@overload
	def Radius(self, E: TopoDS_Edge) -> float: ...
	def Reset(self, AllData: Optional[bool]) -> None: ...
	@overload
	def SetRadius(self, Radius: float, E: TopoDS_Edge) -> None: ...
	@overload
	def SetRadius(self, Radius: float, V: TopoDS_Vertex) -> None: ...
	@overload
	def SetRadius(self, UandR: gp_XY, IinC: int) -> None: ...
	@overload
	def SetRadius(self, Radius: float) -> None: ...
	@overload
	def SetRadius(self, C: Law_Function, IinC: int) -> None: ...
	@overload
	def UnSetRadius(self, E: TopoDS_Edge) -> None: ...
	@overload
	def UnSetRadius(self, V: TopoDS_Vertex) -> None: ...

# harray1 classes

class ChFiDS_SecHArray1(ChFiDS_SecArray1, Standard_Transient):
    def ChFiDS_SecHArray1(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> ChFiDS_SecArray1: ...

# harray2 classes
# hsequence classes

class ChFiDS_HData(ChFiDS_SequenceOfSurfData, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: ChFiDS_SequenceOfSurfData) -> None: ...
    def Sequence(self) -> ChFiDS_SequenceOfSurfData: ...
    def Append(self, theSequence: ChFiDS_SequenceOfSurfData) -> None: ...


