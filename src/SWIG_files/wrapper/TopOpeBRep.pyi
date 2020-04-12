from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepTopAdaptor import *
from OCC.Core.IntRes2d import *
from OCC.Core.IntSurf import *
from OCC.Core.IntPatch import *
from OCC.Core.TopOpeBRepDS import *
from OCC.Core.TopoDS import *
from OCC.Core.TopOpeBRepTool import *
from OCC.Core.Geom2dAdaptor import *
from OCC.Core.TCollection import *
from OCC.Core.Bnd import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TopAbs import *
from OCC.Core.gp import *
from OCC.Core.TopTools import *
from OCC.Core.Geom2d import *
from OCC.Core.Geom import *

#the following typedef cannot be wrapped as is
TopOpeBRep_DataMapIteratorOfDataMapOfTopolTool = NewType('TopOpeBRep_DataMapIteratorOfDataMapOfTopolTool', Any)
#the following typedef cannot be wrapped as is
TopOpeBRep_DataMapOfTopolTool = NewType('TopOpeBRep_DataMapOfTopolTool', Any)
#the following typedef cannot be wrapped as is
TopOpeBRep_ListIteratorOfListOfBipoint = NewType('TopOpeBRep_ListIteratorOfListOfBipoint', Any)
#the following typedef cannot be wrapped as is
TopOpeBRep_ListOfBipoint = NewType('TopOpeBRep_ListOfBipoint', Any)
TopOpeBRep_PEdgesIntersector = NewType('TopOpeBRep_PEdgesIntersector', TopOpeBRep_EdgesIntersector)
TopOpeBRep_PFacesFiller = NewType('TopOpeBRep_PFacesFiller', TopOpeBRep_FacesFiller)
TopOpeBRep_PFacesIntersector = NewType('TopOpeBRep_PFacesIntersector', TopOpeBRep_FacesIntersector)
TopOpeBRep_PIntRes2d_IntersectionPoint = NewType('TopOpeBRep_PIntRes2d_IntersectionPoint', IntRes2d_IntersectionPoint)
TopOpeBRep_PLineInter = NewType('TopOpeBRep_PLineInter', TopOpeBRep_LineInter)
TopOpeBRep_PPntOn2S = NewType('TopOpeBRep_PPntOn2S', IntSurf_PntOn2S)
TopOpeBRep_PThePointOfIntersection = NewType('TopOpeBRep_PThePointOfIntersection', IntPatch_Point)
#the following typedef cannot be wrapped as is
TopOpeBRep_SequenceOfPoint2d = NewType('TopOpeBRep_SequenceOfPoint2d', Any)

class TopOpeBRep_Array1OfLineInter:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> TopOpeBRep_LineInter: ...
    def __setitem__(self, index: int, value: TopOpeBRep_LineInter) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TopOpeBRep_LineInter]:
    def next(self) -> TopOpeBRep_LineInter: ...
    __next__ = next

class TopOpeBRep_Array1OfVPointInter:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> TopOpeBRep_VPointInter: ...
    def __setitem__(self, index: int, value: TopOpeBRep_VPointInter) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TopOpeBRep_VPointInter]:
    def next(self) -> TopOpeBRep_VPointInter: ...
    __next__ = next

class TopOpeBRep_P2Dstatus(IntEnum):
	TopOpeBRep_P2DUNK: int = ...
	TopOpeBRep_P2DINT: int = ...
	TopOpeBRep_P2DSGF: int = ...
	TopOpeBRep_P2DSGL: int = ...
	TopOpeBRep_P2DNEW: int = ...
TopOpeBRep_P2DUNK = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DUNK
TopOpeBRep_P2DINT = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DINT
TopOpeBRep_P2DSGF = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGF
TopOpeBRep_P2DSGL = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DSGL
TopOpeBRep_P2DNEW = TopOpeBRep_P2Dstatus.TopOpeBRep_P2DNEW

class TopOpeBRep_TypeLineCurve(IntEnum):
	TopOpeBRep_ANALYTIC: int = ...
	TopOpeBRep_RESTRICTION: int = ...
	TopOpeBRep_WALKING: int = ...
	TopOpeBRep_LINE: int = ...
	TopOpeBRep_CIRCLE: int = ...
	TopOpeBRep_ELLIPSE: int = ...
	TopOpeBRep_PARABOLA: int = ...
	TopOpeBRep_HYPERBOLA: int = ...
	TopOpeBRep_OTHERTYPE: int = ...
TopOpeBRep_ANALYTIC = TopOpeBRep_TypeLineCurve.TopOpeBRep_ANALYTIC
TopOpeBRep_RESTRICTION = TopOpeBRep_TypeLineCurve.TopOpeBRep_RESTRICTION
TopOpeBRep_WALKING = TopOpeBRep_TypeLineCurve.TopOpeBRep_WALKING
TopOpeBRep_LINE = TopOpeBRep_TypeLineCurve.TopOpeBRep_LINE
TopOpeBRep_CIRCLE = TopOpeBRep_TypeLineCurve.TopOpeBRep_CIRCLE
TopOpeBRep_ELLIPSE = TopOpeBRep_TypeLineCurve.TopOpeBRep_ELLIPSE
TopOpeBRep_PARABOLA = TopOpeBRep_TypeLineCurve.TopOpeBRep_PARABOLA
TopOpeBRep_HYPERBOLA = TopOpeBRep_TypeLineCurve.TopOpeBRep_HYPERBOLA
TopOpeBRep_OTHERTYPE = TopOpeBRep_TypeLineCurve.TopOpeBRep_OTHERTYPE

class TopOpeBRep:
	pass

class TopOpeBRep_Bipoint:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, I1: int, I2: int) -> None: ...
	def I1(self) -> int: ...
	def I2(self) -> int: ...

class TopOpeBRep_DSFiller:
	def __init__(self) -> None: ...
	def ChangeEdgesFiller(self) -> TopOpeBRep_EdgesFiller: ...
	def ChangeFaceEdgeFiller(self) -> TopOpeBRep_FaceEdgeFiller: ...
	def ChangeFacesFiller(self) -> TopOpeBRep_FacesFiller: ...
	def ChangeShapeIntersector(self) -> TopOpeBRep_ShapeIntersector: ...
	def ChangeShapeIntersector2d(self) -> TopOpeBRep_ShapeIntersector2d: ...
	def Checker(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def Complete(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def CompleteDS(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def CompleteDS2d(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def Filter(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def GapFiller(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def Insert(self, S1: TopoDS_Shape, S2: TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure, orientFORWARD: Optional[bool]) -> None: ...
	def Insert1d(self, S1: TopoDS_Shape, S2: TopoDS_Shape, F1: TopoDS_Face, F2: TopoDS_Face, HDS: TopOpeBRepDS_HDataStructure, orientFORWARD: Optional[bool]) -> None: ...
	def Insert2d(self, S1: TopoDS_Shape, S2: TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def InsertIntersection(self, S1: TopoDS_Shape, S2: TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure, orientFORWARD: Optional[bool]) -> None: ...
	def InsertIntersection2d(self, S1: TopoDS_Shape, S2: TopoDS_Shape, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def IsContext1d(self, S: TopoDS_Shape) -> bool: ...
	def IsMadeOf1d(self, S: TopoDS_Shape) -> bool: ...
	def PShapeClassifier(self) -> TopOpeBRepTool_PShapeClassifier: ...
	def Reducer(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	def RemoveUnsharedGeometry(self, HDS: TopOpeBRepDS_HDataStructure) -> None: ...

class TopOpeBRep_EdgesFiller:
	def __init__(self) -> None: ...
	@overload
	def Face(self, I: int, F: TopoDS_Shape) -> None: ...
	@overload
	def Face(self, I: int) -> TopoDS_Shape: ...
	def Insert(self, E1: TopoDS_Shape, E2: TopoDS_Shape, EI: TopOpeBRep_EdgesIntersector, HDS: TopOpeBRepDS_HDataStructure) -> None: ...

class TopOpeBRep_EdgesIntersector:
	def __init__(self) -> None: ...
	def Curve(self, Index: int) -> Geom2dAdaptor_Curve: ...
	@overload
	def Dimension(self, D: int) -> None: ...
	@overload
	def Dimension(self) -> int: ...
	def Dump(self, str: TCollection_AsciiString, ie1: Optional[int], ie2: Optional[int]) -> None: ...
	def Edge(self, Index: int) -> TopoDS_Shape: ...
	def Face(self, Index: int) -> TopoDS_Shape: ...
	def FacesSameOriented(self) -> bool: ...
	def ForceTolerances(self, Tol1: float, Tol2: float) -> None: ...
	def HasSegment(self) -> bool: ...
	def InitPoint(self, selectkeep: Optional[bool]) -> None: ...
	def IsEmpty(self) -> bool: ...
	def MorePoint(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def NbSegments(self) -> int: ...
	def NextPoint(self) -> None: ...
	def Perform(self, E1: TopoDS_Shape, E2: TopoDS_Shape, ReduceSegments: Optional[bool]) -> None: ...
	@overload
	def Point(self) -> TopOpeBRep_Point2d: ...
	@overload
	def Point(self, I: int) -> TopOpeBRep_Point2d: ...
	def Points(self) -> TopOpeBRep_SequenceOfPoint2d: ...
	def ReduceSegment(self, P1: TopOpeBRep_Point2d, P2: TopOpeBRep_Point2d, Pn: TopOpeBRep_Point2d) -> bool: ...
	def SameDomain(self) -> bool: ...
	@overload
	def SetFaces(self, F1: TopoDS_Shape, F2: TopoDS_Shape) -> None: ...
	@overload
	def SetFaces(self, F1: TopoDS_Shape, F2: TopoDS_Shape, B1: Bnd_Box, B2: Bnd_Box) -> None: ...
	def Status1(self) -> TopOpeBRep_P2Dstatus: ...
	def Surface(self, Index: int) -> BRepAdaptor_Surface: ...
	def SurfacesSameOriented(self) -> bool: ...
	def ToleranceMax(self) -> float: ...
	def Tolerances(self) -> Tuple[float, float]: ...

class TopOpeBRep_FFDumper(Standard_Transient):
	def __init__(self, PFF: TopOpeBRep_PFacesFiller) -> None: ...
	def DumpDSP(self, VP: TopOpeBRep_VPointInter, GK: TopOpeBRepDS_Kind, G: int, newinDS: bool) -> None: ...
	@overload
	def DumpLine(self, I: int) -> None: ...
	@overload
	def DumpLine(self, L: TopOpeBRep_LineInter) -> None: ...
	@overload
	def DumpVP(self, VP: TopOpeBRep_VPointInter) -> None: ...
	@overload
	def DumpVP(self, VP: TopOpeBRep_VPointInter, ISI: int) -> None: ...
	def ExploreIndex(self, S: TopoDS_Shape, ISI: int) -> int: ...
	def Init(self, PFF: TopOpeBRep_PFacesFiller) -> None: ...
	def PFacesFillerDummy(self) -> TopOpeBRep_PFacesFiller: ...

class TopOpeBRep_FFTransitionTool:
	@staticmethod
	def ProcessEdgeONTransition(self, VP: TopOpeBRep_VPointInter, Index: int, R: TopoDS_Shape, E: TopoDS_Shape, F: TopoDS_Shape) -> TopOpeBRepDS_Transition: ...
	@staticmethod
	def ProcessEdgeTransition(self, P: TopOpeBRep_VPointInter, Index: int, LineOrientation: TopAbs_Orientation) -> TopOpeBRepDS_Transition: ...
	@staticmethod
	def ProcessFaceTransition(self, L: TopOpeBRep_LineInter, Index: int, FaceOrientation: TopAbs_Orientation) -> TopOpeBRepDS_Transition: ...
	@overload
	@staticmethod
	def ProcessLineTransition(self, P: TopOpeBRep_VPointInter, Index: int, EdgeOrientation: TopAbs_Orientation) -> TopOpeBRepDS_Transition: ...
	@overload
	@staticmethod
	def ProcessLineTransition(self, P: TopOpeBRep_VPointInter, L: TopOpeBRep_LineInter) -> TopOpeBRepDS_Transition: ...

class TopOpeBRep_FaceEdgeFiller:
	def __init__(self) -> None: ...
	def Insert(self, F: TopoDS_Shape, E: TopoDS_Shape, FEINT: TopOpeBRep_FaceEdgeIntersector, HDS: TopOpeBRepDS_HDataStructure) -> None: ...

class TopOpeBRep_FaceEdgeIntersector:
	def __init__(self) -> None: ...
	def ForceTolerance(self, tol: float) -> None: ...
	def Index(self) -> int: ...
	def InitPoint(self) -> None: ...
	def IsEmpty(self) -> bool: ...
	@overload
	def IsVertex(self, S: TopoDS_Shape, P: gp_Pnt, Tol: float, V: TopoDS_Vertex) -> bool: ...
	@overload
	def IsVertex(self, I: int, V: TopoDS_Vertex) -> bool: ...
	def MorePoint(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def NextPoint(self) -> None: ...
	def Parameter(self) -> float: ...
	def Perform(self, F: TopoDS_Shape, E: TopoDS_Shape) -> None: ...
	def Shape(self, Index: int) -> TopoDS_Shape: ...
	def State(self) -> TopAbs_State: ...
	def Tolerance(self) -> float: ...
	def Transition(self, Index: int, FaceOrientation: TopAbs_Orientation) -> TopOpeBRepDS_Transition: ...
	def UVPoint(self, P: gp_Pnt2d) -> None: ...
	def Value(self) -> gp_Pnt: ...

class TopOpeBRep_FacesFiller:
	def __init__(self) -> None: ...
	def AddShapesLine(self) -> None: ...
	def ChangeDataStructure(self) -> TopOpeBRepDS_DataStructure: ...
	def ChangeFacesIntersector(self) -> TopOpeBRep_FacesIntersector: ...
	def ChangePointClassifier(self) -> TopOpeBRep_PointClassifier: ...
	def CheckLine(self, L: TopOpeBRep_LineInter) -> bool: ...
	@staticmethod
	def EqualpPonR(self, Lrest: TopOpeBRep_LineInter, VP1: TopOpeBRep_VPointInter, VP2: TopOpeBRep_VPointInter) -> bool: ...
	def Face(self, I: int) -> TopoDS_Face: ...
	@overload
	def FaceFaceTransition(self, L: TopOpeBRep_LineInter, I: int) -> TopOpeBRepDS_Transition: ...
	@overload
	def FaceFaceTransition(self, I: int) -> TopOpeBRepDS_Transition: ...
	def FillLine(self) -> None: ...
	def FillLineVPonR(self) -> None: ...
	def GetESL(self, LES: TopTools_ListOfShape) -> None: ...
	@overload
	def GetFFGeometry(self, DSP: TopOpeBRepDS_Point, K: TopOpeBRepDS_Kind) -> Tuple[bool, int]: ...
	@overload
	def GetFFGeometry(self, VP: TopOpeBRep_VPointInter, K: TopOpeBRepDS_Kind) -> Tuple[bool, int]: ...
	def GetGeometry(self, IT: TopOpeBRepDS_ListIteratorOfListOfInterference, VP: TopOpeBRep_VPointInter, K: TopOpeBRepDS_Kind) -> Tuple[bool, int]: ...
	def GetTraceIndex(self) -> Tuple[int, int]: ...
	def HDataStructure(self) -> TopOpeBRepDS_HDataStructure: ...
	def Insert(self, F1: TopoDS_Shape, F2: TopoDS_Shape, FACINT: TopOpeBRep_FacesIntersector, HDS: TopOpeBRepDS_HDataStructure) -> None: ...
	@staticmethod
	def IsVPtransLok(self, L: TopOpeBRep_LineInter, iVP: int, SI12: int, T: TopOpeBRepDS_Transition) -> bool: ...
	@staticmethod
	def LSameDomainERL(self, L: TopOpeBRep_LineInter, ERL: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def Lminmax(self, L: TopOpeBRep_LineInter) -> Tuple[float, float]: ...
	def LoadLine(self, L: TopOpeBRep_LineInter) -> None: ...
	def MakeGeometry(self, VP: TopOpeBRep_VPointInter, ShapeIndex: int, K: TopOpeBRepDS_Kind) -> int: ...
	def PDataStructureDummy(self) -> TopOpeBRepDS_PDataStructure: ...
	def PFacesIntersectorDummy(self) -> TopOpeBRep_PFacesIntersector: ...
	def PLineInterDummy(self) -> TopOpeBRep_PLineInter: ...
	def PShapeClassifier(self) -> TopOpeBRepTool_PShapeClassifier: ...
	def ProcessLine(self) -> None: ...
	def ProcessRLine(self) -> None: ...
	def ProcessSectionEdges(self) -> None: ...
	def ProcessVPInotonR(self, VPI: TopOpeBRep_VPointInterIterator) -> None: ...
	def ProcessVPIonR(self, VPI: TopOpeBRep_VPointInterIterator, trans1: TopOpeBRepDS_Transition, F1: TopoDS_Shape, ShapeIndex: int) -> None: ...
	def ProcessVPR(self, FF: TopOpeBRep_FacesFiller, VP: TopOpeBRep_VPointInter) -> None: ...
	def ProcessVPnotonR(self, VP: TopOpeBRep_VPointInter) -> None: ...
	def ProcessVPonR(self, VP: TopOpeBRep_VPointInter, trans1: TopOpeBRepDS_Transition, F1: TopoDS_Shape, ShapeIndex: int) -> None: ...
	def ProcessVPonclosingR(self, VP: TopOpeBRep_VPointInter, F1: TopoDS_Shape, ShapeIndex: int, transEdge: TopOpeBRepDS_Transition, PVKind: TopOpeBRepDS_Kind, PVIndex: int, EPIfound: bool, IEPI: TopOpeBRepDS_Interference) -> None: ...
	def ProcessVPondgE(self, VP: TopOpeBRep_VPointInter, ShapeIndex: int, PVKind: TopOpeBRepDS_Kind, IEPI: TopOpeBRepDS_Interference, ICPI: TopOpeBRepDS_Interference) -> Tuple[bool, int, bool, bool]: ...
	def ResetDSC(self) -> None: ...
	def SetPShapeClassifier(self, PSC: TopOpeBRepTool_PShapeClassifier) -> None: ...
	def SetTraceIndex(self, exF1: int, exF2: int) -> None: ...
	def StoreCurveInterference(self, I: TopOpeBRepDS_Interference) -> None: ...
	@staticmethod
	def TransvpOK(self, L: TopOpeBRep_LineInter, iVP: int, SI: int, isINOUT: bool) -> bool: ...
	@staticmethod
	def VPParamOnER(self, vp: TopOpeBRep_VPointInter, Lrest: TopOpeBRep_LineInter) -> float: ...
	@overload
	def VP_Position(self, FACINT: TopOpeBRep_FacesIntersector) -> None: ...
	@overload
	def VP_Position(self, L: TopOpeBRep_LineInter) -> None: ...
	@overload
	def VP_Position(self, VP: TopOpeBRep_VPointInter, VPC: TopOpeBRep_VPointInterClassifier) -> None: ...
	def VP_PositionOnL(self, L: TopOpeBRep_LineInter) -> None: ...
	def VP_PositionOnR(self, L: TopOpeBRep_LineInter) -> None: ...

class TopOpeBRep_FacesIntersector:
	def __init__(self) -> None: ...
	def ChangeLine(self, IL: int) -> TopOpeBRep_LineInter: ...
	def CurrentLine(self) -> TopOpeBRep_LineInter: ...
	def CurrentLineIndex(self) -> int: ...
	def Face(self, Index: int) -> TopoDS_Shape: ...
	def ForceTolerances(self, tolarc: float, toltang: float) -> None: ...
	def GetTolerances(self) -> Tuple[float, float]: ...
	def InitLine(self) -> None: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsRestriction(self, E: TopoDS_Shape) -> bool: ...
	def Lines(self) -> TopOpeBRep_HArray1OfLineInter: ...
	def MoreLine(self) -> bool: ...
	def NbLines(self) -> int: ...
	def NextLine(self) -> None: ...
	@overload
	def Perform(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
	@overload
	def Perform(self, S1: TopoDS_Shape, S2: TopoDS_Shape, B1: Bnd_Box, B2: Bnd_Box) -> None: ...
	def PrepareLines(self) -> None: ...
	def Restrictions(self) -> TopTools_IndexedMapOfShape: ...
	def SameDomain(self) -> bool: ...
	def SurfacesSameOriented(self) -> bool: ...

class TopOpeBRep_GeomTool:
	@staticmethod
	def MakeBSpline1fromWALKING2d(self, L: TopOpeBRep_LineInter, SI: int) -> Geom2d_Curve: ...
	@staticmethod
	def MakeBSpline1fromWALKING3d(self, L: TopOpeBRep_LineInter) -> Geom_Curve: ...
	@staticmethod
	def MakeCurve(self, min: float, max: float, L: TopOpeBRep_LineInter, C: Geom_Curve) -> None: ...
	@staticmethod
	def MakeCurves(self, min: float, max: float, L: TopOpeBRep_LineInter, S1: TopoDS_Shape, S2: TopoDS_Shape, C: TopOpeBRepDS_Curve, PC1: Geom2d_Curve, PC2: Geom2d_Curve) -> None: ...

class TopOpeBRep_Hctxee2d(Standard_Transient):
	def __init__(self) -> None: ...
	def Curve(self, I: int) -> Geom2dAdaptor_Curve: ...
	def Domain(self, I: int) -> IntRes2d_Domain: ...
	def Edge(self, I: int) -> TopoDS_Shape: ...
	def SetEdges(self, E1: TopoDS_Edge, E2: TopoDS_Edge, BAS1: BRepAdaptor_Surface, BAS2: BRepAdaptor_Surface) -> None: ...

class TopOpeBRep_Hctxff2d(Standard_Transient):
	def __init__(self) -> None: ...
	def Face(self, I: int) -> TopoDS_Face: ...
	def FaceSameOrientedWithRef(self, I: int) -> bool: ...
	def FacesSameOriented(self) -> bool: ...
	def GetMaxTolerance(self) -> float: ...
	def GetTolerances(self) -> Tuple[float, float]: ...
	def HSurface(self, I: int) -> BRepAdaptor_HSurface: ...
	def SetFaces(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
	def SetHSurfaces(self, S1: BRepAdaptor_HSurface, S2: BRepAdaptor_HSurface) -> None: ...
	def SetTolerances(self, Tol1: float, Tol2: float) -> None: ...
	def SurfacesSameOriented(self) -> bool: ...

class TopOpeBRep_LineInter:
	def __init__(self) -> None: ...
	def Arc(self) -> TopoDS_Shape: ...
	def ArcIsEdge(self, I: int) -> bool: ...
	def Bounds(self) -> Tuple[float, float]: ...
	def ChangeVPoint(self, I: int) -> TopOpeBRep_VPointInter: ...
	def ComputeFaceFaceTransition(self) -> None: ...
	@overload
	def Curve(self) -> Geom_Curve: ...
	@overload
	def Curve(self, parmin: float, parmax: float) -> Geom_Curve: ...
	def DumpBipoint(self, B: TopOpeBRep_Bipoint, s1: TCollection_AsciiString, s2: TCollection_AsciiString) -> None: ...
	def DumpType(self) -> None: ...
	def DumpVPoint(self, I: int, s1: TCollection_AsciiString, s2: TCollection_AsciiString) -> None: ...
	def FaceFaceTransition(self, I: int) -> TopOpeBRepDS_Transition: ...
	def GetTraceIndex(self) -> Tuple[int, int]: ...
	def HasFirstPoint(self) -> bool: ...
	def HasLastPoint(self) -> bool: ...
	def HasVInternal(self) -> bool: ...
	def HasVPonR(self) -> bool: ...
	def INL(self) -> bool: ...
	@overload
	def Index(self, I: int) -> None: ...
	@overload
	def Index(self) -> int: ...
	def IsPeriodic(self) -> bool: ...
	def IsVClosed(self) -> bool: ...
	def LineG(self) -> IntPatch_GLine: ...
	def LineR(self) -> IntPatch_RLine: ...
	def LineW(self) -> IntPatch_WLine: ...
	def NbVPoint(self) -> int: ...
	def NbWPoint(self) -> int: ...
	def OK(self) -> bool: ...
	def Period(self) -> float: ...
	def SetFaces(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
	def SetHasVPonR(self) -> None: ...
	def SetINL(self) -> None: ...
	def SetIsVClosed(self) -> None: ...
	def SetLine(self, L: IntPatch_Line, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface) -> None: ...
	def SetOK(self, B: bool) -> None: ...
	def SetTraceIndex(self, exF1: int, exF2: int) -> None: ...
	def SetVPBounds(self) -> None: ...
	def SituationS1(self) -> IntSurf_Situation: ...
	def SituationS2(self) -> IntSurf_Situation: ...
	def TransitionOnS1(self) -> IntSurf_TypeTrans: ...
	def TransitionOnS2(self) -> IntSurf_TypeTrans: ...
	def TypeLineCurve(self) -> TopOpeBRep_TypeLineCurve: ...
	def VPBounds(self) -> Tuple[int, int, int]: ...
	def VPoint(self, I: int) -> TopOpeBRep_VPointInter: ...
	def WPoint(self, I: int) -> TopOpeBRep_WPointInter: ...

class TopOpeBRep_Point2d:
	def __init__(self) -> None: ...
	def ChangeTransition(self, I: int) -> TopOpeBRepDS_Transition: ...
	def Dump(self, ie1: Optional[int], ie2: Optional[int]) -> None: ...
	def EdgesConfig(self) -> TopOpeBRepDS_Config: ...
	def HasPint(self) -> bool: ...
	def Hctxee2d(self) -> TopOpeBRep_Hctxee2d: ...
	def Hctxff2d(self) -> TopOpeBRep_Hctxff2d: ...
	def Index(self) -> int: ...
	def IsPointOfSegment(self) -> bool: ...
	def IsVertex(self, I: int) -> bool: ...
	def Keep(self) -> bool: ...
	def Parameter(self, I: int) -> float: ...
	def Pint(self) -> IntRes2d_IntersectionPoint: ...
	def SegmentAncestors(self) -> Tuple[bool, int, int]: ...
	def SetEdgesConfig(self, C: TopOpeBRepDS_Config) -> None: ...
	def SetHctxee2d(self, ee2d: TopOpeBRep_Hctxee2d) -> None: ...
	def SetHctxff2d(self, ff2d: TopOpeBRep_Hctxff2d) -> None: ...
	def SetIndex(self, X: int) -> None: ...
	def SetIsPointOfSegment(self, B: bool) -> None: ...
	def SetIsVertex(self, I: int, B: bool) -> None: ...
	def SetKeep(self, B: bool) -> None: ...
	def SetParameter(self, I: int, P: float) -> None: ...
	def SetPint(self, P: IntRes2d_IntersectionPoint) -> None: ...
	def SetSegmentAncestors(self, IP1: int, IP2: int) -> None: ...
	def SetStatus(self, S: TopOpeBRep_P2Dstatus) -> None: ...
	def SetTolerance(self, T: float) -> None: ...
	def SetTransition(self, I: int, T: TopOpeBRepDS_Transition) -> None: ...
	def SetValue(self, P: gp_Pnt) -> None: ...
	def SetValue2d(self, P: gp_Pnt2d) -> None: ...
	def SetVertex(self, I: int, V: TopoDS_Vertex) -> None: ...
	def Status(self) -> TopOpeBRep_P2Dstatus: ...
	def Tolerance(self) -> float: ...
	def Transition(self, I: int) -> TopOpeBRepDS_Transition: ...
	def Value(self) -> gp_Pnt: ...
	def Value2d(self) -> gp_Pnt2d: ...
	def Vertex(self, I: int) -> TopoDS_Vertex: ...

class TopOpeBRep_PointClassifier:
	def __init__(self) -> None: ...
	def Classify(self, F: TopoDS_Face, P: gp_Pnt2d, Tol: float) -> TopAbs_State: ...
	def Init(self) -> None: ...
	def Load(self, F: TopoDS_Face) -> None: ...
	def State(self) -> TopAbs_State: ...

class TopOpeBRep_PointGeomTool:
	@staticmethod
	def IsEqual(self, DSP1: TopOpeBRepDS_Point, DSP2: TopOpeBRepDS_Point) -> bool: ...
	@overload
	@staticmethod
	def MakePoint(self, IP: TopOpeBRep_VPointInter) -> TopOpeBRepDS_Point: ...
	@overload
	@staticmethod
	def MakePoint(self, P2D: TopOpeBRep_Point2d) -> TopOpeBRepDS_Point: ...
	@overload
	@staticmethod
	def MakePoint(self, FEI: TopOpeBRep_FaceEdgeIntersector) -> TopOpeBRepDS_Point: ...
	@overload
	@staticmethod
	def MakePoint(self, S: TopoDS_Shape) -> TopOpeBRepDS_Point: ...

class TopOpeBRep_ShapeIntersector:
	def __init__(self) -> None: ...
	def ChangeEdgesIntersector(self) -> TopOpeBRep_EdgesIntersector: ...
	def ChangeFaceEdgeIntersector(self) -> TopOpeBRep_FaceEdgeIntersector: ...
	def ChangeFacesIntersector(self) -> TopOpeBRep_FacesIntersector: ...
	def CurrentGeomShape(self, Index: int) -> TopoDS_Shape: ...
	def DumpCurrent(self, K: int) -> None: ...
	def GetTolerances(self) -> Tuple[float, float]: ...
	def Index(self, K: int) -> int: ...
	@overload
	def InitIntersection(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
	@overload
	def InitIntersection(self, S1: TopoDS_Shape, S2: TopoDS_Shape, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
	def MoreIntersection(self) -> bool: ...
	def NextIntersection(self) -> None: ...
	def RejectedFaces(self, anObj: TopoDS_Shape, aReference: TopoDS_Shape, aListOfShape: TopTools_ListOfShape) -> None: ...
	def Shape(self, Index: int) -> TopoDS_Shape: ...

class TopOpeBRep_ShapeIntersector2d:
	def __init__(self) -> None: ...
	def ChangeEdgesIntersector(self) -> TopOpeBRep_EdgesIntersector: ...
	def CurrentGeomShape(self, Index: int) -> TopoDS_Shape: ...
	def DumpCurrent(self, K: int) -> None: ...
	def Index(self, K: int) -> int: ...
	def InitIntersection(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
	def MoreIntersection(self) -> bool: ...
	def NextIntersection(self) -> None: ...
	def Shape(self, Index: int) -> TopoDS_Shape: ...

class TopOpeBRep_ShapeScanner:
	def __init__(self) -> None: ...
	def AddBoxesMakeCOB(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum]) -> None: ...
	def BoxSort(self) -> TopOpeBRepTool_BoxSort: ...
	def ChangeBoxSort(self) -> TopOpeBRepTool_BoxSort: ...
	def Clear(self) -> None: ...
	def Current(self) -> TopoDS_Shape: ...
	def Index(self) -> int: ...
	@overload
	def Init(self, E: TopoDS_Shape) -> None: ...
	@overload
	def Init(self, X: TopOpeBRepTool_ShapeExplorer) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...

class TopOpeBRep_VPointInter:
	def __init__(self) -> None: ...
	def ArcOnS1(self) -> TopoDS_Shape: ...
	def ArcOnS2(self) -> TopoDS_Shape: ...
	def ChangeKeep(self, keep: bool) -> None: ...
	def Edge(self, I: int) -> TopoDS_Shape: ...
	@overload
	def EdgeON(self, Eon: TopoDS_Shape, Par: float, I: int) -> None: ...
	@overload
	def EdgeON(self, I: int) -> TopoDS_Shape: ...
	def EdgeONParameter(self, I: int) -> float: ...
	def EdgeParameter(self, I: int) -> float: ...
	def EqualpP(self, VP: TopOpeBRep_VPointInter) -> bool: ...
	def GetShapes(self) -> Tuple[int, int]: ...
	@overload
	def Index(self, I: int) -> None: ...
	@overload
	def Index(self) -> int: ...
	def IsInternal(self) -> bool: ...
	def IsMultiple(self) -> bool: ...
	def IsOnDomS1(self) -> bool: ...
	def IsOnDomS2(self) -> bool: ...
	def IsVertex(self, I: int) -> bool: ...
	def IsVertexOnS1(self) -> bool: ...
	def IsVertexOnS2(self) -> bool: ...
	def Keep(self) -> bool: ...
	def PThePointOfIntersectionDummy(self) -> TopOpeBRep_PThePointOfIntersection: ...
	def ParameterOnArc1(self) -> float: ...
	def ParameterOnArc2(self) -> float: ...
	def ParameterOnLine(self) -> float: ...
	def ParametersOnS1(self) -> Tuple[float, float]: ...
	def ParametersOnS2(self) -> Tuple[float, float]: ...
	def ParonE(self, E: TopoDS_Edge) -> Tuple[bool, float]: ...
	def SetPoint(self, P: IntPatch_Point) -> None: ...
	def SetShapes(self, I1: int, I2: int) -> None: ...
	@overload
	def ShapeIndex(self) -> int: ...
	@overload
	def ShapeIndex(self, I: int) -> None: ...
	@overload
	def State(self, I: int) -> TopAbs_State: ...
	@overload
	def State(self, S: TopAbs_State, I: int) -> None: ...
	def SurfaceParameters(self, I: int) -> gp_Pnt2d: ...
	def Tolerance(self) -> float: ...
	def TransitionLineArc1(self) -> IntSurf_Transition: ...
	def TransitionLineArc2(self) -> IntSurf_Transition: ...
	def TransitionOnS1(self) -> IntSurf_Transition: ...
	def TransitionOnS2(self) -> IntSurf_Transition: ...
	def UpdateKeep(self) -> None: ...
	def Value(self) -> gp_Pnt: ...
	def Vertex(self, I: int) -> TopoDS_Shape: ...
	def VertexOnS1(self) -> TopoDS_Shape: ...
	def VertexOnS2(self) -> TopoDS_Shape: ...

class TopOpeBRep_VPointInterClassifier:
	def __init__(self) -> None: ...
	def Edge(self) -> TopoDS_Shape: ...
	def EdgeParameter(self) -> float: ...
	def VPointPosition(self, F: TopoDS_Shape, VP: TopOpeBRep_VPointInter, ShapeIndex: int, PC: TopOpeBRep_PointClassifier, AssumeINON: bool, Tol: float) -> TopAbs_State: ...

class TopOpeBRep_VPointInterIterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, LI: TopOpeBRep_LineInter) -> None: ...
	def ChangeCurrentVP(self) -> TopOpeBRep_VPointInter: ...
	def CurrentVP(self) -> TopOpeBRep_VPointInter: ...
	def CurrentVPIndex(self) -> int: ...
	@overload
	def Init(self, LI: TopOpeBRep_LineInter, checkkeep: Optional[bool]) -> None: ...
	@overload
	def Init(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def PLineInterDummy(self) -> TopOpeBRep_PLineInter: ...

class TopOpeBRep_WPointInter:
	def __init__(self) -> None: ...
	def PPntOn2SDummy(self) -> TopOpeBRep_PPntOn2S: ...
	def Parameters(self) -> Tuple[float, float, float, float]: ...
	def ParametersOnS1(self) -> Tuple[float, float]: ...
	def ParametersOnS2(self) -> Tuple[float, float]: ...
	def Set(self, P: IntSurf_PntOn2S) -> None: ...
	def Value(self) -> gp_Pnt: ...
	def ValueOnS1(self) -> gp_Pnt2d: ...
	def ValueOnS2(self) -> gp_Pnt2d: ...

class TopOpeBRep_WPointInterIterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, LI: TopOpeBRep_LineInter) -> None: ...
	def CurrentWP(self) -> TopOpeBRep_WPointInter: ...
	@overload
	def Init(self, LI: TopOpeBRep_LineInter) -> None: ...
	@overload
	def Init(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def PLineInterDummy(self) -> TopOpeBRep_PLineInter: ...

#classnotwrapped
class TopOpeBRep_traceSIFF: ...

# harray1 classes

class TopOpeBRep_HArray1OfVPointInter(TopOpeBRep_Array1OfVPointInter, Standard_Transient):
    def TopOpeBRep_HArray1OfVPointInter(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TopOpeBRep_Array1OfVPointInter: ...


class TopOpeBRep_HArray1OfLineInter(TopOpeBRep_Array1OfLineInter, Standard_Transient):
    def TopOpeBRep_HArray1OfLineInter(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> TopOpeBRep_Array1OfLineInter: ...

# harray2 classes
# hsequence classes

topopebrep_Print = topopebrep.Print
TopOpeBRep_FFTransitionTool_ProcessEdgeONTransition = TopOpeBRep_FFTransitionTool.ProcessEdgeONTransition
TopOpeBRep_FFTransitionTool_ProcessEdgeTransition = TopOpeBRep_FFTransitionTool.ProcessEdgeTransition
TopOpeBRep_FFTransitionTool_ProcessFaceTransition = TopOpeBRep_FFTransitionTool.ProcessFaceTransition
TopOpeBRep_FFTransitionTool_ProcessLineTransition = TopOpeBRep_FFTransitionTool.ProcessLineTransition
TopOpeBRep_FFTransitionTool_ProcessLineTransition = TopOpeBRep_FFTransitionTool.ProcessLineTransition
TopOpeBRep_FacesFiller_EqualpPonR = TopOpeBRep_FacesFiller.EqualpPonR
TopOpeBRep_FacesFiller_IsVPtransLok = TopOpeBRep_FacesFiller.IsVPtransLok
TopOpeBRep_FacesFiller_LSameDomainERL = TopOpeBRep_FacesFiller.LSameDomainERL
TopOpeBRep_FacesFiller_Lminmax = TopOpeBRep_FacesFiller.Lminmax
TopOpeBRep_FacesFiller_TransvpOK = TopOpeBRep_FacesFiller.TransvpOK
TopOpeBRep_FacesFiller_VPParamOnER = TopOpeBRep_FacesFiller.VPParamOnER
TopOpeBRep_GeomTool_MakeBSpline1fromWALKING2d = TopOpeBRep_GeomTool.MakeBSpline1fromWALKING2d
TopOpeBRep_GeomTool_MakeBSpline1fromWALKING3d = TopOpeBRep_GeomTool.MakeBSpline1fromWALKING3d
TopOpeBRep_GeomTool_MakeCurve = TopOpeBRep_GeomTool.MakeCurve
TopOpeBRep_GeomTool_MakeCurves = TopOpeBRep_GeomTool.MakeCurves
TopOpeBRep_PointGeomTool_IsEqual = TopOpeBRep_PointGeomTool.IsEqual
TopOpeBRep_PointGeomTool_MakePoint = TopOpeBRep_PointGeomTool.MakePoint
TopOpeBRep_PointGeomTool_MakePoint = TopOpeBRep_PointGeomTool.MakePoint
TopOpeBRep_PointGeomTool_MakePoint = TopOpeBRep_PointGeomTool.MakePoint
TopOpeBRep_PointGeomTool_MakePoint = TopOpeBRep_PointGeomTool.MakePoint
