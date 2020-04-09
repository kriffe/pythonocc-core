from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.gp import *
from OCC.Core.IntRes2d import *
from OCC.Core.Geom2dInt import *


class BRepClass_Edge:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	@overload
	def Edge(self) -> TopoDS_Edge: ...
	@overload
	def Edge(self) -> TopoDS_Edge: ...
	@overload
	def Face(self) -> TopoDS_Face: ...
	@overload
	def Face(self) -> TopoDS_Face: ...

class BRepClass_FClass2dOfFClassifier:
	def __init__(self) -> None: ...
	def ClosestIntersection(self) -> int: ...
	def Compare(self, E: BRepClass_Edge, Or: TopAbs_Orientation) -> None: ...
	def Intersector(self) -> BRepClass_Intersector: ...
	def IsHeadOrEnd(self) -> bool: ...
	def Parameter(self) -> float: ...
	def Reset(self, L: gp_Lin2d, P: float, Tol: float) -> None: ...
	def State(self) -> TopAbs_State: ...

class BRepClass_FClassifier:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: BRepClass_FaceExplorer, P: gp_Pnt2d, Tol: float) -> None: ...
	def Edge(self) -> BRepClass_Edge: ...
	def EdgeParameter(self) -> float: ...
	def NoWires(self) -> bool: ...
	def Perform(self, F: BRepClass_FaceExplorer, P: gp_Pnt2d, Tol: float) -> None: ...
	def Position(self) -> IntRes2d_Position: ...
	def Rejected(self) -> bool: ...
	def State(self) -> TopAbs_State: ...

class BRepClass_FaceExplorer:
	def __init__(self, F: TopoDS_Face) -> None: ...
	def CheckPoint(self, thePoint: gp_Pnt2d) -> bool: ...
	def CurrentEdge(self, E: BRepClass_Edge, Or: TopAbs_Orientation) -> None: ...
	def InitEdges(self) -> None: ...
	def InitWires(self) -> None: ...
	def MoreEdges(self) -> bool: ...
	def MoreWires(self) -> bool: ...
	def NextEdge(self) -> None: ...
	def NextWire(self) -> None: ...
	def OtherSegment(self, P: gp_Pnt2d, L: gp_Lin2d) -> Tuple[bool, float]: ...
	def Reject(self, P: gp_Pnt2d) -> bool: ...
	def RejectEdge(self, L: gp_Lin2d, Par: float) -> bool: ...
	def RejectWire(self, L: gp_Lin2d, Par: float) -> bool: ...
	def Segment(self, P: gp_Pnt2d, L: gp_Lin2d) -> Tuple[bool, float]: ...

class BRepClass_FacePassiveClassifier:
	def __init__(self) -> None: ...
	def ClosestIntersection(self) -> int: ...
	def Compare(self, E: BRepClass_Edge, Or: TopAbs_Orientation) -> None: ...
	def Intersector(self) -> BRepClass_Intersector: ...
	def IsHeadOrEnd(self) -> bool: ...
	def Parameter(self) -> float: ...
	def Reset(self, L: gp_Lin2d, P: float, Tol: float) -> None: ...
	def State(self) -> TopAbs_State: ...

class BRepClass_Intersector(Geom2dInt_IntConicCurveOfGInter):
	def __init__(self) -> None: ...
	def LocalGeometry(self, E: BRepClass_Edge, U: float, T: gp_Dir2d, N: gp_Dir2d) -> float: ...
	def Perform(self, L: gp_Lin2d, P: float, Tol: float, E: BRepClass_Edge) -> None: ...

#classnotwrapped
class BRepClass_FaceClassifier:
	pass

# harray1 classes
# harray2 classes
# harray2 classes

