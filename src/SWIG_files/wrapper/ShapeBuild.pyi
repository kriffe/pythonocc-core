from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.TopoDS import *
from OCC.Core.TopLoc import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.BRepTools import *
from OCC.Core.TopAbs import *
from OCC.Core.ShapeExtend import *


class ShapeBuild:
	@staticmethod
	def PlaneXOY(self) -> Geom_Plane: ...

class ShapeBuild_Edge:
	def BuildCurve3d(self, edge: TopoDS_Edge) -> bool: ...
	def Copy(self, edge: TopoDS_Edge, sharepcurves: Optional[bool]) -> TopoDS_Edge: ...
	def CopyPCurves(self, toedge: TopoDS_Edge, fromedge: TopoDS_Edge) -> None: ...
	def CopyRanges(self, toedge: TopoDS_Edge, fromedge: TopoDS_Edge, alpha: Optional[float], beta: Optional[float]) -> None: ...
	def CopyReplaceVertices(self, edge: TopoDS_Edge, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> TopoDS_Edge: ...
	@overload
	def MakeEdge(self, edge: TopoDS_Edge, curve: Geom_Curve, L: TopLoc_Location) -> None: ...
	@overload
	def MakeEdge(self, edge: TopoDS_Edge, curve: Geom_Curve, L: TopLoc_Location, p1: float, p2: float) -> None: ...
	@overload
	def MakeEdge(self, edge: TopoDS_Edge, pcurve: Geom2d_Curve, face: TopoDS_Face) -> None: ...
	@overload
	def MakeEdge(self, edge: TopoDS_Edge, pcurve: Geom2d_Curve, face: TopoDS_Face, p1: float, p2: float) -> None: ...
	@overload
	def MakeEdge(self, edge: TopoDS_Edge, pcurve: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	@overload
	def MakeEdge(self, edge: TopoDS_Edge, pcurve: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location, p1: float, p2: float) -> None: ...
	def ReassignPCurve(self, edge: TopoDS_Edge, old: TopoDS_Face, sub: TopoDS_Face) -> bool: ...
	def RemoveCurve3d(self, edge: TopoDS_Edge) -> None: ...
	@overload
	def RemovePCurve(self, edge: TopoDS_Edge, face: TopoDS_Face) -> None: ...
	@overload
	def RemovePCurve(self, edge: TopoDS_Edge, surf: Geom_Surface) -> None: ...
	@overload
	def RemovePCurve(self, edge: TopoDS_Edge, surf: Geom_Surface, loc: TopLoc_Location) -> None: ...
	def ReplacePCurve(self, edge: TopoDS_Edge, pcurve: Geom2d_Curve, face: TopoDS_Face) -> None: ...
	def SetRange3d(self, edge: TopoDS_Edge, first: float, last: float) -> None: ...
	def TransformPCurve(self, pcurve: Geom2d_Curve, trans: gp_Trsf2d, uFact: float) -> Tuple[Geom2d_Curve, float, float]: ...

class ShapeBuild_ReShape(BRepTools_ReShape):
	def __init__(self) -> None: ...
	@overload
	def Apply(self, shape: TopoDS_Shape, until: TopAbs_ShapeEnum, buildmode: int) -> TopoDS_Shape: ...
	@overload
	def Apply(self, shape: TopoDS_Shape, until: Optional[TopAbs_ShapeEnum]) -> TopoDS_Shape: ...
	@overload
	def Status(self, shape: TopoDS_Shape, newsh: TopoDS_Shape, last: Optional[bool]) -> int: ...
	@overload
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeBuild_Vertex:
	@overload
	def CombineVertex(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex, tolFactor: Optional[float]) -> TopoDS_Vertex: ...
	@overload
	def CombineVertex(self, pnt1: gp_Pnt, pnt2: gp_Pnt, tol1: float, tol2: float, tolFactor: Optional[float]) -> TopoDS_Vertex: ...

# harray1 classes
# harray2 classes
# harray2 classes

shapebuild_PlaneXOY = shapebuild.PlaneXOY
