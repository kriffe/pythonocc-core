from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.ShapeExtend import *
from OCC.Core.TopTools import *
from OCC.Core.gp import *
from OCC.Core.Geom2d import *
from OCC.Core.Bnd import *
from OCC.Core.TColgp import *
from OCC.Core.Geom import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TopLoc import *
from OCC.Core.TColStd import *
from OCC.Core.TopAbs import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.IntRes2d import *

#the following typedef cannot be wrapped as is
ShapeAnalysis_BoxBndTree = NewType('ShapeAnalysis_BoxBndTree', Any)
#the following typedef cannot be wrapped as is
ShapeAnalysis_DataMapIteratorOfDataMapOfShapeListOfReal = NewType('ShapeAnalysis_DataMapIteratorOfDataMapOfShapeListOfReal', Any)
#the following typedef cannot be wrapped as is
ShapeAnalysis_DataMapOfShapeListOfReal = NewType('ShapeAnalysis_DataMapOfShapeListOfReal', Any)
#the following typedef cannot be wrapped as is
ShapeAnalysis_SequenceOfFreeBounds = NewType('ShapeAnalysis_SequenceOfFreeBounds', Any)

class ShapeAnalysis:
	@staticmethod
	def AdjustByPeriod(self, Val: float, ToVal: float, Period: float) -> float: ...
	@staticmethod
	def AdjustToPeriod(self, Val: float, ValMin: float, ValMax: float) -> float: ...
	@staticmethod
	def ContourArea(self, theWire: TopoDS_Wire) -> float: ...
	@staticmethod
	def FindBounds(self, shape: TopoDS_Shape, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@staticmethod
	def GetFaceUVBounds(self, F: TopoDS_Face) -> Tuple[float, float, float, float]: ...
	@staticmethod
	def IsOuterBound(self, face: TopoDS_Face) -> bool: ...
	@staticmethod
	def OuterWire(self, face: TopoDS_Face) -> TopoDS_Wire: ...
	@staticmethod
	def TotCross2D(self, sewd: ShapeExtend_WireData, aFace: TopoDS_Face) -> float: ...

class ShapeAnalysis_CheckSmallFace:
	def __init__(self) -> None: ...
	def CheckPin(self, F: TopoDS_Face) -> Tuple[bool, int, int]: ...
	def CheckPinEdges(self, theFirstEdge: TopoDS_Edge, theSecondEdge: TopoDS_Edge, coef1: float, coef2: float, toler: float) -> bool: ...
	def CheckPinFace(self, F: TopoDS_Face, mapEdges: TopTools_DataMapOfShapeShape, toler: Optional[float]) -> bool: ...
	def CheckSingleStrip(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, tol: Optional[float]) -> bool: ...
	def CheckSplittingVertices(self, F: TopoDS_Face, MapEdges: TopTools_DataMapOfShapeListOfShape, MapParam: ShapeAnalysis_DataMapOfShapeListOfReal, theAllVert: TopoDS_Compound) -> int: ...
	def CheckSpotFace(self, F: TopoDS_Face, tol: Optional[float]) -> bool: ...
	def CheckStripEdges(self, E1: TopoDS_Edge, E2: TopoDS_Edge, tol: float) -> Tuple[bool, float]: ...
	def CheckStripFace(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, tol: Optional[float]) -> bool: ...
	def CheckTwisted(self, F: TopoDS_Face) -> Tuple[bool, float, float]: ...
	def FindStripEdges(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, tol: float) -> Tuple[bool, float]: ...
	def IsSpotFace(self, F: TopoDS_Face, spot: gp_Pnt, tol: Optional[float]) -> Tuple[int, float]: ...
	def IsStripSupport(self, F: TopoDS_Face, tol: Optional[float]) -> bool: ...
	def SetTolerance(self, tol: float) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...
	def StatusPin(self, status: ShapeExtend_Status) -> bool: ...
	def StatusPinEdges(self, status: ShapeExtend_Status) -> bool: ...
	def StatusPinFace(self, status: ShapeExtend_Status) -> bool: ...
	def StatusSplitVert(self, status: ShapeExtend_Status) -> bool: ...
	def StatusSpot(self, status: ShapeExtend_Status) -> bool: ...
	def StatusStrip(self, status: ShapeExtend_Status) -> bool: ...
	def StatusTwisted(self, status: ShapeExtend_Status) -> bool: ...
	def Tolerance(self) -> float: ...

class ShapeAnalysis_Curve:
	def FillBndBox(self, C2d: Geom2d_Curve, First: float, Last: float, NPoints: int, Exact: bool, Box: Bnd_Box2d) -> None: ...
	@overload
	@staticmethod
	def GetSamplePoints(self, curve: Geom2d_Curve, first: float, last: float, seq: TColgp_SequenceOfPnt2d) -> bool: ...
	@overload
	@staticmethod
	def GetSamplePoints(self, curve: Geom_Curve, first: float, last: float, seq: TColgp_SequenceOfPnt) -> bool: ...
	@staticmethod
	def IsClosed(self, curve: Geom_Curve, preci: Optional[float]) -> bool: ...
	@overload
	@staticmethod
	def IsPeriodic(self, curve: Geom_Curve) -> bool: ...
	@overload
	@staticmethod
	def IsPeriodic(self, curve: Geom2d_Curve) -> bool: ...
	@overload
	@staticmethod
	def IsPlanar(self, pnts: TColgp_Array1OfPnt, Normal: gp_XYZ, preci: Optional[float]) -> bool: ...
	@overload
	@staticmethod
	def IsPlanar(self, curve: Geom_Curve, Normal: gp_XYZ, preci: Optional[float]) -> bool: ...
	@overload
	def NextProject(self, paramPrev: float, C3D: Geom_Curve, P3D: gp_Pnt, preci: float, proj: gp_Pnt, cf: float, cl: float, AdjustToEnds: Optional[bool]) -> Tuple[float, float]: ...
	@overload
	def NextProject(self, paramPrev: float, C3D: Adaptor3d_Curve, P3D: gp_Pnt, preci: float, proj: gp_Pnt) -> Tuple[float, float]: ...
	@overload
	def Project(self, C3D: Geom_Curve, P3D: gp_Pnt, preci: float, proj: gp_Pnt, AdjustToEnds: Optional[bool]) -> Tuple[float, float]: ...
	@overload
	def Project(self, C3D: Adaptor3d_Curve, P3D: gp_Pnt, preci: float, proj: gp_Pnt, AdjustToEnds: Optional[bool]) -> Tuple[float, float]: ...
	@overload
	def Project(self, C3D: Geom_Curve, P3D: gp_Pnt, preci: float, proj: gp_Pnt, cf: float, cl: float, AdjustToEnds: Optional[bool]) -> Tuple[float, float]: ...
	def ProjectAct(self, C3D: Adaptor3d_Curve, P3D: gp_Pnt, preci: float, proj: gp_Pnt) -> Tuple[float, float]: ...
	def SelectForwardSeam(self, C1: Geom2d_Curve, C2: Geom2d_Curve) -> int: ...
	def ValidateRange(self, Crv: Geom_Curve, prec: float) -> Tuple[bool, float, float]: ...

class ShapeAnalysis_Edge:
	def __init__(self) -> None: ...
	@overload
	def BoundUV(self, edge: TopoDS_Edge, face: TopoDS_Face, first: gp_Pnt2d, last: gp_Pnt2d) -> bool: ...
	@overload
	def BoundUV(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location, first: gp_Pnt2d, last: gp_Pnt2d) -> bool: ...
	@overload
	def CheckCurve3dWithPCurve(self, edge: TopoDS_Edge, face: TopoDS_Face) -> bool: ...
	@overload
	def CheckCurve3dWithPCurve(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location) -> bool: ...
	def CheckOverlapping(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, theDomainDist: Optional[float]) -> Tuple[bool, float]: ...
	def CheckPCurveRange(self, theFirst: float, theLast: float, thePC: Geom2d_Curve) -> bool: ...
	@overload
	def CheckSameParameter(self, edge: TopoDS_Edge, NbControl: Optional[int]) -> Tuple[bool, float]: ...
	@overload
	def CheckSameParameter(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face, theNbControl: Optional[int]) -> Tuple[bool, float]: ...
	@overload
	def CheckVertexTolerance(self, edge: TopoDS_Edge, face: TopoDS_Face) -> Tuple[bool, float, float]: ...
	@overload
	def CheckVertexTolerance(self, edge: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def CheckVerticesWithCurve3d(self, edge: TopoDS_Edge, preci: Optional[float], vtx: Optional[int]) -> bool: ...
	@overload
	def CheckVerticesWithPCurve(self, edge: TopoDS_Edge, face: TopoDS_Face, preci: Optional[float], vtx: Optional[int]) -> bool: ...
	@overload
	def CheckVerticesWithPCurve(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location, preci: Optional[float], vtx: Optional[int]) -> bool: ...
	@staticmethod
	def ComputeDeviation(self, CRef: Adaptor3d_Curve, Other: Adaptor3d_Curve, SameParameter: bool, NCONTROL: int) -> Tuple[bool, float]: ...
	def Curve3d(self, edge: TopoDS_Edge, C3d: Geom_Curve, orient: Optional[bool]) -> Tuple[bool, float, float]: ...
	def FirstVertex(self, edge: TopoDS_Edge) -> TopoDS_Vertex: ...
	@overload
	def GetEndTangent2d(self, edge: TopoDS_Edge, face: TopoDS_Face, atEnd: bool, pos: gp_Pnt2d, tang: gp_Vec2d, dparam: Optional[float]) -> bool: ...
	@overload
	def GetEndTangent2d(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location, atEnd: bool, pos: gp_Pnt2d, tang: gp_Vec2d, dparam: Optional[float]) -> bool: ...
	def HasCurve3d(self, edge: TopoDS_Edge) -> bool: ...
	@overload
	def HasPCurve(self, edge: TopoDS_Edge, face: TopoDS_Face) -> bool: ...
	@overload
	def HasPCurve(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location) -> bool: ...
	def IsClosed3d(self, edge: TopoDS_Edge) -> bool: ...
	@overload
	def IsSeam(self, edge: TopoDS_Edge, face: TopoDS_Face) -> bool: ...
	@overload
	def IsSeam(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location) -> bool: ...
	def LastVertex(self, edge: TopoDS_Edge) -> TopoDS_Vertex: ...
	@overload
	def PCurve(self, edge: TopoDS_Edge, face: TopoDS_Face, C2d: Geom2d_Curve, orient: Optional[bool]) -> Tuple[bool, float, float]: ...
	@overload
	def PCurve(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location, C2d: Geom2d_Curve, orient: Optional[bool]) -> Tuple[bool, float, float]: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeAnalysis_FreeBoundData(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, freebound: TopoDS_Wire) -> None: ...
	def AddNotch(self, notch: TopoDS_Wire, width: float) -> None: ...
	def Area(self) -> float: ...
	def Clear(self) -> None: ...
	def FreeBound(self) -> TopoDS_Wire: ...
	def NbNotches(self) -> int: ...
	def Notch(self, index: int) -> TopoDS_Wire: ...
	@overload
	def NotchWidth(self, index: int) -> float: ...
	@overload
	def NotchWidth(self, notch: TopoDS_Wire) -> float: ...
	def Notches(self) -> TopTools_HSequenceOfShape: ...
	def Perimeter(self) -> float: ...
	def Ratio(self) -> float: ...
	def SetArea(self, area: float) -> None: ...
	def SetFreeBound(self, freebound: TopoDS_Wire) -> None: ...
	def SetPerimeter(self, perimeter: float) -> None: ...
	def SetRatio(self, ratio: float) -> None: ...
	def SetWidth(self, width: float) -> None: ...
	def Width(self) -> float: ...

class ShapeAnalysis_FreeBounds:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape, toler: float, splitclosed: Optional[bool], splitopen: Optional[bool]) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape, splitclosed: Optional[bool], splitopen: Optional[bool], checkinternaledges: Optional[bool]) -> None: ...
	@staticmethod
	def ConnectEdgesToWires(self, edges: TopTools_HSequenceOfShape, toler: float, shared: bool, wires: TopTools_HSequenceOfShape) -> None: ...
	@overload
	@staticmethod
	def ConnectWiresToWires(self, iwires: TopTools_HSequenceOfShape, toler: float, shared: bool, owires: TopTools_HSequenceOfShape) -> None: ...
	@overload
	@staticmethod
	def ConnectWiresToWires(self, iwires: TopTools_HSequenceOfShape, toler: float, shared: bool, owires: TopTools_HSequenceOfShape, vertices: TopTools_DataMapOfShapeShape) -> None: ...
	@staticmethod
	def DispatchWires(self, wires: TopTools_HSequenceOfShape, closed: TopoDS_Compound, open: TopoDS_Compound) -> None: ...
	def GetClosedWires(self) -> TopoDS_Compound: ...
	def GetOpenWires(self) -> TopoDS_Compound: ...
	@staticmethod
	def SplitWires(self, wires: TopTools_HSequenceOfShape, toler: float, shared: bool, closed: TopTools_HSequenceOfShape, open: TopTools_HSequenceOfShape) -> None: ...

class ShapeAnalysis_FreeBoundsProperties:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape, tolerance: float, splitclosed: Optional[bool], splitopen: Optional[bool]) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape, splitclosed: Optional[bool], splitopen: Optional[bool]) -> None: ...
	def CheckContours(self, prec: Optional[float]) -> bool: ...
	@overload
	def CheckNotches(self, prec: Optional[float]) -> bool: ...
	@overload
	def CheckNotches(self, fbData: ShapeAnalysis_FreeBoundData, prec: Optional[float]) -> bool: ...
	@overload
	def CheckNotches(self, freebound: TopoDS_Wire, num: int, notch: TopoDS_Wire, prec: Optional[float]) -> Tuple[bool, float]: ...
	def ClosedFreeBound(self, index: int) -> ShapeAnalysis_FreeBoundData: ...
	def ClosedFreeBounds(self) -> ShapeAnalysis_HSequenceOfFreeBounds: ...
	def DispatchBounds(self) -> bool: ...
	def FillProperties(self, fbData: ShapeAnalysis_FreeBoundData, prec: Optional[float]) -> bool: ...
	@overload
	def Init(self, shape: TopoDS_Shape, tolerance: float, splitclosed: Optional[bool], splitopen: Optional[bool]) -> None: ...
	@overload
	def Init(self, shape: TopoDS_Shape, splitclosed: Optional[bool], splitopen: Optional[bool]) -> None: ...
	def IsLoaded(self) -> bool: ...
	def NbClosedFreeBounds(self) -> int: ...
	def NbFreeBounds(self) -> int: ...
	def NbOpenFreeBounds(self) -> int: ...
	def OpenFreeBound(self, index: int) -> ShapeAnalysis_FreeBoundData: ...
	def OpenFreeBounds(self) -> ShapeAnalysis_HSequenceOfFreeBounds: ...
	def Perform(self) -> bool: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Tolerance(self) -> float: ...

class ShapeAnalysis_Geom:
	@staticmethod
	def NearestPlane(self, Pnts: TColgp_Array1OfPnt, aPln: gp_Pln) -> Tuple[bool, float]: ...
	@staticmethod
	def PositionTrsf(self, coefs: TColStd_HArray2OfReal, trsf: gp_Trsf, unit: float, prec: float) -> bool: ...

class ShapeAnalysis_ShapeContents:
	def __init__(self) -> None: ...
	def BigSplineSec(self) -> TopTools_HSequenceOfShape: ...
	def Clear(self) -> None: ...
	def ClearFlags(self) -> None: ...
	def IndirectSec(self) -> TopTools_HSequenceOfShape: ...
	def GetModifyBigSplineMode(self) -> bool: ...
	def SetModifyBigSplineMode(self, value: bool) -> None: ...
	def GetModifyIndirectMode(self) -> bool: ...
	def SetModifyIndirectMode(self, value: bool) -> None: ...
	def GetModifyOffestSurfaceMode(self) -> bool: ...
	def SetModifyOffestSurfaceMode(self, value: bool) -> None: ...
	def GetModifyOffsetCurveMode(self) -> bool: ...
	def SetModifyOffsetCurveMode(self, value: bool) -> None: ...
	def GetModifyTrimmed2dMode(self) -> bool: ...
	def SetModifyTrimmed2dMode(self, value: bool) -> None: ...
	def GetModifyTrimmed3dMode(self) -> bool: ...
	def SetModifyTrimmed3dMode(self, value: bool) -> None: ...
	def NbBSplibeSurf(self) -> int: ...
	def NbBezierSurf(self) -> int: ...
	def NbBigSplines(self) -> int: ...
	def NbC0Curves(self) -> int: ...
	def NbC0Surfaces(self) -> int: ...
	def NbEdges(self) -> int: ...
	def NbFaceWithSevWires(self) -> int: ...
	def NbFaces(self) -> int: ...
	def NbFreeEdges(self) -> int: ...
	def NbFreeFaces(self) -> int: ...
	def NbFreeWires(self) -> int: ...
	def NbIndirectSurf(self) -> int: ...
	def NbNoPCurve(self) -> int: ...
	def NbOffsetCurves(self) -> int: ...
	def NbOffsetSurf(self) -> int: ...
	def NbSharedEdges(self) -> int: ...
	def NbSharedFaces(self) -> int: ...
	def NbSharedFreeEdges(self) -> int: ...
	def NbSharedFreeWires(self) -> int: ...
	def NbSharedShells(self) -> int: ...
	def NbSharedSolids(self) -> int: ...
	def NbSharedVertices(self) -> int: ...
	def NbSharedWires(self) -> int: ...
	def NbShells(self) -> int: ...
	def NbSolids(self) -> int: ...
	def NbSolidsWithVoids(self) -> int: ...
	def NbTrimSurf(self) -> int: ...
	def NbTrimmedCurve2d(self) -> int: ...
	def NbTrimmedCurve3d(self) -> int: ...
	def NbVertices(self) -> int: ...
	def NbWireWithSevSeams(self) -> int: ...
	def NbWireWitnSeam(self) -> int: ...
	def NbWires(self) -> int: ...
	def OffsetCurveSec(self) -> TopTools_HSequenceOfShape: ...
	def OffsetSurfaceSec(self) -> TopTools_HSequenceOfShape: ...
	def Perform(self, shape: TopoDS_Shape) -> None: ...
	def Trimmed2dSec(self) -> TopTools_HSequenceOfShape: ...
	def Trimmed3dSec(self) -> TopTools_HSequenceOfShape: ...

class ShapeAnalysis_ShapeTolerance:
	def __init__(self) -> None: ...
	def AddTolerance(self, shape: TopoDS_Shape, type: Optional[TopAbs_ShapeEnum]) -> None: ...
	def GlobalTolerance(self, mode: int) -> float: ...
	def InTolerance(self, shape: TopoDS_Shape, valmin: float, valmax: float, type: Optional[TopAbs_ShapeEnum]) -> TopTools_HSequenceOfShape: ...
	def InitTolerance(self) -> None: ...
	def OverTolerance(self, shape: TopoDS_Shape, value: float, type: Optional[TopAbs_ShapeEnum]) -> TopTools_HSequenceOfShape: ...
	def Tolerance(self, shape: TopoDS_Shape, mode: int, type: Optional[TopAbs_ShapeEnum]) -> float: ...

class ShapeAnalysis_Shell:
	def BadEdges(self) -> TopoDS_Compound: ...
	def CheckOrientedShells(self, shape: TopoDS_Shape, alsofree: Optional[bool], checkinternaledges: Optional[bool]) -> bool: ...
	def Clear(self) -> None: ...
	def FreeEdges(self) -> TopoDS_Compound: ...
	def HasBadEdges(self) -> bool: ...
	def HasConnectedEdges(self) -> bool: ...
	def HasFreeEdges(self) -> bool: ...
	def IsLoaded(self, shape: TopoDS_Shape) -> bool: ...
	def LoadShells(self, shape: TopoDS_Shape) -> None: ...
	def Loaded(self, num: int) -> TopoDS_Shape: ...
	def NbLoaded(self) -> int: ...

class ShapeAnalysis_Surface(Standard_Transient):
	def __init__(self, S: Geom_Surface) -> None: ...
	def Adaptor3d(self) -> GeomAdaptor_HSurface: ...
	def Bounds(self) -> Tuple[float, float, float, float]: ...
	def ComputeBoundIsos(self) -> None: ...
	def DegeneratedValues(self, P3d: gp_Pnt, preci: float, firstP2d: gp_Pnt2d, lastP2d: gp_Pnt2d, forward: Optional[bool]) -> Tuple[bool, float, float]: ...
	def Gap(self) -> float: ...
	def GetBoxUF(self) -> Bnd_Box: ...
	def GetBoxUL(self) -> Bnd_Box: ...
	def GetBoxVF(self) -> Bnd_Box: ...
	def GetBoxVL(self) -> Bnd_Box: ...
	def HasSingularities(self, preci: float) -> bool: ...
	@overload
	def Init(self, S: Geom_Surface) -> None: ...
	@overload
	def Init(self, other: ShapeAnalysis_Surface) -> None: ...
	@overload
	def IsDegenerated(self, P3d: gp_Pnt, preci: float) -> bool: ...
	@overload
	def IsDegenerated(self, p2d1: gp_Pnt2d, p2d2: gp_Pnt2d, tol: float, ratio: float) -> bool: ...
	def IsUClosed(self, preci: Optional[float]) -> bool: ...
	def IsVClosed(self, preci: Optional[float]) -> bool: ...
	def NbSingularities(self, preci: float) -> int: ...
	def NextValueOfUV(self, p2dPrev: gp_Pnt2d, P3D: gp_Pnt, preci: float, maxpreci: Optional[float]) -> gp_Pnt2d: ...
	@overload
	def ProjectDegenerated(self, P3d: gp_Pnt, preci: float, neighbour: gp_Pnt2d, result: gp_Pnt2d) -> bool: ...
	@overload
	def ProjectDegenerated(self, nbrPnt: int, points: TColgp_SequenceOfPnt, pnt2d: TColgp_SequenceOfPnt2d, preci: float, direct: bool) -> bool: ...
	def SetDomain(self, U1: float, U2: float, V1: float, V2: float) -> None: ...
	def Singularity(self, num: int, P3d: gp_Pnt, firstP2d: gp_Pnt2d, lastP2d: gp_Pnt2d) -> Tuple[bool, float, float, float, bool]: ...
	def Surface(self) -> Geom_Surface: ...
	def TrueAdaptor3d(self) -> GeomAdaptor_HSurface: ...
	def UCloseVal(self) -> float: ...
	def UIso(self, U: float) -> Geom_Curve: ...
	def UVFromIso(self, P3D: gp_Pnt, preci: float) -> Tuple[float, float, float]: ...
	def VCloseVal(self) -> float: ...
	def VIso(self, V: float) -> Geom_Curve: ...
	@overload
	def Value(self, u: float, v: float) -> gp_Pnt: ...
	@overload
	def Value(self, p2d: gp_Pnt2d) -> gp_Pnt: ...
	def ValueOfUV(self, P3D: gp_Pnt, preci: float) -> gp_Pnt2d: ...

class ShapeAnalysis_TransferParameters(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def Init(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def IsSameRange(self) -> bool: ...
	@overload
	def Perform(self, Params: TColStd_HSequenceOfReal, To2d: bool) -> TColStd_HSequenceOfReal: ...
	@overload
	def Perform(self, Param: float, To2d: bool) -> float: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def TransferRange(self, newEdge: TopoDS_Edge, prevPar: float, currPar: float, To2d: bool) -> None: ...

class ShapeAnalysis_Wire(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, wire: TopoDS_Wire, face: TopoDS_Face, precision: float) -> None: ...
	@overload
	def __init__(self, sbwd: ShapeExtend_WireData, face: TopoDS_Face, precision: float) -> None: ...
	def CheckClosed(self, prec: Optional[float]) -> bool: ...
	@overload
	def CheckConnected(self, prec: Optional[float]) -> bool: ...
	@overload
	def CheckConnected(self, num: int, prec: Optional[float]) -> bool: ...
	def CheckCurveGap(self, num: Optional[int]) -> bool: ...
	def CheckCurveGaps(self) -> bool: ...
	@overload
	def CheckDegenerated(self) -> bool: ...
	@overload
	def CheckDegenerated(self, num: int, dgnr1: gp_Pnt2d, dgnr2: gp_Pnt2d) -> bool: ...
	@overload
	def CheckDegenerated(self, num: int) -> bool: ...
	def CheckEdgeCurves(self) -> bool: ...
	def CheckGap2d(self, num: Optional[int]) -> bool: ...
	def CheckGap3d(self, num: Optional[int]) -> bool: ...
	def CheckGaps2d(self) -> bool: ...
	def CheckGaps3d(self) -> bool: ...
	@overload
	def CheckIntersectingEdges(self, num: int, points2d: IntRes2d_SequenceOfIntersectionPoint, points3d: TColgp_SequenceOfPnt, errors: TColStd_SequenceOfReal) -> bool: ...
	@overload
	def CheckIntersectingEdges(self, num: int) -> bool: ...
	@overload
	def CheckIntersectingEdges(self, num1: int, num2: int, points2d: IntRes2d_SequenceOfIntersectionPoint, points3d: TColgp_SequenceOfPnt, errors: TColStd_SequenceOfReal) -> bool: ...
	@overload
	def CheckIntersectingEdges(self, num1: int, num2: int) -> bool: ...
	@overload
	def CheckLacking(self) -> bool: ...
	@overload
	def CheckLacking(self, num: int, Tolerance: float, p2d1: gp_Pnt2d, p2d2: gp_Pnt2d) -> bool: ...
	@overload
	def CheckLacking(self, num: int, Tolerance: Optional[float]) -> bool: ...
	def CheckLoop(self, aMapLoopVertices: TopTools_IndexedMapOfShape, aMapVertexEdges: TopTools_DataMapOfShapeListOfShape, aMapSmallEdges: TopTools_MapOfShape, aMapSeemEdges: TopTools_MapOfShape) -> bool: ...
	def CheckNotchedEdges(self, num: int, Tolerance: Optional[float]) -> Tuple[bool, int, float]: ...
	@overload
	def CheckOrder(self, isClosed: Optional[bool], mode3d: Optional[bool]) -> bool: ...
	@overload
	def CheckOrder(self, sawo: ShapeAnalysis_WireOrder, isClosed: Optional[bool], mode3d: Optional[bool]) -> bool: ...
	def CheckOuterBound(self, APIMake: Optional[bool]) -> bool: ...
	@overload
	def CheckSeam(self, num: int, C1: Geom2d_Curve, C2: Geom2d_Curve) -> Tuple[bool, float, float]: ...
	@overload
	def CheckSeam(self, num: int) -> bool: ...
	@overload
	def CheckSelfIntersectingEdge(self, num: int, points2d: IntRes2d_SequenceOfIntersectionPoint, points3d: TColgp_SequenceOfPnt) -> bool: ...
	@overload
	def CheckSelfIntersectingEdge(self, num: int) -> bool: ...
	def CheckSelfIntersection(self) -> bool: ...
	@overload
	def CheckShapeConnect(self, shape: TopoDS_Shape, prec: Optional[float]) -> bool: ...
	@overload
	def CheckShapeConnect(self, shape: TopoDS_Shape, prec: Optional[float]) -> Tuple[bool, float, float, float, float]: ...
	@overload
	def CheckSmall(self, precsmall: Optional[float]) -> bool: ...
	@overload
	def CheckSmall(self, num: int, precsmall: Optional[float]) -> bool: ...
	def CheckSmallArea(self, theWire: TopoDS_Wire) -> bool: ...
	def CheckTail(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, theMaxSine: float, theMaxWidth: float, theMaxTolerance: float, theEdge11: TopoDS_Edge, theEdge12: TopoDS_Edge, theEdge21: TopoDS_Edge, theEdge22: TopoDS_Edge) -> bool: ...
	def ClearStatuses(self) -> None: ...
	def Face(self) -> TopoDS_Face: ...
	@overload
	def Init(self, wire: TopoDS_Wire, face: TopoDS_Face, precision: float) -> None: ...
	@overload
	def Init(self, sbwd: ShapeExtend_WireData, face: TopoDS_Face, precision: float) -> None: ...
	def IsLoaded(self) -> bool: ...
	def IsReady(self) -> bool: ...
	def LastCheckStatus(self, Status: ShapeExtend_Status) -> bool: ...
	@overload
	def Load(self, wire: TopoDS_Wire) -> None: ...
	@overload
	def Load(self, sbwd: ShapeExtend_WireData) -> None: ...
	def MaxDistance2d(self) -> float: ...
	def MaxDistance3d(self) -> float: ...
	def MinDistance2d(self) -> float: ...
	def MinDistance3d(self) -> float: ...
	def NbEdges(self) -> int: ...
	def Perform(self) -> bool: ...
	def Precision(self) -> float: ...
	def SetFace(self, face: TopoDS_Face) -> None: ...
	def SetPrecision(self, precision: float) -> None: ...
	@overload
	def SetSurface(self, surface: Geom_Surface) -> None: ...
	@overload
	def SetSurface(self, surface: Geom_Surface, location: TopLoc_Location) -> None: ...
	def StatusClosed(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusConnected(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusCurveGaps(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusDegenerated(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusEdgeCurves(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusGaps2d(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusGaps3d(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusLacking(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusLoop(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusOrder(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusSelfIntersection(self, Status: ShapeExtend_Status) -> bool: ...
	def StatusSmall(self, Status: ShapeExtend_Status) -> bool: ...
	def Surface(self) -> ShapeAnalysis_Surface: ...
	def WireData(self) -> ShapeExtend_WireData: ...

class ShapeAnalysis_WireOrder:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, mode3d: bool, tol: float) -> None: ...
	@overload
	def Add(self, start3d: gp_XYZ, end3d: gp_XYZ) -> None: ...
	@overload
	def Add(self, start2d: gp_XY, end2d: gp_XY) -> None: ...
	def Chain(self, num: int) -> Tuple[int, int]: ...
	def Clear(self) -> None: ...
	def Couple(self, num: int) -> Tuple[int, int]: ...
	def Gap(self, num: Optional[int]) -> float: ...
	def IsDone(self) -> bool: ...
	def GetKeepLoopsMode(self) -> bool: ...
	def SetKeepLoopsMode(self, value: bool) -> None: ...
	def NbChains(self) -> int: ...
	def NbCouples(self) -> int: ...
	def NbEdges(self) -> int: ...
	def Ordered(self, n: int) -> int: ...
	def Perform(self, closed: Optional[bool]) -> None: ...
	def SetChains(self, gap: float) -> None: ...
	def SetCouples(self, gap: float) -> None: ...
	def SetMode(self, mode3d: bool, tol: float) -> None: ...
	def Status(self) -> int: ...
	def Tolerance(self) -> float: ...
	def XY(self, num: int, start2d: gp_XY, end2d: gp_XY) -> None: ...
	def XYZ(self, num: int, start3d: gp_XYZ, end3d: gp_XYZ) -> None: ...

class ShapeAnalysis_WireVertex:
	def __init__(self) -> None: ...
	def Analyze(self) -> None: ...
	def Data(self, num: int, pos: gp_XYZ) -> Tuple[int, float, float]: ...
	@overload
	def Init(self, wire: TopoDS_Wire, preci: float) -> None: ...
	@overload
	def Init(self, swbd: ShapeExtend_WireData, preci: float) -> None: ...
	def IsDone(self) -> bool: ...
	@overload
	def Load(self, wire: TopoDS_Wire) -> None: ...
	@overload
	def Load(self, sbwd: ShapeExtend_WireData) -> None: ...
	def NbEdges(self) -> int: ...
	def NextCriter(self, crit: int, num: Optional[int]) -> int: ...
	def NextStatus(self, stat: int, num: Optional[int]) -> int: ...
	def Position(self, num: int) -> gp_XYZ: ...
	def Precision(self) -> float: ...
	def SetClose(self, num: int) -> None: ...
	def SetDisjoined(self, num: int) -> None: ...
	def SetEnd(self, num: int, pos: gp_XYZ, ufol: float) -> None: ...
	def SetInters(self, num: int, pos: gp_XYZ, upre: float, ufol: float) -> None: ...
	def SetPrecision(self, preci: float) -> None: ...
	def SetSameCoords(self, num: int) -> None: ...
	def SetSameVertex(self, num: int) -> None: ...
	def SetStart(self, num: int, pos: gp_XYZ, upre: float) -> None: ...
	def Status(self, num: int) -> int: ...
	def UFollowing(self, num: int) -> float: ...
	def UPrevious(self, num: int) -> float: ...
	def WireData(self) -> ShapeExtend_WireData: ...

class ShapeAnalysis_TransferParametersProj(ShapeAnalysis_TransferParameters):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	@overload
	@staticmethod
	def CopyNMVertex(self, theVert: TopoDS_Vertex, toedge: TopoDS_Edge, fromedge: TopoDS_Edge) -> TopoDS_Vertex: ...
	@overload
	@staticmethod
	def CopyNMVertex(self, theVert: TopoDS_Vertex, toFace: TopoDS_Face, fromFace: TopoDS_Face) -> TopoDS_Vertex: ...
	def GetForceProjection(self) -> bool: ...
	def SetForceProjection(self, value: bool) -> None: ...
	def Init(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def IsSameRange(self) -> bool: ...
	@overload
	def Perform(self, Papams: TColStd_HSequenceOfReal, To2d: bool) -> TColStd_HSequenceOfReal: ...
	@overload
	def Perform(self, Param: float, To2d: bool) -> float: ...
	def TransferRange(self, newEdge: TopoDS_Edge, prevPar: float, currPar: float, Is2d: bool) -> None: ...

#classnotwrapped
class ShapeAnalysis_BoxBndTreeSelector: ...

#classnotwrapped
class ShapeCustom_ConvertToRevolution: ...

# harray1 classes
# harray2 classes
# harray2 classes

class ShapeAnalysis_HSequenceOfFreeBounds(ShapeAnalysis_SequenceOfFreeBounds, Standard_Transient): ...


shapeanalysis_AdjustByPeriod = shapeanalysis.AdjustByPeriod
shapeanalysis_AdjustToPeriod = shapeanalysis.AdjustToPeriod
shapeanalysis_ContourArea = shapeanalysis.ContourArea
shapeanalysis_FindBounds = shapeanalysis.FindBounds
shapeanalysis_GetFaceUVBounds = shapeanalysis.GetFaceUVBounds
shapeanalysis_IsOuterBound = shapeanalysis.IsOuterBound
shapeanalysis_OuterWire = shapeanalysis.OuterWire
shapeanalysis_TotCross2D = shapeanalysis.TotCross2D
ShapeAnalysis_Curve_GetSamplePoints = ShapeAnalysis_Curve.GetSamplePoints
ShapeAnalysis_Curve_GetSamplePoints = ShapeAnalysis_Curve.GetSamplePoints
ShapeAnalysis_Curve_IsClosed = ShapeAnalysis_Curve.IsClosed
ShapeAnalysis_Curve_IsPeriodic = ShapeAnalysis_Curve.IsPeriodic
ShapeAnalysis_Curve_IsPeriodic = ShapeAnalysis_Curve.IsPeriodic
ShapeAnalysis_Curve_IsPlanar = ShapeAnalysis_Curve.IsPlanar
ShapeAnalysis_Curve_IsPlanar = ShapeAnalysis_Curve.IsPlanar
ShapeAnalysis_Edge_ComputeDeviation = ShapeAnalysis_Edge.ComputeDeviation
ShapeAnalysis_FreeBounds_ConnectEdgesToWires = ShapeAnalysis_FreeBounds.ConnectEdgesToWires
ShapeAnalysis_FreeBounds_ConnectWiresToWires = ShapeAnalysis_FreeBounds.ConnectWiresToWires
ShapeAnalysis_FreeBounds_ConnectWiresToWires = ShapeAnalysis_FreeBounds.ConnectWiresToWires
ShapeAnalysis_FreeBounds_DispatchWires = ShapeAnalysis_FreeBounds.DispatchWires
ShapeAnalysis_FreeBounds_SplitWires = ShapeAnalysis_FreeBounds.SplitWires
ShapeAnalysis_Geom_NearestPlane = ShapeAnalysis_Geom.NearestPlane
ShapeAnalysis_Geom_PositionTrsf = ShapeAnalysis_Geom.PositionTrsf
ShapeAnalysis_TransferParametersProj_CopyNMVertex = ShapeAnalysis_TransferParametersProj.CopyNMVertex
ShapeAnalysis_TransferParametersProj_CopyNMVertex = ShapeAnalysis_TransferParametersProj.CopyNMVertex
