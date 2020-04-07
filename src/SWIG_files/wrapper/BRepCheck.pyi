from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *


class BRepCheck_Status:
	BRepCheck_NoError: int = ...
	BRepCheck_InvalidPointOnCurve: int = ...
	BRepCheck_InvalidPointOnCurveOnSurface: int = ...
	BRepCheck_InvalidPointOnSurface: int = ...
	BRepCheck_No3DCurve: int = ...
	BRepCheck_Multiple3DCurve: int = ...
	BRepCheck_Invalid3DCurve: int = ...
	BRepCheck_NoCurveOnSurface: int = ...
	BRepCheck_InvalidCurveOnSurface: int = ...
	BRepCheck_InvalidCurveOnClosedSurface: int = ...
	BRepCheck_InvalidSameRangeFlag: int = ...
	BRepCheck_InvalidSameParameterFlag: int = ...
	BRepCheck_InvalidDegeneratedFlag: int = ...
	BRepCheck_FreeEdge: int = ...
	BRepCheck_InvalidMultiConnexity: int = ...
	BRepCheck_InvalidRange: int = ...
	BRepCheck_EmptyWire: int = ...
	BRepCheck_RedundantEdge: int = ...
	BRepCheck_SelfIntersectingWire: int = ...
	BRepCheck_NoSurface: int = ...
	BRepCheck_InvalidWire: int = ...
	BRepCheck_RedundantWire: int = ...
	BRepCheck_IntersectingWires: int = ...
	BRepCheck_InvalidImbricationOfWires: int = ...
	BRepCheck_EmptyShell: int = ...
	BRepCheck_RedundantFace: int = ...
	BRepCheck_InvalidImbricationOfShells: int = ...
	BRepCheck_UnorientableShape: int = ...
	BRepCheck_NotClosed: int = ...
	BRepCheck_NotConnected: int = ...
	BRepCheck_SubshapeNotInShape: int = ...
	BRepCheck_BadOrientation: int = ...
	BRepCheck_BadOrientationOfSubshape: int = ...
	BRepCheck_InvalidPolygonOnTriangulation: int = ...
	BRepCheck_InvalidToleranceValue: int = ...
	BRepCheck_EnclosedRegion: int = ...
	BRepCheck_CheckFail: int = ...

class BRepCheck:
	@staticmethod
	def Add(self, List: BRepCheck_ListOfStatus, Stat: BRepCheck_Status) -> None: ...
	@staticmethod
	def PrecCurve(self, aAC3D: Adaptor3d_Curve) -> float: ...
	@staticmethod
	def PrecSurface(self, aAHSurf: Adaptor3d_HSurface) -> float: ...
	@staticmethod
	def SelfIntersection(self, W: TopoDS_Wire, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge) -> bool: ...

class BRepCheck_Analyzer:
	def __init__(self, S: TopoDS_Shape, GeomControls: Optional[bool]) -> None: ...
	def Init(self, S: TopoDS_Shape, GeomControls: Optional[bool]) -> None: ...
	def IsValid(self, S: TopoDS_Shape) -> bool: ...
	def IsValid(self) -> bool: ...
	def Result(self, SubS: TopoDS_Shape) -> BRepCheck_Result: ...

class BRepCheck_Result(Standard_Transient):
	def Blind(self) -> None: ...
	def ContextualShape(self) -> TopoDS_Shape: ...
	def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def InitContextIterator(self) -> None: ...
	def IsBlind(self) -> bool: ...
	def IsMinimum(self) -> bool: ...
	def Minimum(self) -> None: ...
	def MoreShapeInContext(self) -> bool: ...
	def NextShapeInContext(self) -> None: ...
	def SetFailStatus(self, S: TopoDS_Shape) -> None: ...
	def Status(self) -> BRepCheck_ListOfStatus: ...
	def StatusOnShape(self, S: TopoDS_Shape) -> BRepCheck_ListOfStatus: ...
	def StatusOnShape(self) -> BRepCheck_ListOfStatus: ...

class BRepCheck_Edge(BRepCheck_Result):
	def __init__(self, E: TopoDS_Edge) -> None: ...
	def Blind(self) -> None: ...
	def CheckPolygonOnTriangulation(self, theEdge: TopoDS_Edge) -> BRepCheck_Status: ...
	def GeometricControls(self) -> bool: ...
	def GeometricControls(self, B: bool) -> None: ...
	def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
	def Minimum(self) -> None: ...
	def SetStatus(self, theStatus: BRepCheck_Status) -> None: ...
	def Tolerance(self) -> float: ...

class BRepCheck_Face(BRepCheck_Result):
	def __init__(self, F: TopoDS_Face) -> None: ...
	def Blind(self) -> None: ...
	def ClassifyWires(self, Update: Optional[bool]) -> BRepCheck_Status: ...
	def GeometricControls(self) -> bool: ...
	def GeometricControls(self, B: bool) -> None: ...
	def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
	def IntersectWires(self, Update: Optional[bool]) -> BRepCheck_Status: ...
	def IsUnorientable(self) -> bool: ...
	def Minimum(self) -> None: ...
	def OrientationOfWires(self, Update: Optional[bool]) -> BRepCheck_Status: ...
	def SetStatus(self, theStatus: BRepCheck_Status) -> None: ...
	def SetUnorientable(self) -> None: ...

class BRepCheck_Shell(BRepCheck_Result):
	def __init__(self, S: TopoDS_Shell) -> None: ...
	def Blind(self) -> None: ...
	def Closed(self, Update: Optional[bool]) -> BRepCheck_Status: ...
	def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
	def IsUnorientable(self) -> bool: ...
	def Minimum(self) -> None: ...
	def NbConnectedSet(self, theSets: TopTools_ListOfShape) -> int: ...
	def Orientation(self, Update: Optional[bool]) -> BRepCheck_Status: ...
	def SetUnorientable(self) -> None: ...

class BRepCheck_Solid(BRepCheck_Result):
	def __init__(self, theS: TopoDS_Solid) -> None: ...
	def Blind(self) -> None: ...
	def InContext(self, theContextShape: TopoDS_Shape) -> None: ...
	def Minimum(self) -> None: ...

class BRepCheck_Vertex(BRepCheck_Result):
	def __init__(self, V: TopoDS_Vertex) -> None: ...
	def Blind(self) -> None: ...
	def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
	def Minimum(self) -> None: ...
	def Tolerance(self) -> float: ...

class BRepCheck_Wire(BRepCheck_Result):
	def __init__(self, W: TopoDS_Wire) -> None: ...
	def Blind(self) -> None: ...
	def Closed(self, Update: Optional[bool]) -> BRepCheck_Status: ...
	def Closed2d(self, F: TopoDS_Face, Update: Optional[bool]) -> BRepCheck_Status: ...
	def GeometricControls(self) -> bool: ...
	def GeometricControls(self, B: bool) -> None: ...
	def InContext(self, ContextShape: TopoDS_Shape) -> None: ...
	def Minimum(self) -> None: ...
	def Orientation(self, F: TopoDS_Face, Update: Optional[bool]) -> BRepCheck_Status: ...
	def SelfIntersect(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, Update: Optional[bool]) -> BRepCheck_Status: ...
	def SetStatus(self, theStatus: BRepCheck_Status) -> None: ...
