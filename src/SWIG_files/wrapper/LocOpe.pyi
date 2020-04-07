from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TColgp import *
from OCC.Core.TopTools import *
from OCC.Core.TopAbs import *
from OCC.Core.TColGeom import *
from OCC.Core.gp import *
from OCC.Core.Geom import *


class LocOpe_Operation:
	LocOpe_FUSE: int = ...
	LocOpe_CUT: int = ...
	LocOpe_INVALID: int = ...

class LocOpe:
	@staticmethod
	def Closed(self, W: TopoDS_Wire, OnF: TopoDS_Face) -> bool: ...
	@staticmethod
	def Closed(self, E: TopoDS_Edge, OnF: TopoDS_Face) -> bool: ...
	@staticmethod
	def SampleEdges(self, S: TopoDS_Shape, Pt: TColgp_SequenceOfPnt) -> None: ...
	@staticmethod
	def TgtFaces(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face) -> bool: ...

class LocOpe_BuildShape:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, L: TopTools_ListOfShape) -> None: ...
	def Perform(self, L: TopTools_ListOfShape) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class LocOpe_BuildWires:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Ledges: TopTools_ListOfShape, PW: LocOpe_WiresOnShape) -> None: ...
	def IsDone(self) -> bool: ...
	def Perform(self, Ledges: TopTools_ListOfShape, PW: LocOpe_WiresOnShape) -> None: ...
	def Result(self) -> TopTools_ListOfShape: ...

class LocOpe_CSIntersector:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Destroy(self) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def LocalizeAfter(self, I: int, From: float, Tol: float, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def LocalizeAfter(self, I: int, FromInd: int, Tol: float, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def LocalizeBefore(self, I: int, From: float, Tol: float, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def LocalizeBefore(self, I: int, FromInd: int, Tol: float, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def NbPoints(self, I: int) -> int: ...
	def Perform(self, Slin: LocOpe_SequenceOfLin) -> None: ...
	def Perform(self, Scir: LocOpe_SequenceOfCirc) -> None: ...
	def Perform(self, Scur: TColGeom_SequenceOfCurve) -> None: ...
	def Point(self, I: int, Index: int) -> LocOpe_PntFace: ...

class LocOpe_CurveShapeIntersector:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Axis: gp_Ax1, S: TopoDS_Shape) -> None: ...
	@overload
	def __init__(self, C: gp_Circ, S: TopoDS_Shape) -> None: ...
	def Init(self, Axis: gp_Ax1, S: TopoDS_Shape) -> None: ...
	def Init(self, C: gp_Circ, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def LocalizeAfter(self, From: float, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def LocalizeAfter(self, FromInd: int, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def LocalizeBefore(self, From: float, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def LocalizeBefore(self, FromInd: int, Or: TopAbs_Orientation) -> Tuple[bool, int, int]: ...
	def NbPoints(self) -> int: ...
	def Point(self, Index: int) -> LocOpe_PntFace: ...

class LocOpe_DPrism:
	@overload
	def __init__(self, Spine: TopoDS_Face, Height1: float, Height2: float, Angle: float) -> None: ...
	@overload
	def __init__(self, Spine: TopoDS_Face, Height: float, Angle: float) -> None: ...
	def BarycCurve(self) -> Geom_Curve: ...
	def Curves(self, SCurves: TColGeom_SequenceOfCurve) -> None: ...
	def FirstShape(self) -> TopoDS_Shape: ...
	def IsDone(self) -> bool: ...
	def LastShape(self) -> TopoDS_Shape: ...
	def Profile(self) -> TopoDS_Shape: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Shapes(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Spine(self) -> TopoDS_Shape: ...

class LocOpe_FindEdges:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, FFrom: TopoDS_Shape, FTo: TopoDS_Shape) -> None: ...
	def EdgeFrom(self) -> TopoDS_Edge: ...
	def EdgeTo(self) -> TopoDS_Edge: ...
	def InitIterator(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Set(self, FFrom: TopoDS_Shape, FTo: TopoDS_Shape) -> None: ...

class LocOpe_FindEdgesInFace:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, F: TopoDS_Face) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Init(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Set(self, S: TopoDS_Shape, F: TopoDS_Face) -> None: ...

class LocOpe_GeneratedShape(Standard_Transient):
	def Generated(self, V: TopoDS_Vertex) -> TopoDS_Edge: ...
	def Generated(self, E: TopoDS_Edge) -> TopoDS_Face: ...
	def GeneratingEdges(self) -> TopTools_ListOfShape: ...
	def OrientedFaces(self) -> TopTools_ListOfShape: ...

class LocOpe_Generator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def DescendantFace(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def Perform(self, G: LocOpe_GeneratedShape) -> None: ...
	def ResultingShape(self) -> TopoDS_Shape: ...
	def Shape(self) -> TopoDS_Shape: ...

class LocOpe_Gluer:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Sbase: TopoDS_Shape, Snew: TopoDS_Shape) -> None: ...
	def BasisShape(self) -> TopoDS_Shape: ...
	def Bind(self, Fnew: TopoDS_Face, Fbase: TopoDS_Face) -> None: ...
	def Bind(self, Enew: TopoDS_Edge, Ebase: TopoDS_Edge) -> None: ...
	def DescendantFaces(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def Edges(self) -> TopTools_ListOfShape: ...
	def GluedShape(self) -> TopoDS_Shape: ...
	def Init(self, Sbase: TopoDS_Shape, Snew: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def OpeType(self) -> LocOpe_Operation: ...
	def Perform(self) -> None: ...
	def ResultingShape(self) -> TopoDS_Shape: ...
	def TgtEdges(self) -> TopTools_ListOfShape: ...

class LocOpe_LinearForm:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Base: TopoDS_Shape, V: gp_Vec, Pnt1: gp_Pnt, Pnt2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, Base: TopoDS_Shape, V: gp_Vec, Vectra: gp_Vec, Pnt1: gp_Pnt, Pnt2: gp_Pnt) -> None: ...
	def FirstShape(self) -> TopoDS_Shape: ...
	def LastShape(self) -> TopoDS_Shape: ...
	def Perform(self, Base: TopoDS_Shape, V: gp_Vec, Pnt1: gp_Pnt, Pnt2: gp_Pnt) -> None: ...
	def Perform(self, Base: TopoDS_Shape, V: gp_Vec, Vectra: gp_Vec, Pnt1: gp_Pnt, Pnt2: gp_Pnt) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Shapes(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...

class LocOpe_Pipe:
	def __init__(self, Spine: TopoDS_Wire, Profile: TopoDS_Shape) -> None: ...
	def BarycCurve(self) -> Geom_Curve: ...
	def Curves(self, Spt: TColgp_SequenceOfPnt) -> TColGeom_SequenceOfCurve: ...
	def FirstShape(self) -> TopoDS_Shape: ...
	def LastShape(self) -> TopoDS_Shape: ...
	def Profile(self) -> TopoDS_Shape: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Shapes(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Spine(self) -> TopoDS_Shape: ...

class LocOpe_PntFace:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P: gp_Pnt, F: TopoDS_Face, Or: TopAbs_Orientation, Param: float, UPar: float, VPar: float) -> None: ...
	def ChangeOrientation(self) -> TopAbs_Orientation: ...
	def Face(self) -> TopoDS_Face: ...
	def Orientation(self) -> TopAbs_Orientation: ...
	def Parameter(self) -> float: ...
	def Pnt(self) -> gp_Pnt: ...
	def UParameter(self) -> float: ...
	def VParameter(self) -> float: ...

class LocOpe_Prism:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Base: TopoDS_Shape, V: gp_Vec) -> None: ...
	@overload
	def __init__(self, Base: TopoDS_Shape, V: gp_Vec, Vectra: gp_Vec) -> None: ...
	def BarycCurve(self) -> Geom_Curve: ...
	def Curves(self, SCurves: TColGeom_SequenceOfCurve) -> None: ...
	def FirstShape(self) -> TopoDS_Shape: ...
	def LastShape(self) -> TopoDS_Shape: ...
	def Perform(self, Base: TopoDS_Shape, V: gp_Vec) -> None: ...
	def Perform(self, Base: TopoDS_Shape, V: gp_Vec, Vtra: gp_Vec) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Shapes(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...

class LocOpe_SplitDrafts:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def OriginalShape(self) -> TopoDS_Shape: ...
	def Perform(self, F: TopoDS_Face, W: TopoDS_Wire, Extractg: gp_Dir, NPlg: gp_Pln, Angleg: float, Extractd: gp_Dir, NPld: gp_Pln, Angled: float, ModifyLeft: Optional[bool], ModifyRight: Optional[bool]) -> None: ...
	def Perform(self, F: TopoDS_Face, W: TopoDS_Wire, Extract: gp_Dir, NPl: gp_Pln, Angle: float) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def ShapesFromShape(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...

class LocOpe_SplitShape:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Add(self, V: TopoDS_Vertex, P: float, E: TopoDS_Edge) -> None: ...
	def Add(self, W: TopoDS_Wire, F: TopoDS_Face) -> bool: ...
	def Add(self, Lwires: TopTools_ListOfShape, F: TopoDS_Face) -> bool: ...
	def CanSplit(self, E: TopoDS_Edge) -> bool: ...
	def DescendantShapes(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def LeftOf(self, W: TopoDS_Wire, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def Shape(self) -> TopoDS_Shape: ...

class LocOpe_Spliter:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def DescendantShapes(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def DirectLeft(self) -> TopTools_ListOfShape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def Left(self) -> TopTools_ListOfShape: ...
	def Perform(self, PW: LocOpe_WiresOnShape) -> None: ...
	def ResultingShape(self) -> TopoDS_Shape: ...
	def Shape(self) -> TopoDS_Shape: ...

class LocOpe_WiresOnShape(Standard_Transient):
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Add(self, theEdges: TopTools_SequenceOfShape) -> bool: ...
	def Bind(self, W: TopoDS_Wire, F: TopoDS_Face) -> None: ...
	def Bind(self, Comp: TopoDS_Compound, F: TopoDS_Face) -> None: ...
	def Bind(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def Bind(self, EfromW: TopoDS_Edge, EonFace: TopoDS_Edge) -> None: ...
	def BindAll(self) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def InitEdgeIterator(self) -> None: ...
	def IsDone(self) -> bool: ...
	def IsFaceWithSection(self, aFace: TopoDS_Shape) -> bool: ...
	def MoreEdge(self) -> bool: ...
	def NextEdge(self) -> None: ...
	def OnEdge(self, E: TopoDS_Edge) -> bool: ...
	def OnEdge(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float]: ...
	def OnEdge(self, V: TopoDS_Vertex, EdgeFrom: TopoDS_Edge, E: TopoDS_Edge) -> Tuple[bool, float]: ...
	def OnFace(self) -> TopoDS_Face: ...
	def OnVertex(self, Vwire: TopoDS_Vertex, Vshape: TopoDS_Vertex) -> bool: ...
	def SetCheckInterior(self, ToCheckInterior: bool) -> None: ...

class LocOpe_GluedShape(LocOpe_GeneratedShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Generated(self, V: TopoDS_Vertex) -> TopoDS_Edge: ...
	def Generated(self, E: TopoDS_Edge) -> TopoDS_Face: ...
	def GeneratingEdges(self) -> TopTools_ListOfShape: ...
	def GlueOnFace(self, F: TopoDS_Face) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def OrientedFaces(self) -> TopTools_ListOfShape: ...

#classnotwrapped
class LocOpe_Revol:
	pass

#classnotwrapped
class LocOpe_RevolutionForm:
	pass
